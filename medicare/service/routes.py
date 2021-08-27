from medicare.main.routes import service
from flask import render_template, url_for, flash, redirect, request, Blueprint
from medicare.service.forms import Cancer
from medicare import db
service = Blueprint('service', __name__)
@service.route("/breastcancer")
def breastcancer():
    form=Cancer()

 
    return render_template('breastcancer.html',title='breastcancer',form=form)
