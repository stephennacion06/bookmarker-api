from flask import Blueprint,render_template, flash, request, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect
from database import User, db
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash
from constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
from dashboard_page import dashboard_page


url_page = Blueprint("url_page", __name__, url_prefix="/api")

@url_page.route('/api_post')
def post_route():
    

  user = request.args.get('user', default = 1, type = int)
  field1 = request.args.get('field1', default = 0, type = str)
  field2 = request.args.get('field2', default = 0, type = str)
  print(user)
  print(field1)
  print(field2)
  return jsonify({'user': user, 
                  "field1": field1,
                  "field2": field2})


@url_page.route('/')
def api_home():
    return jsonify({"h": "hasd"})