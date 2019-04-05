from wtforms import Form
from wtforms import StringField, TextField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class ContactForm(Form):
    fullname = StringField('Fullname',
    [
        validators.Required(message = 'El nombre completo es requerido'),
        validators.length(min = 20, max=200, message = 'Ingrese el fullname válido')
    ]
    , render_kw = {
        "placeholder": "Fullname"
    })
    phone = StringField('Phone',
    [
        validators.Required(message = 'El número telefónico es requerido')
    ]
    ,render_kw = {
        "placeholder": "Phone"
    } )
    email = EmailField('Email',
    [
        validators.Required(message = 'El número telefónico es requerido'),
        validators.email(message = 'Escriba un email válido')
    ]
    , render_kw = {
        "placeholder": "Email"
    })
