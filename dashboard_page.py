from flask import Blueprint,render_template, flash, request, jsonify, redirect, url_for
from database import User, db
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash
from constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
import random
import time
from database import Battery, db


dashboard_page = Blueprint("dashboard_page", __name__)


def get_health(soh):
    battery_health = "Excellent"
    if 95 < float(soh) <= 100:
        battery_health = "Excellent"
    elif 90 < float(soh) <= 95:
        battery_health = "Good"
    elif 85 < float(soh) <= 90:
        battery_health = "Regular"
    elif 80 < float(soh) <= 85:
        battery_health = "Bad"
    elif float(soh) <= 80:
        battery_health = "Very Bad"
    return battery_health

@dashboard_page.route('/<username>/dashboard/data', methods = ['GET'])
def stuff(username):
    user = User.query.filter_by(username=username).first()
    user_id = user.id

    battery = Battery.query.filter_by(user_id=user_id).order_by(Battery.id.desc()).first()
    current_user = User.query.filter_by(username=username).first()

    battery_health = get_health(battery.SOH)

    if battery.voltage == 0:
        battery_health = "-"

    print("BATTERY HEALTH!", battery_health)


    return jsonify(result=battery.voltage,
    result2=battery.current,
    result3=battery.SOH,
    result4=battery.SOC,
    result5=battery.internal_resistance,
    result6=current_user.battery_capacity,
    result7=battery.DOD,
    result8=current_user.battery_model,
    result9=current_user.battery_voltage,
    result10=battery.number_of_cycle,
    result11=battery_health,
    )


@dashboard_page.route('/<username>/dashboarddirect', methods = ['POST'])
def goto_dashboard(username):
    print("Redirecting to homepage user:", username)
    return redirect(url_for("dashboard_page.user_dashboard", username=username ))

@dashboard_page.route('/<username>')
def user_dashboard(username):
    print("Visited homepage user:", username)
    return render_template('dashboard.html', username=username)



