set session my.number_of_products = '100';
set session my.number_of_mutualfunds = '5';
set session my.number_of_cmp = '5';

CREATE EXTENSION pgcrypto;

INSERT INTO product
select id, concat('Product ', id) 
FROM GENERATE_SERIES(1, current_setting('my.number_of_products')::int) as id;

INSERT INTO userp values(1,'Anmol');

INSERT INTO mutualfund
select id, concat('MF ', id) 
FROM GENERATE_SERIES(1, current_setting('my.number_of_mutualfunds')::int) as id;

INSERT INTO company
select id, concat('CP ', id) 
FROM GENERATE_SERIES(1, current_setting('my.number_of_cmp')::int) as id;