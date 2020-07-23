DROP TABLE IF EXISTS stock_exchange;

CREATE TABLE stock_exchange (
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(64) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT unique_exchange UNIQUE(name)
);