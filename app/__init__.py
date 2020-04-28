from flask import Flask
# from .config import DevConfig 
from flask_bootstrap import Bootstrap
# from flask_wtf.csrf import CSRFProtect
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)


    return app










# # Initializing application
# app = Flask(__name__,instance_relative_config = True)


# # Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')
# app.config['SECRET_KEY'] = "secretkey"
# app.config['WTF_CSRF_SECRET_KEY'] = "secretkey"
# csrf = CSRFProtect(app)

# # Initializing Flask Extensions
# bootstrap = Bootstrap(app)

# from app import views
# from app import error