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


def read_all():
    """
    Request response for /api/clue/all
    :return: json of answers
    """
    page_size = request.args.get("size") or 100
    page_num = request.args.get("page") or 1

    if page_num <= 0 or page_size > 500:
        abort(400, f'Please check if request is valid')

    # error exceptions for other arguments

    clue = Clue.query.paginate(int(page_num), int(page_size)).items

    clue_schema = ClueSchema(many=True)
    return clue_schema.dump(clue)


def read():
    """
    Request response for /api/clue
    Parses for date, year, day via query parameter
    :return: json of answers
    """
    # id_filt = [int(x) for x in request.args.getlist("id")]
    date_filt = request.args.get("date")
    year_filt = request.args.get("year")
    day_filt = request.args.get("day")

    # if len(id_filt) > 0:
    #     clue = Clue.query.filter(Clue.clue_id.in_(id_filt))
    # else:
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

def search_clue(keyword):
    """
    Request response for /api/clue/search/{keyword}
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
