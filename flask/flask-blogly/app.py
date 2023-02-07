"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User, UserService, Post, PostService, Tag, TagService,PostTag
from flask_debugtoolbar import DebugToolbarExtension
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
# db.drop_all()
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


    # Part Two: Post

@app.route('/users/<user_id>/posts/new')
def addpost_page(user_id):
    user = UserService.get_user_detail(user_id)
    tags = TagService.get_alltags()
    return render_template('newpost.html', user = user, tags = tags)

@app.route('/users/<user_id>/posts/new', methods = ["POST"])
def addedpost_page(user_id):
    title = request.form.get('ptitle')
    content = request.form.get('pcontent')
    created_at = date.today()
    tagids = request.form.getlist('tagid')
    post = Post(title = title, content = content,created_at = created_at, user_id=user_id)
    PostService.save_post(post)
    post_id = post.id
    for tagid in tagids:
       posttag = PostTag(postid=post_id, tagid=tagid)
       db.session.add(posttag)
       db.session.commit()
    return redirect("/users/"+ user_id)

@app.route('/posts/<post_id>')
def postlist_page(post_id):
    post = PostService.get_post(post_id)
    tags = post.tag
    return render_template('postdetail.html', post =post, tags = tags)

@app.route('/posts/<post_id>/delete', methods = ["POST"])
def delete_post_page(post_id):
    post = PostService.get_post(post_id)
    PostService.delete_post(post_id)
    return redirect("/users/"+ str(post.user_id))

@app.route('/posts/<post_id>/edit')
def editpost_page(post_id):
    post = PostService.get_post(post_id)
    tags = TagService.get_alltags()
    posttags = post.tag
    selecttagids = set(x.id for x in posttags)
    viewtags = []
    for tag in tags:
        currtag = {"id" : tag.id, "name": tag.tagname, "selected":True if tag.id in selecttagids else False}
        viewtags.append(currtag)

    return render_template('postedit.html',post = post, tags = viewtags)

@app.route('/posts/<post_id>/edit', methods = ["POST"])
def editedpost_page(post_id):
    title = request.form.get('title')
    content = request.form.get('content')
    created_at = date.today()
    tagids = [int(tagid) for tagid in request.form.getlist('tagid')]
    post = PostService.get_post(post_id)
    post.tags = Tag.query.filter(Tag.id.in_(tagids)).all()
    db.session.add(post)
    db.session.commit()
    updatedpost = Post(id = post_id, title = title, content = content, created_at = created_at, user_id = post.user_id )
    PostService.update_post(updatedpost)
    return redirect("/users/"+ str(post.user_id))


    # Part 3: Tags

@app.route('/tags')
def tags_list():
    tags = TagService.get_alltags()
    return render_template('taglist.html', tags=tags)

@app.route('/tags/new')
def tags_new_form():
    return render_template('addtag.html')

@app.route("/tags/new", methods=["POST"])
def addtags_page():
    tagname = request.form.get('tagname')
    tag = Tag(tagname = tagname)
    TagService.save_tag(tag)
    return redirect("/tags")

@app.route('/tags/<tag_id>') 
def tag_show_page(tag_id):
    tag = TagService.get_a_tag(tag_id)
    
    posts = tag.posts
    return render_template('showtag.html', tag = tag, posts = posts)
    

@app.route('/tags/<tag_id>/edit')
def tag_edit_page(tag_id):
    tag = TagService.get_a_tag(tag_id)
    post = PostService.get_allpost()
    return render_template('edittag.html', tag = tag, post = post)
    
@app.route('/tags/<tag_id>/edit', methods=["POST"])
def tag_editted(tag_id):
    tag = TagService.get_a_tag(tag_id)
    tagname = request.form.get('edit_tag')
    updatedtag = Tag(id = tag_id, tagname = tagname)
    TagService.update_tag(updatedtag)
    post_ids = [int(postid) for postid in request.form.getlist("posts")]
    tag.posts = Post.query.filter(Post.id.in_(post_ids)).all()

    db.session.add(tag)
    db.session.commit()
    return redirect("/tags")

@app.route('/tags/<tag_id>/delete', methods=["POST"])
def tags_destroy(tag_id):
    tag = TagService.get_a_tag(tag_id)
    db.session.delete(tag) 
    db.session.commit()
    return redirect("/tags")





