import os

from flask import Flask, request, render_template, Response

from helpers import sentiment_score

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('video.html');

@app.route('/sentiment/<sentence>')
def sentiment(sentence):
    score = sentiment_score(sentence)
    return Response(str(score))

if __name__ == '__main__':
    #setup dev server
    app.debug = True
    app.run(host='localhost', port=8080)
