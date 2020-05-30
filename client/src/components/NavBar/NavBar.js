import React, { Component } from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";
import Navbar from "react-bootstrap/Navbar";
import "./NavBar.css";

export default class NavBar extends Component {
  onLogoutClick = () => {
    console.log("Logout button clicked");
    this.props.handleLogout();
  };

  render() {
    return (
      <div>
        <Navbar bg="dark" variant="dark">
          <Navbar.Brand href="/home">
            <img src="" width="30" height="30" alt="" />
            Portfolio Tracker
          </Navbar.Brand>

          <Link to="/home" className="nav-item nav-link text-light">
            Home
          </Link>

          {/* Display the login and register button only if there is no user
             that is currently logged in
          */}

          {!this.props.isLoggedIn && (
            <Link to="/login" className="nav-item nav-link text-light">
              Login
            </Link>
          )}

          {!this.props.isLoggedIn && (
            <Link
              to="/register"
              className="nav-item nav-link text-light active"
            >
              Register
            </Link>
          )}

          {/* Display the logout button only if there is a user that is currently
          logged in
          */}
          {this.props.isLoggedIn && (
            <Link to="/addTransaction" className="nav-item nav-link text-light">
              Add Transaction
            </Link>
          )}

          {this.props.isLoggedIn && (
            <Link
              to="/logout"
              className="nav-item nav-link text-light"
              onClick={() => this.onLogoutClick()}
            >
              Logout
            </Link>
          )}
        </Navbar>
      </div>
    );
  }
}

// PropTypes is one way of adding type checking to JavaScript. Other
// competing projects are TypeScript from Microsoft and Flow from Facebook
// They are superior to prop types because they allow us to detect problems
// at compile time
NavBar.propTypes = {
  isLoggedIn: PropTypes.bool.isRequired,
};
