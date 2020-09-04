import sys
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from flask import (
    make_response,
    abort,
)

from models.answer_model import (
    Clue,
    ClueSchema,
)

def read_all():
    """
    Request response for /api/answers
    :return: json of answers
    """
    clue = Clue.query.all()
    clue_schema = ClueSchema(many=True)
    return clue_schema.dump(clue)

def read_one(clue_id):
    """
    Request response for /api/answers/{clue_id}
    :return: json of answers
    """
    answer = Clue.query \
            .filter(Clue.answer_id == clue_id) \
            .one_or_none()

    if answer is not None:
        clue_schema = ClueSchema(many=True)
        return clue_schema.dump(answer)
    else:
        abort(404, f'Answer not found for ID: {clue_id}')