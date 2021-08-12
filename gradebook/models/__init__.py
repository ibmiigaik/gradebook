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

    @staticmethod
    def create_mock_users():

        users=[
            User(
                username=f"Student0",
                password=generate_password_hash(f"Student0password"),
                first_name = f"studentfirstname",
                last_name = f"studentlastname",
                patronymic = f"studentpatronymic",
                addmission_year =f"2020",
                direction = f"ИБ",
                group_num = f"1",
                role="student"
            )
        ]

        users.append(
            User(
                username=f"Teacher0",
                password=generate_password_hash(f"Teacher0password"),
                first_name = f"teacherfirstname",
                last_name = f"teacherlastname",
                patronymic = f"teacherpatronymic",
                addmission_year =f"2020",
                direction = f"ИБ",
                group_num = f"1",
                role="teacher"
            )
        )

        users.append(
            User(
                username=f"Secretary0",
                password=generate_password_hash(f"Secretary0password"),
                first_name = f"secretaryfirstname",
                last_name = f"secretarylastname",
                patronymic = f"secretarypatronymic",
                addmission_year =f"2020",
                direction = f"ИБ",
                group_num = f"1",
                role="secretary"
            )
        )

        for user in users:
            user.save()
