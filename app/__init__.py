import os,click

from flask import Flask,render_template
from .settings import config
from .extensions import bootstrap,db,moment
from .blueprints.auth import auth
from .blueprints.admin import admin
from .blueprints.main import main
from .models import Message,Admin,Injection_Mold_Category


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_logging(app) # 注册日志处理器
    register_extensions(app) # 初始化扩展 
    register_blueprint(app) # 注册蓝本
    register_commands(app) # 注册自定义shell命令
    register_errors(app) # 注册错误处理函数
    register_shell_context(app) # 注册shell上下文处理函数
    register_template_context(app) # 注册模板上下文处理函数

    return app

def register_blueprint(app):
    app.register_blueprint(main)
    app.register_blueprint(admin, url_prefix = '/admin')
    app.register_blueprint(auth, url_prefix ='/auth')

def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)

def register_logging(app):
    pass

def register_template_context(app):
    @app.context_processor
    def mak_template_context():
        admin = Admin.query.first()
        injection_categories = Injection_Mold_Category.query.order_by(Injection_Mold_Category.id).all()
        return dict(admin = admin, injection_categories = injection_categories)

def register_errors(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

def register_commands(app):
    @app.cli.command()
    @click.option('--count', default = 20, help = 'Quantity of messages, default is 20...')
    def forge(count):
        """Generate fake messages"""
        from faker import Faker
        db.drop_all()
        db.create_all()

        faker = Faker()
        click.echo('Working...')

        for i in range(count):
            message = Message(
                name = faker.name(),
                body = faker.sentence(),
                email = faker.email(),
                timestamp = faker.date_time_this_year()
            )
            db.session.add(message)

        db.session.commit()
        click.echo('Create %d fake messages...' % count)

def register_shell_context(app):
    pass



