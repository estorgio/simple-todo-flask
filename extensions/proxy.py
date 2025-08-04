import os
from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix


def init_app(app: Flask) -> None:
    proxy_count = int(os.getenv('PROXY_COUNT', 0))
    if proxy_count >= 1:
        app.wsgi_app = ProxyFix(  # type:ignore
            app.wsgi_app,
            x_for=proxy_count,
            x_proto=proxy_count,
            x_host=proxy_count,
            x_prefix=proxy_count
        )

    @app.context_processor
    def client_ip_address() -> dict:
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        if ip and ',' in ip:
            ip = ip.split(',')[0].strip()
        return dict(client_ip=ip)
