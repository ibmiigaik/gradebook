from flask import Flask
from flask_session import Session


def create_app(config="gradebook.config.Config"):
    app = Flask(__name__)

    with app.app_context():
        app.config.from_object(config)

        from gradebook.models import db, User
        sess = Session()

        db.init_app(app)
        sess.init_app(app)

        from gradebook.utils.initialization import init_template_globals

        init_template_globals(app)

        if app.config.get("DEBUG"):
            User.create_mock_users()

        from gradebook.auth import auth

        app.register_blueprint(auth)

        return app
