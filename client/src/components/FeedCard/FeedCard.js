import React from "react";
import PropTypes from "prop-types";
import Media from "react-bootstrap/Media";

import "./FeedCard.css";

const FeedCard = (props) => {
  return (
    <div className="posts-section">
      <div className="post-bar">
        <div className="post_topbar">
          <div className="usy-dt">
            <img src="./1.jpg" alt="" />
            <div className="usy-name">
              <h3>
                {props.firstName} {props.lastName}
              </h3>
              <span>
                <img src="./clock.png" className="img-fluid clock-image" />
                {props.createdAt}
              </span>
            </div>
          </div>
        </div>

        {/* <div className="order-description"> */}
        {/* <img
          src={props.tickerLogo}
          className="img-fluid ticker-image"
          alt={props.ticker}
        /> */}
        {/* <Media.Body>
            {props.orderType === "BUY" && (
              <h5 className="buy-alert feed-content">Buy Alert</h5>
            )}
            {props.orderType === "SELL" && (
              <h5 className="sell-alert feed-content">Sell Alert</h5>
            )}

            <p className="feed-content">
              {props.firstName} {props.lastName}{" "}
              {props.orderType === "BUY" && "bought"}{" "}
              {props.orderType === "SELL" && "sold"} {props.quantity} stocks of{" "}
              {props.ticker} at ${props.price}
            </p>

            <footer className="blockquote-footer feed-content">
              {props.createdAt}
            </footer>
          </Media.Body> */}
        {/* </div> */}
      </div>
    </div>
  );
};

FeedCard.propTypes = {
  firstName: PropTypes.string.isRequired,
  lastName: PropTypes.string.isRequired,
  ticker: PropTypes.string.isRequired,
  orderType: PropTypes.string.isRequired,
  quantity: PropTypes.number.isRequired,
  price: PropTypes.number.isRequired,
  createdAt: PropTypes.string.isRequired,
};

export default FeedCard;
