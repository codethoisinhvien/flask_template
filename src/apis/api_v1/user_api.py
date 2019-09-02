from flask import Blueprint,jsonify,request
from flask_jwt import  jwt_required

user= Blueprint(__name__,__name__)

@user.route('/test',methods=['GET'])
@jwt_required()
def test_api():
    return jsonify({'success':True})
