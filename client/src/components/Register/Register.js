import React, { Component } from "react";
import axios from "axios";
import "./Register.css";

export default class Register extends Component {
  constructor() {
    super();
    this.state = {
      first_name: "",
      last_name: "",
      username: "",
      password: "",
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

    axios
      .post("/auth/register", {
        first_name: this.state.first_name,
        last_name: this.state.last_name,
        username: this.state.username,
        password: this.state.password,
      })
      .then((response) => {
        console.log("Successfully registered " + this.state.first_name);
      });
  }

  render() {
    return (
      <div className="signup_wrapper">
        <div className="container container-xs">
          <h2 className="mb-1 text-center">Sign up</h2>
          <p className="fs-14 text-gray text-center mb-4">
            Track your portfolio and share recommendations with friends.
          </p>
          <form onSubmit={this.onSubmit}>
            <div className="form-row col-auto">
              <div className="form-group col-md-6">
                <label htmlFor="first_name" className="col-form-label-sm">
                  First Name
                  <span className="required"> *</span>
                </label>
                <input
                  type="text"
                  name="first_name"
                  value={this.state.first_name}
                  onChange={this.onChange}
                  className="form-control"
                  required
                />
              </div>

              <div className="form-group col-md-6">
                <label htmlFor="last_name" className="col-form-label-sm">
                  Last Name
                  <span className="required"> *</span>
                </label>
                <input
                  type="text"
                  name="last_name"
                  value={this.state.last_name}
                  onChange={this.onChange}
                  className="form-control"
                  required
                />
              </div>
            </div>

            <div className="form-group col-auto">
              <label htmlFor="username" className="col-form-label-sm">
                Username
                <span className="required"> *</span>
              </label>
              <div className="input-group">
                <div className="input-group-prepend">
                  <span className="input-group-text" id="inputGroupPrepend2">
                    @
                  </span>
                </div>
                <input
                  type="text"
                  name="username"
                  value={this.state.username}
                  onChange={this.onChange}
                  className="form-control"
                  required autoFocus
                />
              </div>
            </div>

            <div className="form-group col-auto">
              <label htmlFor="password" className="col-form-label-sm">
                Password
                <span className="required"> *</span>
              </label>
              <input
                type="password"
                name="password"
                value={this.state.password}
                onChange={this.onChange}
                className="form-control"
                required
              />
              <small id="passwordHelpBlock" className="form-text text-muted">
                Your password must be 8-20 characters long
              </small>
            </div>

            <div className="form-group col-auto">
              <button type="submit" className="btn btn-primary btn-block">
                Sign Up
              </button>
            </div>
          </form>

          <p className="text-gray-soft text-center small mb-2">
            By clicking "Sign up" you agree to our{" "}
            <a href="https://themes.getbootstrap.com/terms">Terms of Service</a>
            .
          </p>
          <p className="text-gray-soft text-center small mb-2">
            Already have an account?{" "}
            <a href="https://themes.getbootstrap.com/signin/">Sign in</a>
          </p>
        </div>
      </div>
    );
  }
}
