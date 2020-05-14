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
      <div>
        <form onSubmit={this.onSubmit}>
          <label htmlFor="first_name">First Name</label>
          <input
            type="text"
            name="first_name"
            value={this.state.first_name}
            onChange={this.onChange}
            placeholder="Enter First Name"
          />

          <label htmlFor="last_name">Last Name</label>
          <input
            type="text"
            name="last_name"
            value={this.state.last_name}
            onChange={this.onChange}
            placeholder="Enter Last Name"
          />

          <label htmlFor="username">Username</label>
          <input
            type="text"
            name="username"
            value={this.state.username}
            onChange={this.onChange}
            placeholder="Enter Username"
          />

          <label htmlFor="password">Password</label>
          <input
            type="password"
            name="password"
            value={this.state.password}
            onChange={this.onChange}
            placeholder="Enter Password"
          />

          <button type="submit">Register</button>
        </form>
      </div>
    );
  }
}
