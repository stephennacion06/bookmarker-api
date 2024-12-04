from flask import Blueprint,render_template, flash, request, jsonify,redirect,url_for
from database import User, db
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash
from constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
import random
import time
from database import Battery, db
from datetime import datetime



settings_page = Blueprint("settings_page", __name__)

@settings_page.route('/<username>/settings_update', methods=['POST'])
def settings_update_database(username):
    if request.method == 'POST':
        current_user = User.query.filter_by(username=username).first()

        current_user.battery_model = request.form["brand_forms"]
        current_user.battery_capacity = request.form["capacity_forms"]
        current_user.battery_voltage  = request.form["volts_forms"]
        current_user.battery_type  = request.form["type_forms"]
        db.session.commit()

        client_id = current_user.id
        battery = Battery.query.filter_by(user_id=client_id).order_by(Battery.id.desc()).first()

        batteries = Battery(user_id=client_id,
                voltage=0,
                current=0,
                SOC= 0,
                SOH= 0,
                internal_resistance=0,
                DOD= 0,
                number_of_cycle = 0,
                created_at = datetime.now()
                )
        db.session.add(batteries)
        db.session.commit()

        return render_template('settings.html', username=username,
                                                battery_model = request.form["brand_forms"],
                                                battery_capacity = request.form["capacity_forms"],
                                                battery_voltage = request.form["volts_forms"],
                                                battery_type = request.form["type_forms"]
        )




@settings_page.route('/<username>/settingspage')
def user_settingspage(username):

    current_user = User.query.filter_by(username=username).first()

    batery_model = current_user.battery_model
    battery_capacity = current_user.battery_capacity
    battery_voltage = current_user.battery_voltage
    battery_type = current_user.battery_type



    return render_template('settings.html', username=username,
                                            battery_model = batery_model,
                                            battery_capacity = battery_capacity,
                                            battery_voltage = battery_voltage,
                                            battery_type = battery_type
    )


    return render_template('settings.html', username=username)

@settings_page.route("/<username>/settingsdirect", methods=['POST'])
def goto_settingspage(username):

    return redirect(url_for("settings_page.user_settingspage", username=username ))