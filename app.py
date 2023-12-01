from flask import Flask
from flask_smorest import Api

from data_access.db import close_db, get_db, init_db
from resources.post import blp as postBlueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    api = Api(app)
    api.register_blueprint(postBlueprint)

    @app.before_request
    def before_request():                
        get_db(app)
        
    @app.teardown_request
    def teardown_request(exception):
        close_db(exception)        
        
    # Initialize the database schema
    with app.app_context():
        init_db(app)        
        
    return app