"""
API Calls
/api/clue/
    *keyword => {*clue: {answer: *answer, date: *date}}
    *id

/api/answer/
    *keyword => {*clue: {date: *date}}
    *id

/api/crossword/
    *date => {answer:clue}
    *source => source
"""

import connexion
from flask import request, jsonify, render_template
from flask_cors import CORS

app = connexion.App(__name__, specification_dir='./')
CORS(app.app)
app.add_api('swagger.yml')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8088, debug=True)
