from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db
from models import Contact

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://multi_cesar:12345@localhost/flaskcontacts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def index():
    #return render_template('index.html')
    return render_template('index.html')
@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        
        return 'received'
@app.route('/edit')
def edit_contact():
    return 'edit contact'
@app.route('/delete')
def delete_contact():
    return 'delete contact'
if __name__ == '__main__':
  db.init_app(app)
  with app.app_context():
      db.create_all()
  app.run(port=3000, debug=True)
