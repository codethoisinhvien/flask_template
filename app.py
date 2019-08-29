from flask import Flask
from peewee import *
from flask_cors import CORS
from src.apis.api_v1.user_api import user
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'

CORS(app)


@app.before_first_request
def before_first_request():
    pass

app.register_blueprint(user, url_prefix='/api/v1')

app.run(debug=True)
# http://127.0.0.1:5000/api/v1/test