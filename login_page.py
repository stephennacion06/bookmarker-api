from flask import Blueprint,render_template, flash, request, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect
from database import User, db
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash
from constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
from dashboard_page import dashboard_page
login_page = Blueprint("login_page", __name__)

@login_page.route('/')
def index():
    return render_template('login.html')

@login_page.route('/login_post', methods=['POST'])
def login_post():
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    user = User.query.filter_by(username=username).first()
    print("Entered login_post")
    if user:
        is_pass_correct = check_password_hash(user.password, password)

        if is_pass_correct:
            refresh = create_refresh_token(identity=user.id)
            access = create_access_token(identity=user.id)

            # return jsonify({
            #     'user': {
            #         'refresh': refresh,
            #         'access': access,
            #         'username': user.username,
            #         'email': user.email,
            #         'user_number': user.user_number,
            #         'device_number': user.device_number
            #     }

            # }), HTTP_200_OK
            print("entered login_post 2")
            return redirect(url_for("dashboard_page.user_dashboard", username=username ))

    return "LOGIN FAILED"
    
    
