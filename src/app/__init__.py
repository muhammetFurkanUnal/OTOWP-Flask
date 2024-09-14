from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    CORS(app)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:@localhost/otowpdb"
    db.init_app(app)
    
    
    # import blueprints
    from .controllers import mainpageBP, editpageBP
    
    # register blueprints
    app.register_blueprint(mainpageBP)
    app.register_blueprint(editpageBP)
    
    
    return app
