from flask import Blueprint
from flask import render_template


# Defining a blue print for all URLs that begin with /.
# All views that are related to portfolio should be registered with
# this blueprint and this blueprint will in turn be registred
# with the flask application
index_bp = Blueprint('index_bp', __name__, url_prefix='/')

PAGINATION_SIZE = 10


@index_bp.route('/')
def index():
    # Render a jinja template by passing in variables and returning HTML
    # to the caller of this API
    # The path we are passing into render template is just considered to be
    # a text file with placeholders. After the placeholders are filled in,
    # we will render the HTML and then return it to the caller
    return render_template(
        'index.html',
        message='Test message from the backend',
    )
