'''SQLAlchemy models for Daily Expense Tracker'''

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from datetime import datetime

bcrypt = Bcrypt()
db = SQLAlchemy()

class User(db.Model):
    '''User detail'''

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    fname = db.Column(
        db.Text,
        nullable=False,
    )

    lname = db.Column(
        db.Text,
        nullable=False,
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    password = db.Column(
        db.Text,
        nullable=False,
    )

    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"
    
    @classmethod
    def signup(cls, fname, lname, username, email, password):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            fname=fname,
            lname=lname,
            username=username,
            email=email,
            password=hashed_pwd,
            
        )

        db.session.add(user)
        return user
    
    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    tagname = db.Column(
        db.Text,
        nullable=False,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    categoryname = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,        
    )

  

class SubCategory(db.Model):
    __tablename__ = 'subcategories'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    subcategoryname = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey('categories.id', ondelete='CASCADE'),
        nullable=False,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,        
    )


class Expense(db.Model):
    __tablename__ = 'expenses'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )
    timestamp = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )

    expensename = db.Column(
        db.Text,
        nullable=False,
    )
    category_id = db.Column(
        db.Integer,
        db.ForeignKey('categories.id', ondelete='CASCADE'),
        nullable=False,
    )

    subcategory_id = db.Column(
        db.Integer,
        db.ForeignKey('subcategories.id', ondelete='CASCADE'),
        nullable=False,
    )

    amount = db.Column(
        db.Integer,
        nullable=False,
    )




class ExpenseTag(db.Model):
    """Mapping user Expenses"""

    __tablename__ = 'expensetags' 

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    tag_id = db.Column(
        db.Integer,
        db.ForeignKey('tags.id', ondelete='cascade')
    )

    expense_id = db.Column(
        db.Integer,
        db.ForeignKey('expenses.id', ondelete='cascade')
    )


    



def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    app.app_context().push()
    db.init_app(app)
