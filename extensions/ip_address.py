from flask import Flask, request


def init_app(app: Flask) -> None:
    @app.context_processor
    def client_ip_address() -> dict:
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        return dict(client_ip=ip)
