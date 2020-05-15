import React, { Component } from "react";
import { Link } from "react-router-dom";
import "./NavBar.css";

export default class NavBar extends Component {
  render() {
    return (
      <div>
        <nav className="nav navbar justify-content-left navbar-expand-lg navbar-dark bg-dark">
            <a className="navbar-brand" href="#">
              <img
                src=""
                width="30"
                height="30"
                alt=""
              />
              Portfolio Tracker
            </a>
            <Link to="/home" className="nav-item nav-link text-light">
              Home
            </Link>

            <Link to="/login" className="nav-item nav-link text-light">
              Login
            </Link>

            <Link to="/register" className="nav-item nav-link text-light active">
              Register
            </Link>
        </nav>
      </div>
    );
  }
}
