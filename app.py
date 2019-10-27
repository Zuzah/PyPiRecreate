import flask

app = flask.Flask(__name__)

def register_blueprints():
    from templates.views import home_views
    from templates.views import package_views
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)

def main():
    register_blueprints()
    app.run(debug = True)

if __name__ == "__main__":
    main()