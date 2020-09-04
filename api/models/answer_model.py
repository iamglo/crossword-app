import sys
import os
import inspect
from marshmallow import fields

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from database.config import db, ma
# from models.clue_model import Clue


class Clue(db.Model):
    __tablename__ = 'clues'
    clue_id = db.Column(db.Integer,
                        primary_key=True)
    clue = db.Column(db.String(32))
    date = db.Column(db.String(32))
    source = db.Column(db.String(32))

    answer = db.relationship(
        "Answer",
        secondary="mapping",
    )

class Answer(db.Model):
    __tablename__ = 'answers'
    answer_id = db.Column(db.Integer,
                          primary_key=True)
    answer = db.Column(db.String(32))
    clue = db.relationship(
        "Clue",
        secondary="mapping"
    )

class MappingDetail(db.Model):
    __tablename__ = 'mapping'
    id = db.Column(db.Integer,
                   primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey('answers.answer_id'))
    clue_id = db.Column(db.Integer, db.ForeignKey('clues.clue_id'))

class AnswerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Answer
        sqla_session = db.session
    clue = fields.Nested('AnswerClueSchema', default=[], many=True)

class MappingDetailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MappingDetail
        sqla_session = db.session

class AnswerClueSchema(ma.SQLAlchemyAutoSchema):
    clue_id = fields.Int()
    answer_id = fields.Int()
    clue = fields.Str()
    date = fields.Str()
    source = fields.Str()

class ClueAnswerSchema(ma.SQLAlchemyAutoSchema):
    answer = fields.Str()
    answer_id = fields.Int()

class ClueSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Clue
        sqla_session = db.session

    answer = fields.Nested('ClueAnswerSchema', default=[], many=True)