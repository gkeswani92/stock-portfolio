import React, { Component } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import axios from "axios";
import AddTransaction from "../AddTransaction/AddTransaction";
import NavBar from "../NavBar/NavBar";
import Register from "../Register/Register";
import Login from "../Login/Login";
import Home from "../Home/Home";
import "./App.css";

export default class App extends Component {
  constructor() {
    super();
    this.state = {
      isLoggedIn: false,
      userId: NaN,
      username: "",
    };
  }

  componentWillMount() {
    this.checkLoginStatus();
  }

  checkLoginStatus = () => {
    axios
      .get("/auth/is_logged_in")
      .then((response) => {
        if (response.data.is_logged_in && !this.state.isLoggedIn) {
          this.setState({
            isLoggedIn: true,
            userId: response.data.user.user_id,
            username: response.data.user.username,
          });
          console.log("User is already logged in");
        } else if (!response.data.is_logged_in && this.state.isLoggedIn) {
          this.setState({
            isLoggedIn: false,
            userId: NaN,
            username: "",
          });
          console.log("User is not logged in as per the backend. Reset state");
        }
      })
      .catch((error) => {
        console.log("Error encountered while checking if user is logged in");
      });
  };

  handleLogout = () => {
    axios
      .post("/auth/logout")
      .then((response) => {
        if (response.data.logged_out) {
          this.setState({
            isLoggedIn: false,
            userId: NaN,
            username: "",
          });
          console.log("User has been logged out");
        }
      })
      .catch((error) => {
        console.log("Error encountered while logging out the user");
      });
  };

  render() {
    return (
      <Router>
        <div className="App">
          <NavBar
            isLoggedIn={this.state.isLoggedIn}
            handleLogout={this.handleLogout}
          />

          {/* React router makes it possible to support client side routing.
          These routes make sure that the correct component is rendered based
          on the URL that is entered in the browser
          */}
          <Route exact path="/login" component={Login} />
          <Route exact path="/register" component={Register} />
          <Route exact path="/addTransaction" component={AddTransaction} />
          <Route
            path="/home"
            render={(props) => (
              <Home
                userId={this.state.userId}
                username={this.state.username}
                checkLoginStatus={this.checkLoginStatus}
              />
            )}
          />
        </div>
      </Router>
    );
  }
}
