import flask
from infrastructure.view_modifiers import response

app = flask.Flask(__name__)

#function that gets latest pacakges
def get_latest_packages():
    return [
        { 'name': 'flask', 'version' : '1.2.3' },
        { 'name': 'sqlalchemy', 'version' : '2.2.0' },
        { 'name': 'passlib', 'version' : '3.0.0'}
    ]

@app.route('/')
@response(template_file='home/index.html')
def index():
    test_packages =  get_latest_packages()
    return  { 'packages' : test_packages }
    # return flask.render_template("/home/index.html", packages=test_packages)

@app.route('/about')
@response(template_file='home/about.html')
def about():
    #test_packages =  get_latest_packages()
    return {}
    #return flask.render_template("/home/about.html")

if __name__ == "__main__":
    app.run(debug = True)