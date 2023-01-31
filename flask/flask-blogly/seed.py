from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users

John = User(first_name='John', last_name="Anton", image_url="https://www.pngfind.com/pngs/m/470-4703547_icon-user-icon-hd-png-download.png")
Mary = User(first_name='Mary', last_name="Lisa", image_url="https://www.pngfind.com/pngs/m/470-4703547_icon-user-icon-hd-png-download.png")
Tisa = User(first_name='Tisa', last_name="Michael", image_url="https://www.pngfind.com/pngs/m/470-4703547_icon-user-icon-hd-png-download.png")

# Add new objects to session
db.session.add(John)
db.session.add(Mary)
db.session.add(Tisa)

# Commit
db.session.commit()
