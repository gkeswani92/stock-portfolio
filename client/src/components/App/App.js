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
    };
  }

  componentWillMount() {
    this.checkLoginStatus();
  }

  checkLoginStatus() {
    axios
      .get("/auth/is_logged_in")
      .then((response) => {
        if (
          response.data.is_logged_in === true &&
          this.state.isLoggedIn === false
        ) {
          this.setState({ isLoggedIn: true });
          console.log("User is already logged in");
        }
      })
      .catch((error) => {
        console.log("Error encountered while checking if user is logged in");
      });
  }

  render() {
    return (
      <Router>
        <div className="App">
          <NavBar />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/home" />
        </div>
      </Router>
    );
  }
}
