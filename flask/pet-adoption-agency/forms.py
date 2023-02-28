from flask_wtf import FlaskForm
from wtforms import StringField,  IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, Length, url

class PetAdoptForm(FlaskForm):
    """Add the New Pet details"""
    petname = StringField("Pet name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photourl = StringField("Photo URL", validators=[Optional(), NumberRange(min=0, max=10, message='The age must be between 0 to 30')])
    age = IntegerField("Age", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Edit the Pet details"""

    photo_url = StringField("Photo URL", validators=[Optional(), url()])
    notes = StringField("Comments", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")


