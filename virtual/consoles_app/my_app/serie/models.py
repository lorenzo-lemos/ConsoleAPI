from my_app import db

class Serie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    genre = db.Column(db.String(100))
    season = db.Column(db.Integer)
    average = db.Column(db.Integer)
    isActive = db.Column(db.String(100))

    def __init__(self,name,genre,season,average,isActive):
        self.name = name
        self.genre = genre
        self.season = season
        self.average = average
        self.isActive = isActive

    def __repr__(self):
        return 'Serie {0}'.format(self.id)
