"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User, UserService
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route('/')
def home_page():
    return render_template('userlist.html')

@app.route('/users')
def userlist_page():
    users = UserService.get_users()
    return render_template('userlist.html', users =users)

@app.route('/users/new')
def adduser_page():
    return render_template('newuser.html')

@app.route('/users/new', methods = ["POST"])
def addeduser_page():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    img = request.form.get('image')
    user = User(first_name = fname, last_name = lname, image_url = img)
    UserService.save_user(user)
    return redirect("/users")

@app.route('/users/<user_id>')
def getuser_page(user_id):
    user = UserService.get_user_detail(user_id)
    return render_template('userdetail.html', user = user)

@app.route('/users/<user_id>/edit')
def edituser_page(user_id):
    user = UserService.get_user_detail(user_id)
    return render_template('edituser.html',user = user)

@app.route('/users/<user_id>/edit', methods = ["POST"])
def editeduser_page(user_id):
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    img = request.form.get('image')
    user = User(id = user_id, first_name = fname, last_name = lname, image_url = img)
    UserService.update_user(user)
    return redirect("/users")

@app.route('/users/<user_id>/delete', methods = ["POST"])
def deleteuser_page(user_id):
    user = UserService.delete_user(user_id)
    return redirect("/users")





