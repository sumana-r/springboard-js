"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app =  app
    app.app_context().push()
    db.init_app(app)
   

class User(db.Model):
    
    __tablename__ = "User"

    def __repr__(self):
        return f"self.id, self.first_name, self.last_name, self.image_url"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(20),
                     nullable=False)
    last_name = db.Column(db.String(20),
                     nullable=False)
    image_url = db.Column(db.Text, nullable=True)

    
class UserService():
    def save_user(user: User):
        db.session.add(user)
        db.session.commit()
    def get_users():
      return  User.query.all()
    def get_user_detail(id):
      return  User.query.get(id)
    def update_user(user:User):
        edit_user = User.query.get(user.id)
        edit_user.first_name = user.first_name
        edit_user.last_name = user.last_name
        edit_user.image_url = user.image_url
        db.session.add(edit_user)
        db.session.commit()

    def delete_user(id):
        delete_user = User.query.get(id)
        db.session.delete(delete_user)
        db.session.commit()

        
        
        
        

       



