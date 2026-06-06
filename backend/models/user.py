from app import db

class User(db.Model):
    _tablename_= "users"

    id = db.Colimn(db.Integer, primary_key=True)

    username = db.Column(db.String(80, nullable=False))

    email = db.Column(db.String(120),uniqe=True, nullable=False)

    password = db.Column(db.String(225),nullable=False)