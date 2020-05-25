import React, { Component } from "react";
import Transaction from "../Transaction/Transaction";
import FollowUsersJumbotron from "../FollowUsersJumbotron/FollowUsersJumbotron";
import axios from "axios";
import PropTypes from "prop-types";

export default class Home extends Component {
  static propTypes = {
    userId: PropTypes.number,
    username: PropTypes.string,
  };

  constructor(props) {
    super(props);
    this.state = {
      feed: [],
      hasFeedItems: false,
      userId: this.props.userId,
      username: this.props.username,
    };
  }

  componentWillReceiveProps(props) {
    this.setState({
      userId: props.userId,
      username: props.username,
    });
  }

  componentWillMount() {
    if (this.state.userId) {
      this.getFeed();
    }
  }

  getFeed() {
    axios
      .get(`/feed/${this.state.userId}`)
      .then((response) => {
        this.setState({
          feed: response.data.transactions,
          hasFeedItems: true,
        });
      })
      .catch((error) => {
        console.log(error);
      });
  }

  render() {
    return (
      <div>
        {this.state.hasFeedItems &&
          this.state.feed.map((value, index) => {
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

        {!this.state.hasFeedItems && (
          <FollowUsersJumbotron username={this.props.username} />
        )}
      </div>
    );
  }
}
