import React, { Component } from "react";
import Feed from "../Feed/Feed";
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
      isLoading: true,
    };

    this.getFeed = this.getFeed.bind(this);
  }

  componentWillMount() {
    if (this.props.userId) {
      this.getFeed();
    }
  }

  getFeed() {
    axios
      .get(`/feed/${this.props.userId}`)
      .then((response) => {
        this.setState({
          feed: response.data.transactions,
          hasFeedItems: true,
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
      return <div />
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
