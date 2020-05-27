import React, { Component } from "react";
import axios from "axios";
import "./Login.css";

export default class Login extends Component {
  constructor() {
    super();
    this.state = {
      username: "",
      password: "",
      error: "",
    };

    this.onChange = this.onChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  onChange(event) {
    this.setState({
      [event.target.name]: event.target.value,
    });
  }

  onSubmit(event) {
    // We are using preventDefault so as to block the default browser action
    // of making a GET request to the backend
    event.preventDefault();

    var isLoginSuccessful = axios
      .post("/auth/login", {
        username: this.state.username,
        password: this.state.password,
      });

    isLoginSuccessful.then((response) => {
        console.log("Login Successful for " + this.state.username);
        this.props.history.push('/home');
      })
      .catch((error) => {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx and the error message was that
        // the user already exists
        if (
          error.response &&
          error.response.status === 400 &&
          error.response.data.message === "INVALID_CREDENTIALS"
        ) {
          this.setState({
            error: 'Invalid credentials. Please try again.',
          });
          return false
        }
      });
  }

  render() {
    return (
      <div className="signin_wrapper">
        <div className="container container-xs">
          <h3 className="mb-3 text-center">Please sign in</h3>

          <form onSubmit={this.onSubmit} className="form-signin">

            {
              /* If this.state.error is true, display the error message. Remember, we need
              to enclose this statement in brackets because we are writing Javascript code
              inside JSX.
              */
            }
            <div className="form-group col-auto">
              {this.state.error && (
                <div className="alert alert-danger" role="alert">
                  {this.state.error}
                </div>
              )}
            </div>

            <div className="form-group col-auto">
                <input
                  type="text"
                  name="username"
                  value={this.state.username}
                  onChange={this.onChange}
                  className="form-control"
                  placeholder="Username"
                  autoFocus
                  required
                />
            </div>

            <div className="form-group col-auto">
              <input
                type="password"
                name="password"
                value={this.state.password}
                onChange={this.onChange}
                className="form-control"
                placeholder="Password"
                required
              />
            </div>

            <div className="form-group col-auto signInButton">
              <button type="submit" className="btn btn-primary btn-block">
                Sign in
              </button>
            </div>
          </form>
        </div>
      </div>
    );
  }
}
