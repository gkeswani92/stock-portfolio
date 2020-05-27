import React, { Component } from "react";
import PropTypes from "prop-types";
import Button from "react-bootstrap/Button";
import Jumbotron from "react-bootstrap/Jumbotron";

export default class FollowUsersJumbotron extends Component {
  static propTypes = {
    username: PropTypes.string,
  };

  render() {
    return (
      <Jumbotron>
        <h1 className="display-5">Hello, {this.props.username}!</h1>
        <p className="lead">
          Please follow other users to keep track of their transactions.
        </p>
        <p className="lead">
          <Button variant="primary">
            Find users
          </Button>
        </p>
      </Jumbotron>
    );
  }
}
