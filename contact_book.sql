-- contact_book.sql
CREATE DATABASE IF NOT EXISTS contact_book;
USE contact_book;

-- Contacts table
CREATE TABLE contacts (
    contact_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Phone numbers table
CREATE TABLE phone_numbers (
    phone_id INT AUTO_INCREMENT PRIMARY KEY,
    contact_id INT NOT NULL,
    phone_type ENUM('Mobile', 'Home', 'Work', 'Other') NOT NULL DEFAULT 'Mobile',
    number VARCHAR(20) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (contact_id) REFERENCES contacts(contact_id) ON DELETE CASCADE
);

-- Tags table (for categorizing contacts)
CREATE TABLE tags (
    tag_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Contact-Tag relationship (M-M)
CREATE TABLE contact_tags (
    contact_id INT NOT NULL,
    tag_id INT NOT NULL,
    PRIMARY KEY (contact_id, tag_id),
    FOREIGN KEY (contact_id) REFERENCES contacts(contact_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE
);

-- Sample data
INSERT INTO contacts (first_name, last_name, email, address) VALUES
('Jay', 'Doe', 'john.doe@example.com', '123 Main St, Anytown'),
('June', 'Smith', 'jane.smith@example.com', '456 Oak Ave, Somewhere'),
('Bob', 'John', 'bob.john@example.com', '789 Pine Rd, Nowhere');

INSERT INTO tags (name, description) VALUES
('Family', 'Close family members'),
('Work', 'Work colleagues'),
('Friends', 'Personal friends');

INSERT INTO contact_tags VALUES
(1, 1), (1, 3), (2, 2), (3, 1), (3, 3);

INSERT INTO phone_numbers (contact_id, phone_type, number, is_primary) VALUES
(1, 'Mobile', '011-0101', TRUE),
(1, 'Work', '011-0102', FALSE),
(2, 'Mobile', '011-0201', TRUE),
(3, 'Home', '011-0301', TRUE);
