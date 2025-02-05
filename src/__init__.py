from flask import Flask, redirect, url_for
import os
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from src.auth import auth
from src.battery import batteries
from src.login_page import login_page
from src.dashboard_page import dashboard_page
from src.database import db, Battery
from flask_jwt_extended import JWTManager
from src.constants.http_status_codes import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR


def create_app(test_config=None):
    app = Flask(__name__,
                instance_relative_config=True)
    
    if test_config is None:
        print("HELLO CHECK THIS ",os.environ.get("SQLALCHEMY_DB_URI"))
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI="sqlite:///database.db",
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY'),
        )
    else:
        app.config.from_mapping(test_config)
    db.app=app
    db.init_app(app)
    
    JWTManager(app)
    
    app.register_blueprint(login_page)
    app.register_blueprint(dashboard_page)
    app.register_blueprint(auth)
    app.register_blueprint(batteries)
    
    
    
    @app.errorhandler(HTTP_404_NOT_FOUND)
    def handle_404(e):
        return jsonify({'error': 'Not found'}), HTTP_404_NOT_FOUND

    @app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
    def handle_500(e):
        return jsonify({'error': 'Something went wrong, we are working on it'}), HTTP_500_INTERNAL_SERVER_ERROR

    
    
    return app 