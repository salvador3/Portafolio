from flask import Flask
from .home_endpoint import api_home

from flask_cors import CORS , cross_origin

from flask_swagger_ui import get_swaggerui_blueprint

# from config import DATA_ENVORIMENT

def crear_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(api_home)
    
    
    API_URL= "/static/swagger.json"

        
    SWAGGER_URL= '/swagger'

    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "API "
        }
    )

    app.register_blueprint(SWAGGER_BLUEPRINT)

    return app