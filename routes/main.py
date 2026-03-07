from flask import Blueprint, jsonify

from data.database import db
from data.models.form import Form

page = Blueprint(__name__, __name__)

@page.route('/list-forms', methods = ['GET'])
def list_forms():
    _query = db.select(Form)
    forms: list[Form] = db.session.execute(_query).scalars()
    return jsonify({'forms': [str(_) for _ in forms]})