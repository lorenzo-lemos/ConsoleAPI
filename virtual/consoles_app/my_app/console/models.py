from my_app import db

class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    year = db.Column(db.Integer)
    price = db.Column(db.Float(asdecimal=True))
    active_sale = db.Column(db.String(10))
    amount_games = db.Column(db.Integer)


    def __init__(self,name,year,price,active_sale,amount_games):
        self.name = name
        self.year = year
        self.price = price
        self.active_sale = active_sale
        self.amount_games = amount_games

    def __repr__(self):
        return 'Console {0}'.format(self.id)
