import React, { Component } from "react";
import { Link } from "react-router-dom";
import "./NavBar.css";

export default class NavBar extends Component {
  render() {
    return (
      <div>
        <nav class="nav navbar justify-content-end navbar-expand-lg navbar-light">
          <div class="container">
            <a class="navbar-brand" href="#">
              <img
                src="/docs/4.1/assets/brand/bootstrap-solid.svg"
                width="30"
                height="30"
                alt=""
              />
              Portfolio Tracker
            </a>
            <Link to="/home" class="nav-item nav-link text-secondary">
              Home
            </Link>

            <Link to="/login" class="nav-item nav-link text-secondary">
              Login
            </Link>

            <Link to="/register" class="nav-item nav-link text-secondary active">
              Register
            </Link>
          </div>
        </nav>
      </div>
    );
  }
}
