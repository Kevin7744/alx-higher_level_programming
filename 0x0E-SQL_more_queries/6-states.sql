-- creates database hbtn_0d_usa and the table states

CREATE DATBASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_od_usa.states (
id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL);
