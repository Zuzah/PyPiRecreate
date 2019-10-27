import flask
from infrastructure.view_modifiers import response

#create a blueprint object to encapsulate all routes logics in this view
blueprint = flask.Blueprint('account', __name__, template_folder='templates')

# TODO: in app.py, register the above Blueprint to render the page

# ####################### INDEX ############################

@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    return {}

# ####################### REGISTER #########################

@blueprint.route('account/register', method= ['GET'])
@response(template_file = 'account/register.html')
def register_get():
    return {}


@blueprint.route('account/register', method= ['POST'])
@response(template_file = 'account/register.html')
def register_post():
    return {}


# ####################### LOGIN #########################

@blueprint.route('account/login', method= ['GET'])
@response(template_file = 'account/login.html')
def login_get():
    return {}

@blueprint.route('account/login', method= ['POST'])
@response(template_file = 'account/login.html')
def login_post():
    return {}
