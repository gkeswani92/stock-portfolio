import React, { Component } from "react";
import axios from "axios";

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
        [event.target.name]: event.target.value
    });
  }

  onSubmit(event) {
    // We are using preventDefault so as to block the default browser action
    // of making a GET request to the backend
    event.preventDefault()

    axios.post(
        '/auth/register',
        {
            'first_name': this.state.first_name,
            'last_name': this.state.last_name,
            'username': this.state.username,
            'password': this.state.password
        }
    ).then(response => {
        console.log('Successfully registered ' + this.state.first_name)
    })
  }

  render() {
    return (
      <div class="container-fluid">
        <h1 class="mb-1 text-center">Sign up</h1>
        <p class="fs-14 text-gray text-center mb-5">
            Track your portfolio and see what your friends are up to!
        </p>
        <form onSubmit={this.onSubmit}>
            <div class="form-row col-auto">
                <div class="form-group col-md-6">
                    <label htmlFor="first_name" class="col-form-label-lg">First Name</label>
                    <input
                        type="text"
                        name="first_name"
                        value={this.state.first_name}
                        onChange={this.onChange}
                        placeholder="Enter First Name"
                        class="form-control"
                        required
                    />
                </div>

                <div class="form-group col-md-6">
                    <label htmlFor="last_name" class="col-form-label-lg">Last Name</label>
                    <input
                        type="text"
                        name="last_name"
                        value={this.state.last_name}
                        onChange={this.onChange}
                        placeholder="Enter Last Name"
                        class="form-control"
                        required
                    />
                </div>
            </div>

            <div class="form-group col-auto">
                <label htmlFor="username" class="col-form-label-lg">Username</label>
                <div class="input-group">
                    <div class="input-group-prepend">
                        <span class="input-group-text" id="inputGroupPrepend2">@</span>
                    </div>
                    <input
                        type="text"
                        name="username"
                        value={this.state.username}
                        onChange={this.onChange}
                        placeholder="Enter Username"
                        class="form-control"
                        required
                    />
                </div>
            </div>

            <div class="form-group col-auto">
                <label htmlFor="password" class="col-form-label-lg">Password</label>
                <input
                    type="password"
                    name="password"
                    value={this.state.password}
                    onChange={this.onChange}
                    placeholder="Enter Password"
                    class="form-control"
                    required
                />
                <small id="passwordHelpBlock" class="form-text text-muted">
                    Your password must be 8-20 characters long
                </small>
            </div>

            <div class="form-group col-auto">
                <button type="submit" class="btn btn-primary">Sign Up</button>
            </div>
        </form>

        <p class="text-gray-soft text-center small mb-2">
            By clicking "Sign up" you agree to our <a href="https://themes.getbootstrap.com/terms">Terms of Service</a>.
        </p>
        <p class="text-gray-soft text-center small mb-2">
            Already have an account? <a href="https://themes.getbootstrap.com/signin/">Sign in</a>
        </p>
      </div>
    );
  }
}
