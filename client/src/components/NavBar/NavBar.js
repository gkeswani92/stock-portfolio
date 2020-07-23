import React, { Component } from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";
import Navbar from "react-bootstrap/Navbar";
import "./NavBar.css";

const NavBar = (props) => {
  const loggedInLinks = (
    <React.Fragment>
      <Link to="/addTransaction" className="nav-item nav-link text-light">
        Add Transaction
      </Link>
      <Link
        to="/logout"
        className="nav-item nav-link text-light"
        onClick={() => props.handleLogout()}
      >
        Logout
      </Link>
    </React.Fragment>
  );

  const loggedOutLinks = (
    <React.Fragment>
      <Link to="/login" className="nav-item nav-link text-light">
        Login
      </Link>
      <Link to="/register" className="nav-item nav-link text-light active">
        Register
      </Link>
    </React.Fragment>
  );

  return (
    <div>
      <Navbar bg="dark" variant="dark">
        <Navbar.Brand href="/">
          <img src="" width="30" height="30" alt="" />
          Portfolio Tracker
        </Navbar.Brand>

        <Link to="/home" className="nav-item nav-link text-light">
          Home
        </Link>

        {/* Display the login and register button only if there is no user that is currently logged in */}
        {!props.isLoggedIn && loggedOutLinks}

        {/* Display the logout button only if there is a user that is currently logged in */}
        {props.isLoggedIn && loggedInLinks}
      </Navbar>
    </div>
  );
};

// PropTypes is one way of adding type checking to JavaScript. Other
// competing projects are TypeScript from Microsoft and Flow from Facebook
// They are superior to prop types because they allow us to detect problems
// at compile time
NavBar.propTypes = {
  isLoggedIn: PropTypes.bool.isRequired,
};

export default NavBar;
