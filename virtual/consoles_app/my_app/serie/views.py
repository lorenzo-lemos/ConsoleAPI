import json 
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from my_app.serie.models import Serie
from my_app import api, db

serie = Blueprint('serie',__name__)

parser = reqparse.RequestParser()
parser.add_argument('name',type=str)
parser.add_argument('genre',type=str)
parser.add_argument('season',type=int)
parser.add_argument('average',type=int)
parser.add_argument('isActive',type=str)

@serie.route("/")
@serie.route("/home")

def home():
    return "Catálogo de Series"

class SerieAPI(Resource):
    def get(self,id=None,page=1):
        if not id:
            series = Serie.query.paginate(page,10).items
        else:
            series = [Serie.query.get(id)]
        if not series:
            abort(404)
        res = {}
        for ser in series:
            res[ser.id] = {
                'name' : ser.name,
                'genre' : ser.genre,
                'season' : ser.season,
                'average' : ser.average,
                'isActive' : ser.isActive,
            }
        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        name = args['name']
        genre = args['genre']
        season = args['season']
        average = args['average']
        isActive = args['isActive']

        ser = Serie(name,genre,season,average,isActive)
        db.session.add(ser)
        db.session.commit()
        res = {}
        res[ser.id] = {
            'name' : ser.name,
            'genre' : ser.genre,
            'season' : ser.season,
            'average' : ser.average,
            'isActive' : ser.isActive,
        }
        return json.dumps(res)

api.add_resource(
    SerieAPI,
    '/api/serie',
    '/api/serie/<int:id>',
    '/api/serie/<int:id>/<int:page>'
)