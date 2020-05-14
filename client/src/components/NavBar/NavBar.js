import React, { Component } from "react";
import { Link } from "react-router-dom";
import "./NavBar.css";

export default class NavBar extends Component {
  render() {
    return (
      <div>
        <nav class="nav navbar justify-content-left navbar-expand-lg navbar-dark bg-dark">
            <a class="navbar-brand" href="#">
              <img
                src="/docs/4.1/assets/brand/bootstrap-solid.svg"
                width="30"
                height="30"
                alt=""
              />
              Portfolio Tracker
            </a>
            <Link to="/home" class="nav-item nav-link text-light">
              Home
            </Link>

            <Link to="/login" class="nav-item nav-link text-light">
              Login
            </Link>

            <Link to="/register" class="nav-item nav-link text-light active">
              Register
            </Link>
        </nav>
      </div>
    );
  }
}
