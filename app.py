from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

#from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'


#heroku = Heroku(app)
db = SQLAlchemy(app)

 
class Donate(db.Model):
    __tablename__ = "donate"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.Unicode)
    last_name = db.Column('last_name', db.Unicode)
    type_of_pet=db.Column('type_of_pet', db.Unicode)
    age_of_pet=db.Column('age_of_pet', db.Unicode)
    image_of_pet=db.Column('image_of_pet', db.Unicode)
    phone_number=db.Column('phone_number', db.Unicode)

    # def __init__
db.create_all()





@app.route('/submit_form', methods=['POST'])
def submit_form():
    username1 = request.form["fname"]
    username2 = request.form["lname"]
    username3 = request.form["tname"]
    username4 = request.form["aname"]
    username5 = request.form["iname"] 
    username6 = request.form["pname"] 
    
    donate1=Donate(first_name=username1, last_name=username2, type_of_pet=username3, age_of_pet=username4, image_of_pet=username5, phone_number=username6)
    
    db.session.add(donate1)
    db.session.commit()

    users = Donate.query.all()
    return render_template('adopt.html', var=users)



# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')
@app.route('/adopt')
def adopt():
    return render_template('adopt.html')



# Save e-mail to database and send to success page
@app.route('/prereg', methods=['POST'])
def prereg():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')

if __name__ == '__main__':
    #app.debug = True
    app.run()