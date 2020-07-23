"""
This batch should only be run when we want to load symbols for a specific
exchange into our database

python -m server.batch.setup_exchange_symbols --name=NYSE
"""
import argparse
import os
from sqlalchemy.exc import IntegrityError

from server.database import db_session
from server.data_access.stock_exchange import get_stock_exchange
from server.data_access.stock_exchange import register_stock_exchange
from server.data_access.ticker import register_ticker_symbol

# Parse the arguments to get the exchange we want to load information for
parser = argparse.ArgumentParser(
    description="Setup an exchange and its related tickers"
)
parser.add_argument("--name", type=str, help="The stock exchange symbol", required=True)
args = parser.parse_args()

exchange_name = args.name

# Create the exchange if it doesn't already exist. Fetch it if it already
# exists
try:
    stock_exchange = register_stock_exchange(name=exchange_name)
except IntegrityError:
    db_session.rollback()
    stock_exchange = get_stock_exchange(name=exchange_name)

# Load the symbols and company names into the symbols database
symbols_file_path = os.getcwd() + f"/server/data/exchange/{exchange_name}.txt"
try:
    with open(symbols_file_path, "r") as f:
        for line in f.readlines()[1:]:
            try:
                symbol, name = line.strip().split("\t")
            except ValueError:
                continue

            try:
                register_ticker_symbol(stock_exchange.id, symbol, name)
            except IntegrityError:
                db_session.rollback()
                print(f"ERROR: Integrity error while persisting {symbol}")
                continue
except FileNotFoundError:
    print(f"ERROR: Could not find the file with ticker symbols")
