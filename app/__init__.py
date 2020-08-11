import os

from flask import Flask
from .settings import config
from .extensions import bootstrap,db,moment
from .blueprints.auth import auth
from .blueprints.admin import admin
from .blueprints.main import main


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
    pass

def register_errors(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

def register_commands(app):
    pass

def register_shell_context(app):
    pass



