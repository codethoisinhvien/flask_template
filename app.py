from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT, jwt_required, current_identity
from src.apis.api_v1.test import test
from src.commons.auth import authenticate,identity
from src.models import create_database
from werkzeug.utils import secure_filename
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
CORS(app)

jwt = JWT(app,authenticate,identity)
@app.before_first_request
def before_first_request():
    create_database()
app.register_blueprint(test, url_prefix='/api/v1')

app.run(debug=True)
