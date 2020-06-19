import os
import tempfile
from flask import Flask
import sass
from sassutils.wsgi import SassMiddleware


from python_flask_example.db import get_db
from python_flask_example.db import init_db

# read in SQL for populating test data
with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")


def create_app(test_config=None, extra_config_settings={}):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "python_flask_example.sqlite"),
    )

    # 'strip_extension': False,
    app.wsgi_app = SassMiddleware(app.wsgi_app, {
        'python_flask_example': {
            'sass_path': 'static/sass',
            'css_path': 'static/css',
            'wsgi_path': 'static/css',
            'strip_extension': False,
        }
    })

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # register the database commands
    from python_flask_example import db

    db.init_app(app)

    # apply the blueprints to the app
    from python_flask_example import auth, blog

    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app


def app():
    application = create_app()
    with application.app_context():
        init_db()
        #get_db()
        get_db().executescript(_data_sql)
    return application
