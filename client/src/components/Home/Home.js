import React, { Component } from "react";
import Feed from "../Feed/Feed";
import FollowUsersJumbotron from "../FollowUsersJumbotron/FollowUsersJumbotron";
import axios from "axios";
import PropTypes from "prop-types";
import Spinner from "react-bootstrap/Spinner"

export default class Home extends Component {
  static propTypes = {
    userId: PropTypes.number,
    username: PropTypes.string,
    checkLoginStatus: PropTypes.func.isRequired,
  };

  constructor(props) {
    super(props);
    this.state = {
      feed: [],
      hasFeedItems: false,
      isLoading: true,
      userId: props.userId,
      username: props.username,
    };

    this.getFeed = this.getFeed.bind(this);
  }

  // Note: `componentWillMount` will only be called once when the component is
  // being mounted and will not be called on subsequent refreshes.
  componentWillMount() {
    // If a user id has been passed in, get the feed for the user. Else, check
    // if there is a user logged in coz someone can come directly to the /home
    // route
    if (this.props.userId) {
      this.getFeed();
    } else {
      this.props.checkLoginStatus();
    }
  }

  componentDidUpdate() {
    // If the component is updated and isLoading = true i.e. we don't have feed
    // items, we will get the feed
    if (this.state.isLoading === true) {
      this.getFeed();
    }
  }

  getFeed() {
    axios
      .get(`/feed/${this.props.userId}`)
      .then((response) => {
        let transactions = response.data.transactions;
        this.setState({
          feed: transactions,
          hasFeedItems: transactions.length !== 0 ? true : false,
          isLoading: false,
        });
      })
      .catch((error) => {
        console.log(error);
      });
  }

  render() {
    // Show an empty page until the async call to get the feed from the backend
    // is completed.
    if (this.state.isLoading === true) {
      return <Spinner animation="border" size="lg"/>
    }

    return (
      <div className="container">
        <div className="row">
          <div className="col-2"></div>
          <div className="col-8">
            {this.state.hasFeedItems && <Feed feedItems={this.state.feed} />}
            {!this.state.hasFeedItems && (
              <FollowUsersJumbotron username={this.props.username} />
            )}
          </div>
          <div className="col-2"></div>
        </div>
      </div>
    );
  }
}
