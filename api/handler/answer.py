import sys
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from flask import (
    abort,
)

from models.answer_model import (
    Answer,
    AnswerSchema,
    Clue
)


def read_all():
    """
    Request response for /api/answers
    :return: json of answers
    """
    answer = Answer.query.all()
    answer_schema = AnswerSchema(many=True)
    return answer_schema.dump(answer)

def read_one(answer_id):
    """
    Request response for /api/answers/{answer_id}
    :return: json of answers
    """
    answer = Answer.query \
            .filter(Answer.answer_id == answer_id) \
            .one_or_none()

    if answer is not None:
        answer_schema = AnswerSchema()
        return answer_schema.dump(answer)
    else:
        abort(404, f'Answer not found for ID: {answer_id}')