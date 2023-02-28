from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import PetAdoptForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-pet"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def homepage():
   pets = Pet.query.all()
   return render_template("index.html", pets = pets)

@app.route("/add", methods=["GET", "POST"])
def add_snack():
    """Add a pet """
    form = PetAdoptForm()

    if form.validate_on_submit():
        petname = form.petname.data
        species = form.species.data
        photourl = form.photourl.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=petname, species=species, photo_url=photourl, age = age, notes = notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"{petname} is Added")


        return redirect('/')

    else:
        return render_template("pet_add_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet and an updation"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} details are updated.")
        return redirect('/')

    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)
