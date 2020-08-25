import React from "react";
import PropTypes from "prop-types";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

import "./Feed.css";

import FeedCard from "../FeedCard/FeedCard";

const Feed = (props) => {
  return (
    <Container className="feed-page">
      <Row>
        <Col md={2} lg={3} />
        <Col md={8} lg={6}>
          <div>
            {props.feedItems.map((feedItem, index) => {
              return <FeedCard key={index} {...feedItem} />;
            })}
          </div>
        </Col>
        <Col md={2} lg={3} />
      </Row>
    </Container>
  );
};

Feed.propTypes = {
  feedItems: PropTypes.arrayOf(
    PropTypes.shape({
      firstName: PropTypes.string.isRequired,
      lastName: PropTypes.string.isRequired,
      ticker: PropTypes.string.isRequired,
      tickerLogo: PropTypes.string.isRequired,
      orderType: PropTypes.string.isRequired,
      quantity: PropTypes.number.isRequired,
      price: PropTypes.number.isRequired,
      createdAt: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default Feed;
