CREATE IF NOT EXISTS DATABASE supermarket; 
USE supermarket;

CREATE IF NOT EXISTS TABLE products (
        product_id INT PRIMARY KEY,
    	product_name VARCHAR(255) NOT NULL,
    	description TEXT,
    	price DECIMAL(10, 2) NOT NULL,
    	quantity_in_stock INT NOT NULL,
	    CHECK (price > 0 and quantity_in_stock >= 0)
);

CREATE IF NOT EXISTS TABLE suppliers (
    	supplier_id INT PRIMARY KEY,
		supplier_name VARCHAR(255) NOT NULL,
		address TEXT NOT NULL,
    	contact_information BIGINT NOT NULL,
        CHECK (contact_information >= 1000000000 AND contact_information <= 9999999999)
);

CREATE IF NOT EXISTS TABLE customers (
		customer_id INT PRIMARY KEY,
		customer_name VARCHAR(255) NOT NULL,
		address TEXT NOT NULL,
		contact_information BIGINT NOT NULL,
        CHECK (contact_information >= 1000000000 AND contact_information <= 9999999999)
);

CREATE IF NOT EXISTS TABLE employees (
    	employee_id INT PRIMARY KEY,
    	employee_name VARCHAR(255) NOT NULL,
    	address TEXT NOT NULL,
    	contact_information BIGINT NOT NULL,
    	job_position VARCHAR(255) NOT NULL,
        CHECK (contact_information >= 1000000000 AND contact_information <= 9999999999)
);

CREATE IF NOT EXISTS TABLE sales (
    	sale_id INT PRIMARY KEY,
		sale_date DATE NOT NULL,
    	customer_id INT NOT NULL,
		employee_id INT,
		FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
		FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

CREATE IF NOT EXISTS TABLE sale_items (
	unique_id INT AUTO_INCREMENT,
    sale_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity_sold INT NOT NULL,
    FOREIGN KEY (sale_id) REFERENCES sales(sale_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    PRIMARY KEY (unique_id)
);

CREATE IF NOT EXISTS TABLE purchases (
    purchase_id INT PRIMARY KEY,
    purchase_date DATE NOT NULL,
    supplier_id INT NOT NULL,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

CREATE IF NOT EXISTS TABLE purchase_items (
	unique_id INT AUTO_INCREMENT,
    purchase_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity_purchased INT NOT NULL,
    FOREIGN KEY (purchase_id) REFERENCES purchases(purchase_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    PRIMARY KEY (unique_id)
);

-- some initial values

	-- Product Table Values
INSERT INTO products VALUES(0001, 'Apple', 'Fruit', 120.00, 20 );
INSERT INTO products VALUES(0002, 'Banana', 'Fruit', 80.00, 20 );
INSERT INTO products VALUES(0003, 'Mango', 'Fruit', 250.00, 20 );
INSERT INTO products VALUES(0004, 'Strawberry', 'Fruit', 300.00, 20 );
INSERT INTO products VALUES(0005, 'Kiwi', 'Fruit', 500.00, 20 );
INSERT INTO products VALUES(0006, 'Lettuce', 'Vegetable', 80.00, 20 );
INSERT INTO products VALUES(0007, 'Brocoli', 'Vegetable', 130.00, 20 );
INSERT INTO products VALUES(0008, 'Cauliflower', 'Vegetable', 60.00, 20 );
INSERT INTO products VALUES(0009, 'Okra', 'Vegetable', 40.00, 20 );
INSERT INTO products VALUES(0010, 'Potato', 'Vegetable', 25.00, 20 );
-- SELECT * FROM products;

	-- Supplier Table Values
INSERT INTO suppliers VALUES(0001, 'Fruit Supplier', 'Sabji Mandi', '1110203451');
INSERT INTO suppliers VALUES(0002, 'Vegetable Supplier', 'Sabji Mandi', '1230454324');
-- SELECT * FROM suppliers;

	-- Customer Table Values
INSERT INTO customers VALUES(0001, 'X', 'Apartment', 1111111111);
INSERT INTO customers VALUES(0002, 'Y', 'Bungalow', 2222222222);
INSERT INTO customers VALUES(0003, 'Z', 'Building', 3333333333);

	-- Employee Table Values
INSERT INTO employees VALUES(0001, 'A', 'Residential Complex', 4444444444, 'Manager');
INSERT INTO employees VALUES(0002, 'B', 'Residential Complex', 5555555555, 'Salesman');

	-- Sales Table Values
INSERT INTO sales VALUES(0001, '2023-04-05', 0001, NULL);
INSERT INTO sales VALUES(0002, '2023-04-05', 0002, 0002);

	-- Sale Items Table Values
INSERT INTO sale_items (sale_id, product_id, quantity_sold) VALUES(0001, 0001, 10);
INSERT INTO sale_items (sale_id, product_id, quantity_sold) VALUES(0002, 0001, 5);
INSERT INTO sale_items (sale_id, product_id, quantity_sold) VALUES(0002, 0005, 5);
INSERT INTO sale_items (sale_id, product_id, quantity_sold) VALUES(0002, 0010, 5);

	-- Purchases Table Values
INSERT INTO purchases VALUES(0001, '2023-04-04', 0001);
INSERT INTO purchases VALUES(0002, '2023-04-04', 0002);

	-- Purchase Items Table Values
INSERT INTO purchase_items (purchase_id, product_id, quantity_purchased) VALUES(0001, 0001, 35);
INSERT INTO purchase_items (purchase_id, product_id, quantity_purchased) VALUES(0001, 0002, 20);
INSERT INTO purchase_items (purchase_id, product_id, quantity_purchased) VALUES(0001, 0003, 20);
INSERT INTO purchase_items (purchase_id, product_id, quantity_purchased) VALUES(0001, 0004, 20);
INSERT INTO purchase_items (purchase_id, product_id, quantity_purchased) VALUES(0001, 0005, 25);
INSERT INTO purchase_items (purchase_id, product_id, quantity_purchased) VALUES(0002, 0006, 20);
INSERT INTO purchase_items (purchase_id, product_id, quantity_purchased) VALUES(0002, 0007, 20);
INSERT INTO purchase_items (purchase_id, product_id, quantity_purchased) VALUES(0002, 0008, 20);
INSERT INTO purchase_items (purchase_id, product_id, quantity_purchased) VALUES(0002, 0009, 20);
INSERT INTO purchase_items (purchase_id, product_id, quantity_purchased) VALUES(0002, 0010, 25);
