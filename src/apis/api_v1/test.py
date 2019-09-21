from flask import Blueprint,jsonify
from flask_jwt import  jwt_required
import urllib.request

from flask import request
from  src.models.user import User
from src.commons.auth import create_token,token_required
from src.commons.file import allowed_file,secure_filename,save_file_in_local
import  datetime
test= Blueprint(__name__,__name__)
@test.route('/test',methods=['GET'])
@jwt_required()
def test_api():
    return jsonify({'success':True})

@test.route('/test/query',methods=['GET'])
@token_required
def get_query():
    return  request.args
@test.route('/test/query',methods=['POST'])
def post():
    return request.json
@test.route('/test/create')
def create():
    user = User(username="giang", password="13081999")
    user.save()
    return "true"
@test.route('/test/token')
def token():
    return create_token({'username':"giang","password":"13081999","exp":datetime.datetime.utcnow()})

@test.route('/test/upload' ,methods=['POST'])
def upload():
    print("sfsdfd")
    print(request.files)
    if 'file' not in request.files:
        return "erro1"
    file = request.files['file']
    if file.filename == '':
        return "erro2"

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        re=save_file_in_local(file,filename)
        return {"success":re}
    return "False"



