import os

from app import db,create_app
from app.models import Message,Admin,Category,Photo,Injection_Mold_Category
from flask_script import Manager,Shell


app = create_app(os.getenv('FLASK_CONFIG') or 'development')
manager = Manager(app)

def make_shell_context():
    return dict(db=db,app = app,message = Message,admin = Admin,category = Category,photo = Photo,injection_categories = Injection_Mold_Category)

manager.add_command('shell',Shell(make_context=make_shell_context))

if __name__ == "__main__":
    manager.run()