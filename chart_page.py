from flask import Blueprint,render_template, flash, request, jsonify,redirect,url_for
from database import User, db
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash
from constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
import random
import time
from database import Battery, db
import datetime


chart_page = Blueprint("chart_page", __name__)

@chart_page.route('/<username>/chartpage')
def user_chartpage(username):

    print(username)
    data = [
        ("01-01-2020", 1597),
        ("02-01-2020", 1456),
        ("03-01-2020", 1908),
        ("04-01-2020", 896),
        ("05-01-2020", 755),
        ("06-01-2020", 453),
        ("07-01-2020", 1100),
        ("08-01-2020", 1235),
        ("09-01-2020",1478),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    # print(dir(User))

    soh_list = []
    soc_list = []
    current_list = []
    date_list = []

    user = User.query.filter_by(username=username).first()
    user_id = user.id

    battery = Battery.query.all()
    for bat in battery:
        if bat.user_id == user_id:
            soh_list.append(bat.SOH)
            soc_list.append(bat.SOC)
            current_list.append(bat.current)
            t = bat.created_at
            converted = t.strftime("%m/%d/%Y, %H:%M:%S")
            date_list.append(converted)


    print("CHART PAGE DATA")
    soh_list_f = soh_list[-20:]
    soc_list_f = soc_list[-20:]
    current_list_f = current_list[-20:]
    date_list_f = date_list[-20:]

    def Reverse(lst):
        new_lst = lst[::-1]
        return new_lst
    soh_list_r = Reverse(soh_list_f)
    soc_list_r = Reverse(soc_list_f)
    current_list_r = Reverse(current_list_f)
    date_list_r = Reverse(date_list_f)

    print(soh_list_r)
    print(soc_list_r)
    print(current_list_r)
    print(date_list_r)
    return render_template('chart.html',
    username=username,
    labels=labels,
    values=values,
    dates=date_list_r,
    soh_list=soh_list_r,
    soc_list=soc_list_r,
    current_list=current_list_r
    )

@chart_page.route("/<username>/chartdirect", methods=['POST'])
def goto_chartpage(username):
    print("directing", username)
    return redirect(url_for("chart_page.user_chartpage", username=username ))