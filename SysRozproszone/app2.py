from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    return render_template('index.html', active_page='index')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        with app.app_context():
            user = User(name=name, email=email)
            db.session.add(user)
            db.session.commit()
    return render_template('form.html', active_page='form')

@app.route('/media')
def media():
    return render_template('media.html', active_page='media')

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users, active_page='users')

# utworzenie tabeli w bazie danych
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
