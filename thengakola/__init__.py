import os
from flask import Flask, redirect, url_for


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=open("/home/ngj14/thengakola-2.0/secret.txt").read()
    )
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from thengakola import db

    db.init_app(app)

    from thengakola import auth

    app.register_blueprint(auth.bp)

    from thengakola import views

    app.register_blueprint(views.bp)

    return app


app = create_app()
