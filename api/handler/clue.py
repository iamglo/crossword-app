import sys
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from flask import (
    make_response,
    abort,
    request
)

from models.models import (
    Clue,
    ClueSchema,
)

def read():
    """
    Request response for /api/clue
    Parses for date, year, day via query parameter
    :return: json of answers
    """
    id_filt = [int(x) for x in request.args.getlist("id")]
    date_filt = request.args.get("date")
    year_filt = request.args.get("year")
    day_filt = request.args.get("day")

    if len(id_filt) > 0:
        clue = Clue.query.filter(Clue.clue_id.in_(id_filt))
    else:
        clue = Clue.query

    if date_filt:
        if len(year_filt) != 8:
            abort(400, f'Please check that year is valid format')
        clue = clue.filter(Clue.date == date_filt)
    if year_filt:
        if len(year_filt) != 4:
            abort(400, f'Please check that year is valid format')
        clue = clue.filter(Clue.date.endswith(year_filt))
    if day_filt:
        clue = clue.filter(Clue.day_of_week == day_filt)

    clue_schema = ClueSchema(many=True)
    return clue_schema.dump(clue.all())

# def read_one(clue_id):
#     """
#     Request response for /api/clue/{clue_id}
#     :return: json of answers
#     """
#     answer = Clue.query \
#             .filter(Clue.clue_id == clue_id) \
#             .one_or_none()
#
#     if answer is not None:
#         clue_schema = ClueSchema(many=True)
#         return clue_schema.dump(answer)
#     else:
#         abort(404, f'Answer not found for ID: {clue_id}')

def search_clue(keyword):
    """
    Request response for /api/clue/{keyword}
    :param keyword:
    :return:
    """
    search_parse = " ".join(keyword.split("+"))
    search_term = f'%{search_parse}%'
    search = Clue.query.filter(Clue.clue.ilike(search_term))

    if search is not None:
        clue_schema = ClueSchema(many=True)
        return clue_schema.dump(search.all())
    else:
        abort(404, f'Answer not found for ID: {keyword}')
