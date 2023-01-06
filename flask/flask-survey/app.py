from flask import Flask, request, render_template, redirect, flash, session
from surveys import Question,  satisfaction_survey
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY']= "surveysecret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

  

@app.route('/')
def survey_form():
    satisfaction_surveytitle = satisfaction_survey.title
    satisfaction_surveyinst = satisfaction_survey.instructions
    return render_template("survey.html", title = satisfaction_surveytitle,instruction = satisfaction_surveyinst,request = request)

@app.route('/questions/<int:index>')
def question_form(index):
    if index == len(satisfaction_survey.questions):
        return render_template("thank.html") 
    else:
        index = min(index,get_resp_len())   
        question_obj = satisfaction_survey.questions[index]
        return render_template("question.html", question_obj= question_obj,index=index)

@app.route('/answer', methods=["POST"])
def answer_form():
    
    cur_index = request.form["cur_index"]
    index = int(cur_index ) + 1
    if index <= len(satisfaction_survey.questions):
        
        selected_choice = request.form.get("choice")
        
        
        if selected_choice == None:
            flash("Choose the choice")
            return redirect('/questions/' +  cur_index)
        else:
            
            add_choice(selected_choice)
            return redirect('/questions/' +  str(index))
        
    else:
        return render_template("thank.html")

def add_choice(choice):
        responses = session.get('responses')
        if responses is None:
            responses = []
        responses.append(choice)
        session['responses'] = responses

def get_resp_len():
     
    return  0 if(session.get('responses') is None) else len(session['responses'])


        
        











