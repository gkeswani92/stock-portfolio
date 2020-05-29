import React from "react";
import PropTypes from "prop-types";

import FeedCard from "../FeedCard/FeedCard";

const Feed = (props) => {
  return (
    <div>
      {props.feedItems.map((feedItem, index) => {
        return <FeedCard key={index} {...feedItem} />;
      })}
    </div>
  );
};

Feed.propTypes = {
  feedItems: PropTypes.arrayOf(
    PropTypes.shape({
      firstName: PropTypes.string.isRequired,
      lastName: PropTypes.string.isRequired,
      ticker: PropTypes.string.isRequired,
      orderType: PropTypes.string.isRequired,
      quantity: PropTypes.number.isRequired,
      price: PropTypes.number.isRequired,
      createdAt: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default Feed;
