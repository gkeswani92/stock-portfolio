import React, { Component } from "react";
import PropTypes from "prop-types";
import "./FollowUsersPrompt.css";

export default class FollowUsersPrompt extends Component {
  static propTypes = {
    username: PropTypes.string,
  };

  render() {
    return (
      <div id="hero" className="d-flex align-items-center">
        <div className="container">
          <div className="row">
            <div className="col-lg-6">
              <h1>Let's follow some friends, {this.props.username}! </h1>
              <h2>
                Connect your Facebook account and follow some of your friends to
                see the how they are trading equities and options.
              </h2>

              <div
                className="fb-login-button"
                data-size="medium"
                data-button-type="continue_with"
                data-layout="rounded"
                data-auto-logout-link="false"
                data-use-continue-as="false"
                data-width=""
              ></div>
            </div>
            <div className="col-lg-6">
              <img src="./follow-friends.png" className="img-fluid" alt="" />
            </div>
          </div>
        </div>
      </div>
    );
  }
}
