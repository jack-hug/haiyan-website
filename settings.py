import os

from unice import app


dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path),'data.db')

SECRET_KEY = os.getenv('SECRET_KEY','Unice precision')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', dev_db)