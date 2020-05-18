import React, { Component } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import axios from "axios";
import NavBar from "../NavBar/NavBar";
import Register from "../Register/Register";
import Login from "../Login/Login";
import "./App.css";

export default class App extends Component {
  constructor() {
    super();
    this.state = {
      isLoggedIn: false,
      userId: {},
    };

    this.handleLogout = this.handleLogout.bind(this);
  }

  componentWillMount() {
    this.checkLoginStatus();
  }

  checkLoginStatus() {
    axios
      .get("/auth/is_logged_in")
      .then((response) => {
        if (response.data.is_logged_in && !this.state.isLoggedIn) {
          this.setState({
            isLoggedIn: true,
            userId: response.data.user,
          });
          console.log("User is already logged in");
        } else if (!response.data.is_logged_in && this.state.isLoggedIn) {
          this.setState({
            isLoggedIn: false,
            userId: {},
          });
          console.log("User is not logged in as per the backend. Reset state");
        }
      })
      .catch((error) => {
        console.log("Error encountered while checking if user is logged in");
      });
  }

  handleLogout() {
    axios
      .post("/auth/logout")
      .then((response) => {
        if (response.data.logged_out) {
          this.setState({
            isLoggedIn: false,
            userId: {},
          });
          console.log("User has been logged out");
        }
      })
      .catch((error) => {
        console.log("Error encountered while logging out the user");
      });
  }

  render() {
    return (
      <Router>
        <div className="App">
          <NavBar
            isLoggedIn={this.state.isLoggedIn}
            handleLogout={this.handleLogout}
          />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/home" />
        </div>
      </Router>
    );
  }
}
