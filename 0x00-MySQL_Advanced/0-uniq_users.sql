-- creates a users table with 3 fields(id[integer, autoincrements and primary key], email[string, never null, unique]
-- , name[string]). should not fail if table already exists;
CREATE TABLE IF NOT EXISTS `users` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
);
