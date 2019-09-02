from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT, jwt_required, current_identity
from src.apis.api_v1.user_api import user
from src.commons.auth import authenticate,identity
import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
CORS(app)

jwt = JWT(app,authenticate,identity)
@app.before_first_request
def before_first_request():
    pass

app.register_blueprint(user, url_prefix='/api/v1')

app.run(debug=True)
