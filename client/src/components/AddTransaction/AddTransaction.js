import React, { Component } from "react";
import axios from "axios";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Modal from "react-bootstrap/Modal";

export default class AddTransaction extends Component {
  constructor(props) {
    super(props);
    this.state = {
      ticker: "",
      orderType: "",
      price: "",
      quantity: "",
    };

    this.onChange = this.onChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  onChange(event) {
    this.setState({
      [event.target.name]: event.target.value,
    });
  }

  onSubmit(event) {
    console.log(this.state);
    // We are using preventDefault so as to block the default browser action
    // of making a GET request to the backend
    event.preventDefault();

    const formData = new FormData();
    formData.append("ticker", this.state.ticker);
    formData.append("order_type", this.state.orderType);
    formData.append("price", this.state.price);
    formData.append("quantity", this.state.quantity);

    axios
      .post("/transaction/add/2/v1", formData)
      .then((response) => {
        console.log("Successfully added transaction");
      })
      .catch((error) => {
        console.log(error);
      });
  }

  render() {
    return (
      <Modal.Dialog centered>
        <Modal.Header closeButton>Add a Transaction</Modal.Header>
        <Modal.Body>
          <Form onSubmit={this.onSubmit} className="form-signin">
            <Form.Group>
              <Form.Control
                type="text"
                name="ticker"
                value={this.state.ticker}
                onChange={this.onChange}
                placeholder="Ticker"
                autoFocus
                required
              />
            </Form.Group>

            <Form.Group>
              <Form.Control
                type="text"
                name="orderType"
                value={this.state.orderType}
                onChange={this.onChange}
                placeholder="Buy or Sell"
                required
              />
            </Form.Group>

            <Form.Group>
              <Form.Control
                type="text"
                name="price"
                value={this.state.price}
                onChange={this.onChange}
                placeholder="Price"
                required
              />
            </Form.Group>

            <Form.Group>
              <Form.Control
                type="text"
                name="quantity"
                value={this.state.quantity}
                onChange={this.onChange}
                placeholder="Quantity"
                required
              />
            </Form.Group>

            <Form.Group>
              <Button variant="primary" type="submit" className="btn-block">
                Submit Transaction
              </Button>
            </Form.Group>
          </Form>
        </Modal.Body>
      </Modal.Dialog>
    );
  }
}
