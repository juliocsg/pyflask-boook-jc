from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    email = db.Column(db.String(255))

'''
id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True)
    email = db.Column(db.String(40))
    #crearía un hash de 66 caracteres
    password = db.Column(db.String(150))
    create_date = db.Column(db.DateTime, default = datetime.datetime.now)
'''
