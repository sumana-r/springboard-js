from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension


app =  Flask(__name__)
app.config['SECRET_KEY']= "appsecret"
debug = DebugToolbarExtension(app)

@app.route('/')
def prompt_form():
    prompt_list = story.prompts
    return render_template("prompt.html", prompts = prompt_list)

@app.route('/story')
def story_generate():
    text = story.generate(request.args)
    return render_template("story.html", text = text)


