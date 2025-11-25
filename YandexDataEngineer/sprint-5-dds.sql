DROP TABLE IF EXISTS dds.dm_users;

CREATE TABLE IF NOT EXISTS dds.dm_users
(
	id serial PRIMARY KEY NOT NULL, 
	user_id varchar NOT NULL,
	user_name varchar NOT NULL,
	user_login varchar NOT NULL
);

DROP TABLE IF EXISTS dds.dm_restaurants;

CREATE TABLE IF NOT EXISTS dds.dm_restaurants
(
	id serial PRIMARY KEY NOT NULL, 
	restaurant_id varchar NOT NULL,
	restaurant_name varchar NOT NULL,
	active_from timestamp NOT NULL,
	active_to timestamp NOT NULL
);

DROP TABLE IF EXISTS dds.dm_products;

CREATE TABLE IF NOT EXISTS dds.dm_products
(
	id serial PRIMARY KEY NOT NULL,
	restaurant_id int NOT NULL,
	product_id varchar NOT NULL,
	product_name varchar NOT NULL,
	product_price numeric(14,2) NOT NULL DEFAULT 0 CHECK (product_price >= 0),
	active_from timestamp NOT NULL,
	active_to timestamp NOT NULL 
);

ALTER TABLE dds.dm_products 
ADD CONSTRAINT dm_products_restaurant_id_fkey
FOREIGN KEY(restaurant_id) REFERENCES dds.dm_restaurants(id);

DROP TABLE IF EXISTS dds.dm_timestamps;

CREATE TABLE IF NOT EXISTS dds.dm_timestamps
(
	id serial PRIMARY KEY NOT NULL, 
	ts timestamp NOT NULL,
	year smallint NOT NULL CHECK (year BETWEEN 2022 AND 2500),
	month smallint NOT NULL CHECK (month BETWEEN 1 AND 12),
	day smallint NOT NULL CHECK (day BETWEEN 1 AND 31),
	time time NOT NULL,
	date date NOT NULL 
);

DROP TABLE IF EXISTS dds.dm_orders;

CREATE TABLE IF NOT EXISTS dds.dm_orders
(
	id serial PRIMARY KEY NOT NULL, 
	user_id int NOT NULL,
	restaurant_id int NOT NULL,
	timestamp_id int NOT NULL,
	order_key varchar NOT NULL,
	order_status varchar NOT NULL
);

ALTER TABLE dds.dm_orders ADD CONSTRAINT dm_orders_user_id_fkey
FOREIGN KEY(user_id) REFERENCES dds.dm_users(id);

ALTER TABLE dds.dm_orders ADD CONSTRAINT dm_orders_restaurants_id_fkey
FOREIGN KEY(restaurant_id) REFERENCES dds.dm_restaurants(id);

ALTER TABLE dds.dm_orders ADD CONSTRAINT dm_orders_timestamps_id_fkey
FOREIGN KEY(timestamp_id) REFERENCES dds.dm_timestamps(id);

DROP TABLE IF EXISTS dds.fct_product_sales;

CREATE TABLE IF NOT EXISTS dds.fct_product_sales
(
id serial PRIMARY KEY NOT NULL,
product_id int NOT NULL,
order_id int NOT NULL,
"count" int NOT NULL DEFAULT 0 CHECK ("count" >= 0),
price numeric(14, 2) NOT NULL DEFAULT 0 CHECK (price >= 0),
total_sum numeric(14, 2) NOT NULL DEFAULT 0 CHECK (total_sum >= 0),
bonus_payment numeric(14, 2) NOT NULL DEFAULT 0 CHECK(bonus_payment >= 0),
bonus_grant numeric(14, 2) NOT NULL DEFAULT 0 check(bonus_grant >= 0)
);

ALTER TABLE dds.fct_product_sales ADD CONSTRAINT fct_product_sales_product_id_fkey
FOREIGN KEY(product_id) REFERENCES dds.dm_products(id);

ALTER TABLE dds.fct_product_sales ADD CONSTRAINT fct_product_sales_order_id_fkey
FOREIGN KEY(order_id) REFERENCES dds.dm_orders(id);