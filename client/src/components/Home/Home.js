import React, { Component } from "react";
import Transaction from "../Transaction/Transaction";
import axios from "axios";
import PropTypes from "prop-types";

export default class Home extends Component {
  static propTypes = {
    userId: PropTypes.number,
  };

  constructor(props) {
    super(props);
    this.state = {
      feed: [],
    };
  }

  componentWillMount() {
    if (this.props.userId) {
      axios
        .get(`/feed/${this.props.userId}`)
        .then((response) => {
          this.setState({
            feed: response.data.transactions,
          });
        })
        .catch((error) => {
          console.log(error);
        });
    }
  }

  render() {
    return (
      <div>
        {this.state.feed.map((value, index) => {
          return (
            <Transaction
              key={index}
              firstName={value.firstName}
              lastName={value.lastName}
              ticker={value.ticker}
              orderType={value.orderType}
              quantity={value.quantity}
              price={value.price}
              createdAt={value.createdAt}
            />
          );
        })}
      </div>
    );
  }
}
