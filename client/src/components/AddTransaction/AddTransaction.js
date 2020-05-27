import React, { Component } from "react";
import axios from "axios";

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
      <div>
        <form onSubmit={this.onSubmit} className="form-signin">
          <div className="form-group col-auto">
            <input
              type="text"
              name="ticker"
              value={this.state.ticker}
              onChange={this.onChange}
              className="form-control"
              placeholder="Ticker"
              autoFocus
              required
            />
          </div>

          <div className="form-group col-auto">
            <input
              type="text"
              name="orderType"
              value={this.state.orderType}
              onChange={this.onChange}
              className="form-control"
              placeholder="Buy or Sell"
              required
            />
          </div>

          <div className="form-group col-auto">
            <input
              type="text"
              name="price"
              value={this.state.price}
              onChange={this.onChange}
              className="form-control"
              placeholder="Price"
              required
            />
          </div>

          <div className="form-group col-auto">
            <input
              type="text"
              name="quantity"
              value={this.state.quantity}
              onChange={this.onChange}
              className="form-control"
              placeholder="Quantity"
              required
            />
          </div>

          <div className="form-group col-auto">
            <button type="submit" className="btn btn-primary btn-block">
              Submit Transaction
            </button>
          </div>
        </form>
      </div>
    );
  }
}
