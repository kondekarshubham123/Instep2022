########################################################################################
######################          Import packages      ###################################
########################################################################################
from crypt import methods
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
    all_hospitals_data = enumerate(User.query.filter_by(registration_type="Hospital").all(),start=1)
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
        return render_template('images.html',name=current_user.name)
    else:
        return redirect(url_for('main.images'))



@main.route('/drugs',methods=['GET', 'POST'])
@login_required
def drugs():
    drug_names = Drugs.query.all()
    if request.method=='GET':
        return render_template('drugs.html',name=current_user.name,drug_names=drug_names)
    else:
        drug_name = request.form.get('drug_name')
        drug_context = request.form.get('drug_context')
        new_drug = Drugs(drug_name=drug_name,drug_details=drug_context)
        db.session.add(new_drug)
        db.session.commit()
        return redirect(url_for('main.drugs'))

@main.route('/patientprofile',methods=['GET', 'POST'])
@login_required
def patientprofile():
    return render_template('patientprofile.html', nume=current_user.name)

app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode