-- a script that creates a table second_table and adds multiple rows
CREATE TABLE IF NOT EXISTS second_tables (id INT, name VARCHAR(256), score INT);
INSERT INTO second_tables VALUES
	(1, 'John', 10), 
	(2, 'Alex', 3), 
	(3, 'Bob', 14), 
	(4, 'George', 8);
