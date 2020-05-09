from typing import Set

from flask import abort
from flask import Blueprint
from flask import render_template

SUPPORTED_PROVIDERS: Set[str] = {
    'Fidelity',
    'Robinhood',
}

# Defining a blue print for all URLs that begin with /portfolio.
# All views that are related to portfolio should be registered with
# this blueprint and this blueprint will in turn be registred
# with the flask application
portfolio_bp = Blueprint('portfolio_bp', __name__, url_prefix='/portfolio')


@portfolio_bp.route('/')
def index():
    return render_template(
        'portfolio/home.html',
        supported_providers=SUPPORTED_PROVIDERS,
    )


# The <string: provider> in the route means we are expecting an string after
# /portfolio and all routes like /portfolio/1, /portfolio/2 should be routed
# to this controller
@portfolio_bp.route('/<string:provider>')
def portfolio(provider: str):
    if provider not in SUPPORTED_PROVIDERS:
        abort(404)

    return render_template(
        'portfolio/home.html',
        provider=provider.capitalize(),
    )
