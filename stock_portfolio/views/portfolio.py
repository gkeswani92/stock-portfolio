from flask import Blueprint
from flask import render_template


# Defining a blue print for all URLs that begin with /portfolio.
# All views that are related to portfolio should be registered with
# this blueprint and this blueprint will in turn be registred
# with the flask application
portfolio_bp = Blueprint('portfolio_bp', __name__, url_prefix='/portfolio')


@portfolio_bp.route('/')
def index():
    return render_template('portfolio/home.html')
