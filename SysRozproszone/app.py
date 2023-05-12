# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
# db = SQLAlchemy(app)
# db.create_all()
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
# # utworzenie tabeli w bazie danych
# with app.app_context():
#     db.create_all()
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         user = User(name=name, email=email)
#         db.session.add(user)
#         db.session.commit()
#         return 'Thank you for submitting the form!'
#     return render_template('form.html')
#
# @app.route('/media')
# def media():
#     return render_template('media.html')
#
# if __name__ == '__main__':
#     app.run(debug=True)
