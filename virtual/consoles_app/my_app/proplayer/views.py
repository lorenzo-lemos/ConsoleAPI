import json 
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from my_app.proplayer.models import Proplayer
from my_app import api, db

proplayer = Blueprint('proplayer',__name__)

parser = reqparse.RequestParser()
parser.add_argument('name',type=str)
parser.add_argument('name_team',type=str)
parser.add_argument('role',type=str)
parser.add_argument('kills',type=int)
parser.add_argument('assists',type=int)
parser.add_argument('deads',type=int)
parser.add_argument('m_played',type=int)
parser.add_argument('m_win',type=int)

@proplayer.route("/")
@proplayer.route("/home")

def home():
    return "Catálogo de Proplayers"

class ProplayerAPI(Resource):
    def get(self,id=None,page=1):
        if not id:
            proplayers = Proplayer.query.paginate(page,10).items
        else:
            proplayers = [Proplayer.query.get(id)]
        if not proplayers:
            abort(404)
        res = {}
        for pro in proplayers:
            res[pro.id] = {
                'name' : pro.name,
                'name_team' : pro.name_team,
                'role' : pro.role,
                'kills' : pro.kills,
                'assists' : pro.assists,
                'deads' : pro.deads,
                'm_played' : pro.m_played,
                'm_win' : pro.m_win,
                'KDA' : (pro.kills+pro.assists) if (pro.deads == 0 ) else (pro.kills+pro.assists)/(pro.deads),
                '% Win' : (pro.m_win/pro.m_played)
            }
        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        name = args['name']
        name_team = args['name_team']
        role = args['role']
        kills = args['kills']
        assists = args['assists']
        deads = args['deads']
        m_played = args['m_played']
        m_win = args['m_win']

        pro = Proplayer(name,name_team,role,kills,assists,deads,m_played,m_win)
        db.session.add(pro)
        db.session.commit()
        res = {}
        res[pro.id] = {
                'name' : pro.name,
                'name_team' : pro.name_team,
                'role' : pro.role,
                'kills' : pro.kills,
                'assists' : pro.assists,
                'deads' : pro.deads,
                'm_played' : pro.m_played,
                'm_win' : pro.m_win
        }
        return json.dumps(res)

    def delete(self,id):
        pro = Proplayer.query.get(id)
        db.session.delete(pro)
        db.session.commit()
        res = {'id':id}
        return json.dumps(res)

    def put(self,id):
        pro = Proplayer.query.get(id)
        args = parser.parse_args()
        name = args['name']
        name_team = args['name_team']
        role = args['role']
        kills = args['kills']
        assists = args['assists']
        deads = args['deads']
        m_played = args['m_played']
        m_win = args['m_win']
        pro.name = name
        pro.name_team = name_team
        pro.role = role
        pro.kills = kills
        pro.assists = assists
        pro.deads = deads
        pro.m_played = m_played
        pro.m_win = m_win
        db.session.commit()
        res = {}
        res[pro.id] = {
            'name' : pro.name,
            'name_team' : pro.name_team,
            'role' : pro.role,
            'kills' : pro.kills,
            'assists' : pro.assists,
            'deads' : pro.deads,
            'm_played' : pro.m_played,
            'm_win' : pro.m_win
        }
        return json.dumps(res)
        
api.add_resource(
    ProplayerAPI,
    '/api/proplayer',
    '/api/proplayer/<int:id>',
    '/api/proplayer/<int:id>/<int:page>'
)