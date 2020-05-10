from typing import Set

from flask import abort
from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import session
from flask import url_for

from stock_portfolio.data_access.user import get_user_by_id

SUPPORTED_PROVIDERS: Set[str] = {
    'Fidelity',
    'Robinhood',
}

# Defining a blue print for all URLs that begin with /portfolio.
# All views that are related to portfolio should be registered with
# this blueprint and this blueprint will in turn be registred
# with the flask application
portfolio_bp = Blueprint('portfolio_bp', __name__, url_prefix='/portfolio')


@portfolio_bp.route('/home')
def index():
    user_id = session.get('user_id')

    # If a logged out user tries to access this page, we should re-direct them
    # to the login page
    if not user_id:
        # The url_for() function generates the URL to a view based on a name
        # and arguments. The name associated with a view is also called the
        # endpoint, and by default it’s the same as the name of the view
        # function
        return redirect(url_for('auth.login'))

    user = get_user_by_id(user_id)
    return render_template(
        'portfolio/home.html',
        supported_providers=SUPPORTED_PROVIDERS,
        username=user.username,
    )


# The <string: provider> in the route means we are expecting an string after
# /portfolio and all routes like /portfolio/1, /portfolio/2 should be routed
# to this controller
@portfolio_bp.route('/<string:provider>')
def provider_portfolio(provider: str):
    print(f"Calling {provider}")
    if provider.capitalize() not in SUPPORTED_PROVIDERS:
        abort(404)

    return render_template(
        'portfolio/home.html',
        provider=provider,
    )
