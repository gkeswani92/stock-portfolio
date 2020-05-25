import React, { Component } from "react";
import PropTypes from "prop-types";
import "./Transaction.css";

export default class Transaction extends Component {
  static propTypes = {
    firstName: PropTypes.string.isRequired,
    lastName: PropTypes.string.isRequired,
    ticker: PropTypes.string.isRequired,
    orderType: PropTypes.string.isRequired,
    quantity: PropTypes.number.isRequired,
    price: PropTypes.number.isRequired,
    createdAt: PropTypes.string.isRequired,
  };

  render() {
    return (
      <div className="card">
        <div className="row">
          <div className="col-auto">
            <img
              src={"ticker/" + this.props.ticker + ".png"}
              className="img-fluid ticker-image rounded-circle"
              alt={this.props.ticker}
            />
          </div>
          <div className="col">
            <div className="card-body">
              {this.props.orderType === "BUY" && (
                <h5 className="card-title buy-alert">Buy Alert</h5>
              )}
              {this.props.orderType === "SELL" && (
                <h5 className="card-title sell-alert">Sell Alert</h5>
              )}

              <p className="card-text">
                {this.props.firstName} {this.props.lastName}{" "}
                {this.props.orderType === "BUY" && "bought"}{" "}
                {this.props.orderType === "SELL" && "sold"}{" "}
                {this.props.quantity} stocks of {this.props.ticker} at $
                {this.props.price}
              </p>

              <footer className="blockquote-footer">
                {this.props.createdAt}
              </footer>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
