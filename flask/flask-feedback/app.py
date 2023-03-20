from flask import Flask, render_template, flash, redirect, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db,User, Feedback
from forms import UserForm, UserLoginForm, FeedbackForm, DeleteForm
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import Unauthorized



app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-feedback"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///feedbacks"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/register', methods=['GET'])
def get_register_user():
    form = UserForm()
    return render_template('register.html', form=form)  


@app.route('/register', methods=['POST'])
def register_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        new_user = User.register(username, password, email, first_name, last_name)

        db.session.add(new_user)
        try:
            db.session.commit()
            session['username'] = new_user.username
            
        except IntegrityError:
            form.username.errors.append('Username taken.  Please pick another')
            return render_template('index.html')

        redirect_url = url_for('secret_home', username=new_user.username)
        return redirect(redirect_url)
    
    


@app.route('/login', methods=['GET'])
def get_login_user():
    form = UserLoginForm()
    return render_template('login.html', form=form)


@app.route('/login', methods=['POST'])
def login_user():
    if "username" in session:
        return redirect(f"/users/{session['username']}")

    form = UserLoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            flash(f"Welcome Back, {user.username}!", "primary")
            session['username'] = user.username
            redirect_url = url_for('secret_home', username=user.username)
            return redirect(redirect_url)
        else:
            form.username.errors = ['Invalid username/password.']
            return render_template("login.html", form=form)

    return redirect('/login')


# @app.route('/users/<username>', methods=['GET'])
# def secret_home(username):
#     # if username not in session:
#     #     flash("Please login")
#     #     return redirect('/')          
#     return render_template('secret.html')

@app.route('/logout')
def logout_user():
    session.pop('username')
    return redirect('/')

@app.route('/users/<username>', methods=['GET'])
def show_feedbacks(username):
    if "username" not in session:
        flash("Please login to see your feedback!", "danger")
        return redirect('/')
    user = User.query.get_or_404(username)
    form = FeedbackForm()

    return render_template("show.html", user=user, form=form)

@app.route("/users/<username>/delete", methods=["POST"])
def remove_user(username):
    """Remove user nad redirect to login."""

    if "username" not in session or username != session['username']:
        flash("Please login to see your feedback!", "danger")
        return redirect('/')

    user = User.query.get_or_404(username)
    db.session.delete(user)
    db.session.commit()
    session.pop("username")

    return redirect("/login")     


@app.route("/users/<username>/feedback/new", methods=["GET", "POST"])
def new_feedback(username):
    """Show add-feedback form to create feedback"""

    if "username" not in session or username != session['username']:
        raise Unauthorized()

    form = FeedbackForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        feedback = Feedback(
            title=title,
            content=content,
            username=username,
        )

        db.session.add(feedback)
        db.session.commit()

        return redirect(f"/users/{feedback.username}")

    else:
        return render_template("add-feedback.html", form=form)


@app.route("/feedback/<int:feedback_id>/update", methods=["GET", "POST"])
def update_feedback(feedback_id):
    """Show edit-feedback form """

    feedback = Feedback.query.get(feedback_id)

    if "username" not in session or feedback.username != session['username']:
        raise Unauthorized()

    form = FeedbackForm(obj=feedback)

    if form.validate_on_submit():
        feedback.title = form.title.data
        feedback.content = form.content.data

        db.session.commit()

        return redirect(f"/users/{feedback.username}")

    return render_template("edit-feedback.html", form=form, feedback=feedback)


@app.route("/feedback/<int:feedback_id>/delete", methods=["POST"])
def delete_feedback(feedback_id):
    """Delete feedback."""

    feedback = Feedback.query.get(feedback_id)
    if "username" not in session or feedback.username != session['username']:
        raise Unauthorized()

    form = DeleteForm()

    if form.validate_on_submit():
        db.session.delete(feedback)
        db.session.commit()

    return redirect(f"/users/{feedback.username}")


