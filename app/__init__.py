from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_super_secret_key'
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
    app.config['OUTPUT_FOLDER'] = os.path.join(os.getcwd(), 'outputs')

    from .routes import main
    app.register_blueprint(main)

    return app
