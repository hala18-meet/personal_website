from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

#from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'


#heroku = Heroku(app)
db = SQLAlchemy(app)

 
class potato(db.Model):
    __tablename__ = "potato"
    first_name = db.Column('first_name', db.Unicode)
    last_name = db.Column('last_name', db.Unicode)

db.create_all()




@app.route('/submit_form', methods=['POST'])
def submit_form():

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

