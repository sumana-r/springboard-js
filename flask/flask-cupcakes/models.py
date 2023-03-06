"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

def connect_db(app):
    db.app =  app
    app.app_context().push()
    db.init_app(app)


class Cupcake(db.Model):
    __tablename__ = "cupcake"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    size = db.Column(db.String(30), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=False)
    
    def image(self):
        """Return image for cupcake"""
        return self.image or DEFAULT_IMAGE

    def serialize(self):
        """Returns a dict representation of cupcake which we can turn into JSON"""
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }
    
    def __repr__(self):
        return f"<Todo {self.id} flavor={self.flavor} size={self.size} rating={self.rating} image={self.image} >"


