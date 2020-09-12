import sys
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from flask import (
    abort,
    request
)

from database.config import db

from models.models import (
    Answer,
    AnswerSchema,
    Clue,
    VirtualAnswer,
    VirtualAnswerSchema
)

def read_all():
    """
    Request response for /api/answers/all
    :return: json of answers
    """
    page_size = request.args.get("size") or 100
    page_num = request.args.get("page") or 1

    if page_num <= 0 or page_size > 500:
        abort(400, f'Please check if request is valid')

    # error exceptions for other arguments

    answer = Answer.query.paginate(int(page_num), int(page_size)).items

    answer_schema = AnswerSchema(many=True)
    return answer_schema.dump(answer)

def search_answer(keyword):
    """
    Request response for /api/answer/{keyword}
    Search answer using keyword. parse + as space
    :return:
    """
    search_term = f'%{keyword.upper()}%'
    search = Answer.query.filter(Answer.answer.ilike(search_term)).all()

    if search is not None:
        answer_schema = AnswerSchema(many=True)
        return answer_schema.dump(search)
    else:
        abort(404, f'Answer not found for ID: {keyword}')

def search_answer_fts(keyword):
    """"""
    search_parse = 'answer: *' + " ".join(keyword.split("+")) + "*"
    search = db.session.query(VirtualAnswer.answer_id).filter(VirtualAnswer.answer.match(search_parse)).subquery()
    search_full = Answer.query.filter(Answer.answer_id.in_(search)).all()

    if search is not None:
        answer_schema = AnswerSchema(many=True)
        return answer_schema.dump(search_full)
    else:
        abort(404, f'Answer not found for ID: {keyword}')

print(search_answer_fts('ASIA'))