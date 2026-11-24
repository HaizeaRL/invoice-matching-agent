

CREATE TABLE subsidiary(
	id INTEGER PRIMARY KEY,
	nif TEXT NOT NULL UNIQUE,
	name TEXT NOT NULL
	);
	
CREATE TABLE product(
	sku TEXT NOT NULL PRIMARY KEY,
	description TEXT NOT NULL,
	ref_price TEXT NOT NULL
);
 
CREATE TABLE purchase_order(
	id INTEGER PRIMARY KEY,
	po_number TEXT NOT NULL UNIQUE,
	subsidiary_id INTEGER NOT NULL REFERENCES subsidiary(id),
	provider TEXT NOT NULL,
	order_date TEXT NOT NULL
);

CREATE TABLE order_line(
	order_id INTEGER NOT NULL REFERENCES purchase_order(id),
	line_no INTEGER NOT NULL,
	product_id TEXT NOT NULL REFERENCES product(sku),
	description TEXT NOT NULL,
	quantity INTEGER NOT NULL,
	unit_price TEXT NOT NULL,
	PRIMARY KEY (order_id, line_no),
	UNIQUE (order_id, product_id) 
);