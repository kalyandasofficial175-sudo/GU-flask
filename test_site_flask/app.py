import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from forms import TestForm  # Assuming your form is in forms.py

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)


class UserRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    religion = db.Column(db.String(20))
    birthdate = db.Column(db.Date)
    profile_pic = db.Column(db.String(200)) # Stores the filename

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def form_view():
    form = TestForm()
    if form.validate_on_submit():
        
        file = form.profile_pic.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_record = UserRecord(
            name=form.name.data,
            email=form.email.data,
            age=form.age.data,
            gender=form.gender.data,
            religion=form.religion.data,
            birthdate=form.birthdate.data,
            profile_pic=filename
        )
        db.session.add(new_record)
        db.session.commit()
        
       
        all_users = UserRecord.query.all()
        return render_template('success.html', users=all_users)
        
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)


    import os


