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

from models.models import (
    Answer,
    AnswerSchema,
    Clue
)

def read():
    """
    Request response for /api/answers
    :return: json of answers
    """
    id_filt = [int(x) for x in request.args.getlist("id")]
    # error exceptions for other arguments

    if len(id_filt) > 0:
        answer = Answer.query \
        .filter(Answer.answer_id.in_(id_filt))
    else:
        answer = Answer.query

    answer_schema = AnswerSchema(many=True)
    return answer_schema.dump(answer.all())

# def read_one(answer_id):
#     """
#     Request response for /api/answers/{answer_id}
#     :return: json of answers
#     """
#     answer = Answer.query \
#             .filter(Answer.answer_id == answer_id) \
#             .one_or_none()
#
#     if answer is not None:
#         answer_schema = AnswerSchema()
#         return answer_schema.dump(answer)
#     else:
#         abort(404, f'Answer not found for ID: {answer_id}')

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