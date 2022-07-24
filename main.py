########################################################################################
######################          Import packages      ###################################
########################################################################################
import re
from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import create_app, db
from models import Drugs, User

########################################################################################
# our main blueprint
main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.name,registration_type=current_user.registration_type)

@main.route('/hospital') # profile page that return 'hospital'
@login_required
def hospital():
    all_hospitals_data = list(enumerate(User.query.filter_by(registration_type="Hospital").all(),start=1))
    return render_template('hospital.html', name=current_user.name,all_hospitals_data=all_hospitals_data)

@main.route('/patient',methods=['GET', 'POST']) # profile page that return 'patient'
@login_required
def patient():
    if request.method=='GET':
        all_patient_data = enumerate(User.query.filter_by(registration_type="Patient").all(),start=1)
        return render_template('patient.html', name=current_user.name,all_patient_data=all_patient_data)
    else:
        patient_name = request.form.get('patient_name')
        patient_email = request.form.get('patient_email')
        new_user = User(email=patient_email, name=patient_name, password=generate_password_hash("password", method='sha256'), registration_type="Patient")
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.patient'))

@main.route('/syncup',methods=['GET','POST'])
@login_required
def syncup():
    if request.method=='GET':
        return render_template('syncup.html',name=current_user.name)
    else:
        flash('Syncing up data ...')
        return redirect(url_for('main.syncup'))

@main.route('/images',methods=['GET','POST'])
@login_required
def images():
    if request.method=='GET':
        from datetime import date
        sampleDates = [date(2022, 7, 23),date(2022, 7, 22),date(2022, 7, 21)]
        return render_template('images.html',name=current_user.name, sampleDates=sampleDates)
    else:
        return redirect(url_for('main.images'))

@main.route('/calldoc',methods=['GET','POST'])
@login_required
def calldoc():
    return render_template('calldoc.html')

@main.route('/drugs',methods=['GET', 'POST'])
@login_required
def drugs():
    drug_names = enumerate(Drugs.query.all(),start=1)
    if request.method=='GET':
        return render_template('drugs.html',name=current_user.name,drug_names=drug_names)
    else:
        drug_name = request.form.get('drug_name')
        drug_context = request.form.get('drug_context')
        drug_indication = request.form.get('drug_indication')
        new_drug = Drugs(drug_name=drug_name,drug_details=drug_context,drug_indication=drug_indication)
        db.session.add(new_drug)
        db.session.commit()
        return redirect(url_for('main.drugs'))

@main.route('/patientprofile',methods=['GET', 'POST'])
@login_required
def patientprofile():
    email = request.args.get('email')
    patient = User.query.filter_by(email=email).first() 
    return render_template('patientprofile.html', name=current_user.name, patient=patient)

@main.route('/drugdetail',methods=['GET', 'POST'])
@login_required
def drugdetail():
    drug_name = request.args.get('drug')
    drug = Drugs.query.filter_by(drug_name=drug_name).first()
    return render_template('drugdetail.html', drug=drug)

@main.route('/scan',methods=['GET', 'POST'])
@login_required
def scan():
    return render_template('scan.html',name=current_user)

app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode