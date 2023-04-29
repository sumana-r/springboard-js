from flask import Flask, render_template, redirect, flash, request, jsonify, json, session, g
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from forms import UserAddForm, LoginForm, CategoryForm, SubCategoryForm, ShowCategoryForm, ShowSubCategoryForm, TagForm,ExpenseForm
from models import db, connect_db, User, Category, SubCategory, Tag, Expense

CURR_USER_KEY = "curr_user"

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///expense_tracker"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "secret expense"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)
# db.drop_all()
db.create_all()

@app.route('/', methods=["GET", "POST"])
def homepage():
    return render_template("base.html")


########### Current User login and logout ##############

@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
         session.pop(CURR_USER_KEY,None)



############### User Registration ########################

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = UserAddForm()
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

    if form.validate_on_submit():
        try:
            user = User.signup(
                fname=form.fname.data,
                lname=form.lname.data,
                username=form.username.data,
                email=form.email.data,
                password=form.password.data,
            )
            db.session.commit()
        except IntegrityError as e:
            flash("Username already taken", 'danger')
            return render_template('signup.html', form=form)
        
        do_login(user)

        return redirect("/")
   
    else:
        return render_template("signup.html", form=form)

################ User Login ####################

@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('login.html', form=form)

################### User Logout ####################

@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()

    flash("You have successfully logged out.", 'success')
    return redirect("/login")

################### Show, Add, Delete Category ################

@app.route('/category', methods=["GET", "POST"])
def showcategory():
    form = ShowCategoryForm()
    user=g.user
    categorylist = Category.query.filter(Category.user_id == user.id).all()
    form.categories.choices = [(c.id, c.categoryname) for c in categorylist]
 
    return render_template('showcategory.html', form=form)

@app.route('/category/add', methods=["GET", "POST"])

def categorypage():
    form = CategoryForm()
    if form.validate_on_submit():
        try:
            category= Category(
                    categoryname=form.categoryname.data,
                    user_id=g.user.id
            )
                   
            db.session.add(category)
            db.session.commit()
           
        except IntegrityError as e:
            flash("Category Error", 'danger')            

    
    return render_template('category.html', form=form)

################### Add, Delete SubCategory ################
@app.route('/subcategory', methods=["GET", "POST"])
def showsubcategory():
    form = ShowSubCategoryForm()
    user=g.user
    subcategorylist = SubCategory.query.filter(SubCategory.user_id == user.id).all()
    form.subcategories.choices = [(c.id, c.categoryname) for c in subcategorylist]
    return render_template('showsubcategory.html', form=form)

@app.route('/subcategory/add', methods=["GET", "POST"])
def subcategorypage():
    form = SubCategoryForm()
    categorylist = Category.query.filter(Category.user_id == g.user.id).all()
    form.categories.choices = [(c.id, c.categoryname) for c in categorylist]
    print("###################################")
    print(form.categories.data)
    if form.validate_on_submit():
        try:
            subcategory= SubCategory(
                    subcategoryname=form.subcategoryname.data,
                    category_id = form.categories.data,
                    user_id=g.user.id,
            )
                   
            db.session.add(subcategory)
            db.session.commit()
           
        except IntegrityError as e:
            flash("SubCategory Error ", 'danger')         

    
    return render_template('subcategory.html', form=form)

@app.route('/tags', methods=["GET", "POST"])
def tagpage():
    form = TagForm()
    tagslists = Tag.query.filter(Tag.user_id == g.user.id).all()
  
    if form.validate_on_submit():
        try:
            tag= Tag(
                    tagname=form.tagname.data,
                    user_id=g.user.id,
            )
                   
            db.session.add(tag)
            db.session.commit()
           
        except IntegrityError as e:
            flash("tag Error ", 'danger')         

    
    return render_template('tags.html', form=form)
@app.route('/expense', methods=["GET", "POST"])
def addexpense():
    form = ExpenseForm()
    categorylist = Category.query.filter(Category.user_id == g.user.id).all()
    form.categories.choices = [(c.id, c.categoryname) for c in categorylist]
    subcategorylist = SubCategory.query.filter(SubCategory.user_id == g.user.id).all()
    form.subcategories.choices = [(s.id, s.subcategoryname) for s in subcategorylist]
    if form.validate_on_submit():
        try:
            expense= Expense(
                    user_id=g.user.id,
                    timestamp=form.timestamp.data,
                    expensename=form.expensename.data,
                    category_id = form.categories.data,
                    subcategory_id = form.subcategories.data,
                    amount = form.amount.data
            )
                   
            db.session.add(expense)
            db.session.commit()
           
        except IntegrityError as e:
            flash("expense Error ", 'danger')         

    
    return render_template('expense.html', form=form)