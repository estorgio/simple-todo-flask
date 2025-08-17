from flask import Flask, request


class MethodOverrideMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if environ['REQUEST_METHOD'] == 'POST':
            from urllib.parse import parse_qs, urlencode
            from io import BytesIO

            try:
                length = int(environ.get('CONTENT_LENGTH', 0))
                body = environ['wsgi.input'].read(length)
                params = parse_qs(body.decode())

                override = params.pop('_method', [None])[0]
                if override and override.upper() in ('PUT', 'PATCH', 'DELETE'):
                    environ['REQUEST_METHOD'] = override.upper()

                # Re-encode params *without* _method
                new_body = urlencode(params, doseq=True).encode()

                # Update CONTENT_LENGTH
                environ['CONTENT_LENGTH'] = str(len(new_body))

                # Replace wsgi.input so Flask can read the cleaned form data
                environ['wsgi.input'] = BytesIO(new_body)

            except Exception:
                # optionally log the error
                pass

        return self.app(environ, start_response)


def init_app(app: Flask):
    app.wsgi_app = MethodOverrideMiddleware(app.wsgi_app)  # type: ignore
