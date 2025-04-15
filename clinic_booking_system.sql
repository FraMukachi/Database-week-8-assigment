-- Clinic Booking System Database
CREATE DATABASE IF NOT EXISTS clinic_db;
USE clinic_db;

-- Patients table
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other', 'Prefer not to say') NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE,
    address TEXT,
    registration_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    insurance_provider VARCHAR(100),
    insurance_number VARCHAR(50)
);

-- Doctors table
CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    license_number VARCHAR(50) UNIQUE NOT NULL,
    hire_date DATE NOT NULL,
    active_status BOOLEAN DEFAULT TRUE
);

-- Appointments table
CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Cancelled', 'No-show') DEFAULT 'Scheduled',
    reason TEXT,
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE,
    CONSTRAINT chk_time CHECK (end_time > start_time)
);

-- Medical records table
CREATE TABLE medical_records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_id INT,
    diagnosis TEXT,
    prescription TEXT,
    treatment TEXT,
    notes TEXT,
    record_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE SET NULL
);

-- Clinic services table
CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_minutes INT NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    active BOOLEAN DEFAULT TRUE
);

-- Doctor availability table
CREATE TABLE doctor_availability (
    availability_id INT AUTO_INCREMENT PRIMARY KEY,
    doctor_id INT NOT NULL,
    day_of_week ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE,
    CONSTRAINT chk_availability_time CHECK (end_time > start_time)
);

-- Sample data for patients
INSERT INTO patients (first_name, last_name, date_of_birth, gender, phone, email, address, insurance_provider, insurance_number)
VALUES
('Francis', 'Mujakachi, '1984-12-03', Male', '064-123-4567', 'fmujakachi@gmail.com', '1235 Weyer St, East London', 'OutSurance', 'ABC123456789'),
('Kevin', 'Mathews', '1992-11-21', 'Male', '072-234-5678', 'k.mathews@gmail.com', '45 Ellain Ave, KWT', 'Clientale', 'XYZ987654321'),
('Emily', 'Alice', '1988-06-03', 'Female', '071-345-6789', 'emily.wma@email.com', '6534 Cresent, EL', NULL, NULL);

-- Sample data for doctors
INSERT INTO doctors (first_name, last_name, specialization, phone, email, license_number, hire_date)
VALUES
('Jim', 'Smith', 'Cardiology', '062-987-6543', 'dr.smith@clinic.com', 'MD123456', '2010-06-15'),
('Kim', 'Anthony', 'Pediatrics', '073-876-5432', 'dr.kim@clinic.com', 'MD654321', '2015-03-22'),
('Jack', 'Angel', 'Orthopedics', '083-765-4321', 'dr.angel@clinic.com', 'MD789012', '2018-09-10');

-- Sample data for services
INSERT INTO services (service_name, description, duration_minutes, cost)
VALUES
('General Consultation', 'Routine health check-up', 30, 100.00),
('Cardiac Evaluation', 'Comprehensive heart health assessment', 60, 250.00),
('Pediatric Check-up', 'Child wellness examination', 45, 150.00),
('X-ray', 'Basic imaging service', 15, 75.00);

-- Sample data for doctor availability
INSERT INTO doctor_availability (doctor_id, day_of_week, start_time, end_time)
VALUES
(1, 'Monday', '09:00:00', '17:00:00'),
(1, 'Wednesday', '09:00:00', '17:00:00'),
(2, 'Tuesday', '08:00:00', '16:00:00'),
(2, 'Thursday', '08:00:00', '16:00:00'),
(3, 'Friday', '10:00:00', '18:00:00');

-- Sample data for appointments
INSERT INTO appointments (patient_id, doctor_id, appointment_date, start_time, end_time, reason)
VALUES
(1, 1, '2025-04-15', '10:00:00', '11:00:00', 'Annual cardiac check-udr.angel@clinic.com', '09:30:00', '10:15:00', 'Child vaccination'),
(3, 3, '2025-04-17', '14:00:00', '14:30:00', 'Knee pain consultation');

-- Sample data for medical records
INSERT INTO medical_records (patient_id, doctor_id, appointment_id, diagnosis, prescription, treatment)
VALUES
(1, 1, 1, 'Normal cardiac function', 'Continue current medications', 'Annual check-up completed'),
(2, 2, 2, 'Healthy development', 'Vaccine: MMR', 'Administered MMR vaccine');
