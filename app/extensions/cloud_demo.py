import os
import shutil


def deploy_database():
    if os.getenv('GAE_ENV') == 'standard' or os.getenv('RENDER') == 'true':
        os.makedirs('/tmp/app/storage', exist_ok=True)

        with open('/tmp/app/storage/Readme.txt', 'w') as file:
            file.write('This is a storage directory for app.')

        demo_db_path = os.getenv('DEMO_DB_SQLITE', 'demo/app.db')
        shutil.copyfile(demo_db_path, '/tmp/app/app.db')
