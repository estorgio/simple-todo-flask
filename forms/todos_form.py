from flask_wtf import FlaskForm  # type: ignore
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Length
from extensions.flash_form import FlashingForm


class TodosForm(FlashingForm):
    text = TextAreaField('Text', validators=[
        DataRequired(), Length(1, 512)])
