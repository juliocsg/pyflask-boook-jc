from flask import Flask, render_template, request, url_for, redirect, flash, g
from flask_sqlalchemy import SQLAlchemy
from models import db
from models import Contact
from forms import ContactForm
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://multi_cesar:12345@localhost/flaskcontacts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "MY_secret_key"
@app.route('/')
def index():
    #return render_template('index.html')
    #contact = Contact.query.filter_by(fullname = 'julio')
    #contact = Contact.query.filter_by(fullname = 'julio').first()
    #Lista todos los datos
    contacts = Contact.query.all()
    #print(contact.id[1])
    return render_template('index.html', form = ContactForm(), contacts = contacts)
@app.route('/add_contact', methods=['POST'])
def add_contact():
    contact_form = ContactForm(request.form)
    if request.method == 'POST':
        fullname = contact_form.fullname.data
        phone = contact_form.phone.data
        email = contact_form.email.data
        contact = Contact(fullname = fullname, phone = phone, email = email)
        db.session.add(contact)
        db.session.commit()
        flash('Contact Added Successfully!')
        #return render_template('add_contact.html', form = ContactForm(), message = 'received!')
        return redirect(url_for('index'))
        #return 'received'
@app.route('/edit/<string:id>', methods=['GET', 'POST'])
def get_contact(id):
    contact_form = ContactForm()
    contact = Contact.query.filter_by(id = id).first()
    contact_form.fullname.data = contact.fullname
    contact_form.phone.data = contact.phone
    contact_form.email.data = contact.email
    #contact_form.get(contact.id)
    return render_template('edit_contact.html',contact=contact, form = contact_form)
@app.route('/delete/<string:id>')
def delete_contact(id):
    #Guarda en un objeto la consulta para la obtención del id
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact removed successfully!')
    return redirect(url_for('index'))
    #return id

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    contact_form = ContactForm(request.form)
    contact = Contact.query.get(id)
    contact.fullname = contact_form.fullname.data
    contact.phone = contact_form.phone.data
    contact.email = contact_form.email.data
    db.session.commit()
    flash('Contact Updated Successfully!')
    return redirect(url_for('index'))
    #return render_template('edit_contact.html')
if __name__ == '__main__':
  db.init_app(app)
  with app.app_context():
      db.create_all()
  app.run(port=3000, debug=True)
