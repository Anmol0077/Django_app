-- Creation of product table
CREATE TABLE IF NOT EXISTS product (
  product_id INT NOT NULL,
  name varchar(250) NOT NULL,
  PRIMARY KEY (product_id)
);

CREATE TABLE IF NOT EXISTS userp (
  user_id INT NOT NULL,
  name varchar(250) NOT NULL,
  PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS mutualfund (
  mf_id INT NOT NULL,
  mf_name varchar(250) NOT NULL,
  PRIMARY KEY (mf_id)
);

CREATE TABLE IF NOT EXISTS company (
  cmp_id INT NOT NULL,
  cmp_name varchar(250) NOT NULL,
  PRIMARY KEY (cmp_id)
);