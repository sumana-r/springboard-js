"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app =  app
    app.app_context().push()
    db.init_app(app)


class User(db.Model):
    
    __tablename__ = "user"

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
    post = db.relationship('Post', backref='users')

    
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

class Post(db.Model):
    
    __tablename__ = "post"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(30),
                     nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, 
                     nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class PostService():
    def save_post(post:Post):
        db.session.add(post)
        db.session.commit()

    def get_userpost_detail(user_id):
        return  Post.query.filter_by(user_id = user_id).all()

    def get_post(post_id):
        return  Post.query.get(post_id)

    def delete_post(post_id):
        delete_post = Post.query.get(post_id)
        db.session.delete(delete_post)
        db.session.commit()

    def update_post(post:Post):
        edit_post = Post.query.get(post.id)
        edit_post.title = post.title
        edit_post.content = post.content
        edit_post.created_at = post.created_at
        edit_post.user_id = post.user_id
        db.session.add(edit_post)
        db.session.commit()




        
        
        
        

       



