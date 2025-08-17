from flask_wtf import FlaskForm  # type: ignore
from flask import flash
from flask import Flask, get_flashed_messages
import json


class FlashingForm(FlaskForm):
    def validate(self, extra_validators=None):
        # Call original validate() method
        success = super().validate(extra_validators)
        if not success:
            # Flash each error
            error_list = []
            for field_name, errors in self.errors.items():
                name = getattr(self, field_name).name
                label = getattr(self, field_name).label.text
                for error in errors:
                    # 'error' is optional category
                    error_list.append({
                        'name': name,
                        'label': label,
                        'error': error,
                    })

            if error_list:
                flash(json.dumps(error_list), 'error')
        return success


def init_app(app: Flask) -> None:
    @app.context_processor
    def flash_form_processors():
        def form_errors(use_tuple=True):
            messages = get_flashed_messages(category_filter=['error'])
            if messages:
                message_json = messages.pop()
                errors = json.loads(message_json)
                if use_tuple:
                    errors = tuple(
                        (each_error['name'],
                         each_error['label'],
                         each_error['error']) for each_error in errors)
                return errors
            else:
                return []
        return dict(form_errors=form_errors)
