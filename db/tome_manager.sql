
DROP TABLE IF EXISTS tomes;
DROP TABLE IF EXISTS authors;


CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

CREATE TABLE tomes (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  genre VARCHAR(255),
  cost INT,
  quantity INT,
  price INT,
  author_id INT REFERENCES authors(id)
); 