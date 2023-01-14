from boggle import Boggle
from flask import Flask, request, redirect, render_template, session, jsonify, flash
from flask_debugtoolbar import DebugToolbarExtension

board_key = "board"
word_list = "words"

app = Flask(__name__)
app.config['SECRET_KEY']= "surveysecret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


boggle_game = Boggle()


@app.route('/')
def display_board(highscore=0):
    board = boggle_game.make_board() 
    session['board_key'] = board
    score = 0
    session['score'] = score
    
    
    return render_template('boardview.html', board = board, score = session['score'], highscore= highscore )

words = []
wrongwords = []


@app.route('/addWord/<word>',  methods =["POST"])
def check_valid_word(word):
    word = word.lower()
   
    if word not in words:
        board = session['board_key']
        result = boggle_game.check_valid_word(board,word)
        if(result == 'ok'):
           
            words.append(word)
            session['word_list'] = words
            session['score'] = session['score'] + 1
        else:
            request
    else:
         result = "already exist"
 
    return jsonify(result, session['score'])












