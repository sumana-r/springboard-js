"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User, UserService, Post, PostService
from flask_debugtoolbar import DebugToolbarExtension
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


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
    post = PostService.get_userpost_detail(user_id)
    return render_template('userdetail.html', user = user,post =post)

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

@app.route('/users/<user_id>/posts/new')
def addpost_page(user_id):
    user = UserService.get_user_detail(user_id)
    return render_template('newpost.html',user = user)

@app.route('/users/<user_id>/posts/new', methods = ["POST"])
def addedpost_page(user_id):
    title = request.form.get('ptitle')
    content = request.form.get('pcontent')
    created_at = date.today()
    post = Post(title = title, content = content,created_at = created_at, user_id=user_id)
    PostService.save_post(post)
    return redirect("/users/"+ user_id)

@app.route('/posts/<post_id>')
def postlist_page(post_id):
    post = PostService.get_post(post_id)
    return render_template('postdetail.html', post =post)

@app.route('/posts/<post_id>/delete', methods = ["POST"])
def delete_post_page(post_id):
    post = PostService.get_post(post_id)
    PostService.delete_post(post_id)
    return redirect("/users/"+ str(post.user_id))

@app.route('/posts/<post_id>/edit')
def editpost_page(post_id):
    post = PostService.get_post(post_id)
    return render_template('postedit.html',post = post)

@app.route('/posts/<post_id>/edit', methods = ["POST"])
def editedpost_page(post_id):
    title = request.form.get('title')
    content = request.form.get('content')
    created_at = date.today()
    post = PostService.get_post(post_id)
    print("post.user_id")
    updatedpost = Post(id = post_id, title = title, content = content, created_at = created_at, user_id = post.user_id )
    PostService.update_post(updatedpost)
    return redirect("/users/"+ str(post.user_id))

    





