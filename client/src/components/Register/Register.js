import React, { Component } from "react";
import axios from "axios";
import Alert from "react-bootstrap/Alert";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import FormFile from "react-bootstrap/FormFile";
import InputGroup from "react-bootstrap/InputGroup";
import "./Register.css";

const REGISTER_4XX_ERRORS_TO_USER_MESSAES = {
  USER_ALREADY_EXISTS: "Failed to register because username is already taken",
  UNSUPPORTED_CONTENT_TYPE:
    "Failed to register because profile picture format is unsupported",
};

export default class Register extends Component {
  constructor() {
    super();
    this.state = {
      first_name: "",
      last_name: "",
      username: "",
      password: "",
      profilePicture: "",
      error: "",
    };
  }

  uploadFile = (event) => {
    this.setState({
      profilePicture: event.target.files[0],
    });
  };

  onChange = (event) => {
    this.setState({
      [event.target.name]: event.target.value,
    });
  };

  onSubmit = (event) => {
    // We are using preventDefault so as to block the default browser action
    // of making a GET request to the backend
    event.preventDefault();

    const formData = new FormData();
    formData.append("first_name", this.state.first_name);
    formData.append("last_name", this.state.last_name);
    formData.append("username", this.state.username);
    formData.append("password", this.state.password);
    formData.append("profile_picture", this.state.profilePicture);

    axios
      .post("/auth/register", formData)
      .then((response) => {
        console.log("Successfully registered " + this.state.first_name);
        this.props.history.push("/home");
      })
      .catch((error) => {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx and the error message was that
        // the user already exists
        if (error.response && error.response.status === 400) {
          this.setState({
            error:
              REGISTER_4XX_ERRORS_TO_USER_MESSAES[error.response.data.message],
          });
        }
      });
  };

  render() {
    return (
      <div className="signup_wrapper">
        <div className="container container-xs">
          <h2 className="mb-1 text-center">Sign up</h2>
          <p className="fs-14 text-gray text-center mb-4">
            Track your portfolio and share recommendations with friends.
          </p>

          <Form onSubmit={this.onSubmit}>
            {/* If this.state.error is true, display the error message. Remember, we need
              to enclose this statement in brackets because we are writing Javascript code
              inside JSX.
              */}
            <Form.Group>
              {this.state.error && (
                <Alert variant="danger">{this.state.error}</Alert>
              )}
            </Form.Group>

            <Form.Row>
              <Form.Group className="col-md-6">
                <Form.Label htmlFor="first_name" className="col-form-label-sm">
                  First Name
                  <span className="required"> *</span>
                </Form.Label>
                <Form.Control
                  type="text"
                  name="first_name"
                  value={this.state.first_name}
                  onChange={this.onChange}
                  autoFocus
                  required
                />
              </Form.Group>

              <Form.Group className="col-md-6">
                <Form.Label htmlFor="last_name" className="col-form-label-sm">
                  Last Name
                  <span className="required"> *</span>
                </Form.Label>
                <Form.Control
                  type="text"
                  name="last_name"
                  value={this.state.last_name}
                  onChange={this.onChange}
                  required
                />
              </Form.Group>
            </Form.Row>

            <Form.Group>
              <Form.Label htmlFor="username" className="col-form-label-sm">
                Username
                <span className="required"> *</span>
              </Form.Label>
              <InputGroup>
                <InputGroup.Prepend>
                  <InputGroup.Text id="inputGroupPrepend2">@</InputGroup.Text>
                </InputGroup.Prepend>
                <Form.Control
                  type="text"
                  name="username"
                  value={this.state.username}
                  onChange={this.onChange}
                  required
                />
              </InputGroup>
            </Form.Group>

            <Form.Group>
              <Form.Label htmlFor="password" className="col-form-label-sm">
                Password
                <span className="required"> *</span>
              </Form.Label>
              <Form.Control
                type="password"
                name="password"
                value={this.state.password}
                onChange={this.onChange}
                required
              />
              <small id="passwordHelpBlock" className="form-text text-muted">
                Your password must be 8-20 characters long
              </small>
            </Form.Group>

            <Form.Group>
              <FormFile className="custom-file">
                <Form.Control
                  type="file"
                  name="profilePicture"
                  className="custom-file-input"
                  id="profilePicture"
                  onChange={this.uploadFile}
                  required
                />
                <Form.Label
                  className="custom-file-label col-form-label-sm"
                  htmlFor="profilePicture"
                >
                  {this.state.profilePicture.name || "Choose Profile Picture"}
                </Form.Label>
              </FormFile>
            </Form.Group>

            <Form.Group className="signUpButton">
              <Button type="submit" className="btn-block">
                Sign Up
              </Button>
            </Form.Group>
          </Form>

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
