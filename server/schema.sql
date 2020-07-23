DROP TABLE IF EXISTS stock_exchange;

CREATE TABLE stock_exchange (
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(64) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT unique_exchange UNIQUE(name)
);


CREATE TABLE ticker (
    id INT(11) NOT NULL AUTO_INCREMENT,
    exchange_id INT(1) NOT NULL,
    ticker VARCHAR(64) NOT NULL,
    company_name VARCHAR(512) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT unique_ticker_exchange UNIQUE(exchange_id, ticker),
    FOREIGN KEY (exchange_id) REFERENCES stock_exchange(id)
);


CREATE TABLE equity_order (
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    ticker_id INT NOT NULL,
    order_type VARCHAR(6) NOT NULL,
    quantity FLOAT NOT NULL,
    price FLOAT NOT NULL,
    created_at INT NOT NULL,
    PRIMARY KEY (id),
    INDEX (user_id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (ticker_id) REFERENCES ticker(id)
);