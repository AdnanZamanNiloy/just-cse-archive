-- 1. Create the database
CREATE DATABASE  hall_management_system;
USE hall_management_system;

-- 2. Users Table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    role VARCHAR(20) NOT NULL, -- 'student' or 'admin'
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Students Table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    email VARCHAR(100),
    full_name VARCHAR(100),
    department VARCHAR(100),
    session VARCHAR(50),
    date_of_birth DATE,
    gender VARCHAR(10),
    mobile_number VARCHAR(20),
    Father’s_name VARCHAR(100),
    Mother’s_name VARCHAR(100),
    emergency_number VARCHAR(20),
    permanent_address TEXT,
    photo_url VARCHAR(255),
    FOREIGN KEY (student_id) REFERENCES users(user_id)
);

-- 4. Admin Table
CREATE TABLE admins (
    admin_id INT PRIMARY KEY,
    full_name VARCHAR(100),
    designation VARCHAR(50),
    phone VARCHAR(20),
    FOREIGN KEY (admin_id) REFERENCES users(user_id)
);

-- 5. Notices Table
CREATE TABLE notices (
    notice_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150),
    content TEXT,
    created_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES admins(admin_id)
);

-- 6. Offices Table
CREATE TABLE offices (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    contact_email VARCHAR(100),
    phone VARCHAR(20),
    designation VARCHAR(50),
    location VARCHAR(100),
    hours VARCHAR(50)
);

-- 7. Student Room Table
CREATE TABLE student_room (
    student_id INT PRIMARY KEY,
    room_no VARCHAR(20),
    assigned_on DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- 8. Seat Applications Table
CREATE TABLE seat_applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    Father’s_occupation VARCHAR(100),
    Mother’s_occupation VARCHAR(100),
    cgpa DECIMAL(3,2),
    year_semester VARCHAR(50),
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- 9. Swap Requests Table
CREATE TABLE swap_requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    requester_id INT,
    target_id INT,
    reason TEXT,
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
    requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (requester_id) REFERENCES students(student_id),
    FOREIGN KEY (target_id) REFERENCES students(student_id)
);

-- 10. Cancellations Table
CREATE TABLE cancellations (
    cancellation_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    reason VARCHAR(100),
    custom_reason TEXT,
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
    document_url VARCHAR(255),
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- 11. Payments Table
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    amount DECIMAL(10,2),
    type VARCHAR(50), -- Seat Fee, Dining, etc.
    payment_date DATE,
    receipt_url VARCHAR(255),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- 12. Complaints Table
CREATE TABLE complaints (
    complaint_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    category VARCHAR(50), -- Room, Dining, Security
    message TEXT,
    status ENUM('pending', 'resolved') DEFAULT 'pending',
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- 13. Messages Table (Contact Developer)
CREATE TABLE messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    subject VARCHAR(150),
    message TEXT,
    attachment_url VARCHAR(255),
    phone_number VARCHAR(20),
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
