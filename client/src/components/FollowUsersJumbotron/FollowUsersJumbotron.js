import React, { Component } from "react";
import PropTypes from "prop-types";

export default class FollowUsersJumbotron extends Component {
  static propTypes = {
    username: PropTypes.string,
  };

  render() {
    return (
      <div>
        <div className="jumbotron">
          <h1 className="display-5">Hello, {this.props.username}!</h1>
          <p className="lead">
            Please follow other users to keep track of their transactions.
          </p>
          <p className="lead">
            <a className="btn btn-primary btn-lg" href="#" role="button">
              Find users
            </a>
          </p>
        </div>
      </div>
    );
  }
}
