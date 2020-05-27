import React, { Component } from "react";
import PropTypes from "prop-types";
import Row from "react-bootstrap/Row";
import Card from "react-bootstrap/Card";
import Col from "react-bootstrap/Col";
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
      <Card>
        <Row>
          <div className="col-auto">
            <Card.Img
              src={"ticker/" + this.props.ticker + ".png"}
              className="img-fluid ticker-image rounded-circle"
              alt={this.props.ticker}
            />
          </div>
          <Col>
            <Card.Body>
              {this.props.orderType === "BUY" && (
                <h5 className="card-title buy-alert">Buy Alert</h5>
              )}
              {this.props.orderType === "SELL" && (
                <h5 className="card-title sell-alert">Sell Alert</h5>
              )}

              <Card.Text>
                {this.props.firstName} {this.props.lastName}{" "}
                {this.props.orderType === "BUY" && "bought"}{" "}
                {this.props.orderType === "SELL" && "sold"}{" "}
                {this.props.quantity} stocks of {this.props.ticker} at $
                {this.props.price}
              </Card.Text>

              <Card.Footer className="blockquote-footer">
                {this.props.createdAt}
              </Card.Footer>
            </Card.Body>
          </Col>
        </Row>
      </Card>
    );
  }
}
