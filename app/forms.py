"""Forms module."""

from flask_wtf import Form
from wtforms import TextField, IntegerField
from wtforms.validators import Required, NumberRange

class AddForm(Form):
    """
    Class to determine the form fields.
    """

    name = TextField('name', validators = [Required()])
    author = TextField('author', validators = [Required()])
    pages = IntegerField('pages', validators = [NumberRange()])