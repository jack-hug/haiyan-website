from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
# from . import settings

app = Flask(__name__)

# app.config.from_object('settings')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

from . import views,errors


