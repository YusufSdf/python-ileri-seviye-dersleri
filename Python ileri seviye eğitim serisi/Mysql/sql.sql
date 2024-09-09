alter table  products
Add CONSTRAINT fk_categories_products
FOREIGN KEY (categoryId) REFERENCES categories(id)