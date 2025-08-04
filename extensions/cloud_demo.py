import os
import shutil


def deploy_database():
    if os.getenv('GAE_ENV') == 'standard' or os.getenv('RENDER') == 'true':
        os.makedirs('/tmp/app/storage', exist_ok=True)

        with open('/tmp/app/storage/Readme.txt', 'w') as file:
            file.write('This is a storage directory for app.')

        shutil.copyfile('demo/app.db', '/tmp/app/app.db')
