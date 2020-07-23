import React from "react";
import "./LandingPage.css";

const LandingPage = () => {

  return (
    <div id="hero" className="d-flex align-items-center">
      <div className="container">
        <div className="row">
          <div className="col-lg-6">
            <h1>Find your next stock pick</h1>
            <h2>
              Millions of users around the world use our website to follow other users and see how they trade.
              Find your friends and get rich together.
            </h2>
            <a href="/register" className="download-btn">
              <i className="bx bxl-play-store"></i> Register{" "}
            </a>
            <a href="/login" className="download-btn">
              <i className="bx bxl-apple"></i> Login{" "}
            </a>
          </div>
          <div className="col-lg-6">
            <img
              src="./hero-img.png"
              className="img-fluid"
              alt=""
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;
