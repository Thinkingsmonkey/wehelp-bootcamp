SHOW DATABASES;
create database mydb;
USE mydb;
SHOW TABLES;
CREATE TABLE product (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);
CREATE TABLE variant (
	id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    size VARCHAR(255) NOT NULL,
    price INT DEFAULT 30
);

INSERT INTO product (name) VALUES ("拿鐵");
INSERT INTO product (name) VALUES ("美式");
INSERT INTO product (name) VALUES ("珍奶");
INSERT INTO product (name) VALUES ("茉莉綠茶");

INSERT INTO variant(product_id, size, price) VALUES (1, "中杯", 45);
INSERT INTO variant(product_id, size, price) VALUES (1, "大杯", 60);
INSERT INTO variant(product_id, size, price) VALUES (2, "中杯", 50);
INSERT INTO variant(product_id, size, price) VALUES (2, "大杯", 65);
INSERT INTO variant(product_id, size, price) VALUES (3, "中杯", 55);
INSERT INTO variant(product_id, size, price) VALUES (3, "大杯", 70);
INSERT INTO variant(product_id, size, price) VALUES (4, "中杯", 70);

-- 設定外連結預防意外刪除，導致資料不一致
SELECT * FROM product;
SELECT * FROM variant;
-- ALTER TABLE product ADD FOREIGN KEY(id) REFERENCES variant(product_id);
-- ALTER TABLE product DROP FOREIGN KEY product_ibfk_1;
ALTER TABLE variant ADD FOREIGN KEY(product_id) REFERENCES product(id);
SHOW CREATE TABLE variant;
DELETE FROM product WHERE id=4;

-- 設定 index
ALTER TABLE product ADD INDEX name_index(name);
EXPLAIN SELECT * FROM product WHERE name="奶茶";
-- 新建立 table 時設立 index
CREATE TABLE test(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    INDEX name_index(name)
);
INSERT INTO test(name) VALUES ("測試用");
EXPLAIN SELECT * FROM test WHERE name="測試用";
-- PRIMARY 也是一種 index
EXPLAIN SELECT * FROM product WHERE id=2;
SELECT * FROM variant INNER JOIN product ON variant.product_id = product.id;
SELECT product.name, AVG(variant.price) FROM variant INNER JOIN product ON variant.product_id = product.id GROUP BY product.name;

# 先移除安全狀態
SET SQL_SAFE_UPDATES=0;
UPDATE product SET name="波霸奶茶" WHERE name="珍奶";
UPDATE product SET price=60 WHERE price<55 AND price>40;

DELETE FROM product WHERE name="文山清茶";
DROP TABLE product