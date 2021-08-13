from flask_mongoengine import MongoEngine

from werkzeug.security import generate_password_hash


db = MongoEngine()

class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)
    first_name = db.StringField()
    last_name = db.StringField()
    patronymic = db.StringField()
    addmission_year = db.StringField()
    direction = db.StringField()
    group_num = db.StringField()


    role = db.StringField(required=True)
