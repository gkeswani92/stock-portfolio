import React, { Component } from "react";
import PropTypes from "prop-types";
import Row from "react-bootstrap/Row";
import Card from "react-bootstrap/Card";
import Col from "react-bootstrap/Col";
import Media from "react-bootstrap/Media";
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
      <Media>
        <img
          src={"ticker/" + this.props.ticker + ".png"}
          className="img-fluid ticker-image"
          alt={this.props.ticker}
        />
        <Media.Body>
          {this.props.orderType === "BUY" && (
            <h5 className="buy-alert feed-content">Buy Alert</h5>
          )}
          {this.props.orderType === "SELL" && (
            <h5 className="sell-alert feed-content">Sell Alert</h5>
          )}

          <p className="feed-content">
            {this.props.firstName} {this.props.lastName}{" "}
            {this.props.orderType === "BUY" && "bought"}{" "}
            {this.props.orderType === "SELL" && "sold"} {this.props.quantity}{" "}
            stocks of {this.props.ticker} at ${this.props.price}
          </p>

          <footer className="blockquote-footer feed-content">{this.props.createdAt}</footer>
        </Media.Body>
      </Media>
    );
  }
}
