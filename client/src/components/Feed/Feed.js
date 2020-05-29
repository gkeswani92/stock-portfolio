import React, { Component } from "react";
import FeedCard from "../FeedCard/FeedCard";

export default class Feed extends Component {
  render() {
    return (
      <div>
        {this.props.feedItems.map((value, index) => {
          return (
            <FeedCard
              key={index}
              firstName={value.firstName}
              lastName={value.lastName}
              ticker={value.ticker}
              orderType={value.orderType}
              quantity={value.quantity}
              price={value.price}
              createdAt={value.createdAt}
            />
          );
        })}
      </div>
    );
  }
}
