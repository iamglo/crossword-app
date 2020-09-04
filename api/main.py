"""
API Calls
/source/clue/*keyword => {*clue: {answer: *answer, date: *date}}
/source/answer/*answer => {*clue: {date: *date}}

/source/all
/source/date/*date => answer:clue
/source/date/month/*number
/source/date/year/*number
"""

import flask
import connexion
from flask import request, jsonify, render_template

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8088, debug=True)