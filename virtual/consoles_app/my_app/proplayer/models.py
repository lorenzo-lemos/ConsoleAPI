from my_app import db

class Proplayer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    name_team = db.Column(db.String(100))
    role = db.Column(db.String(100))
    kills = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    deads = db.Column(db.Integer)
    m_played = db.Column(db.Integer)
    m_win = db.Column(db.Integer)

    def __init__(self,name,name_team,role,kills,assists,deads,m_played,m_win):
        self.name = name
        self.name_team = name_team 
        self.role = role 
        self.kills = kills 
        self.assists = assists 
        self.deads = deads 
        self.m_played = m_played 
        self.m_win = m_win 

    def __repr__(self):
        return 'Proplayer {0}'.format(self.id)
