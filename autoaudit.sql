CREATE DATABASE IF NOT EXISTS AutoAuditDB;
USE AutoAuditDB;

-- Table for incoming applications
CREATE TABLE policy_applications (
    app_id INT PRIMARY KEY AUTO_INCREMENT,
    applicant_name VARCHAR(100),
    credit_score INT,
    age INT,
    has_prior_claims BOOLEAN,
    status VARCHAR(20) DEFAULT 'Pending' -- 'Auto-Approved', 'Manual Review', 'Declined'
);

-- Table for business rules (demonstrates dynamic configuration)
CREATE TABLE underwriting_rules (
    rule_id INT PRIMARY KEY AUTO_INCREMENT,
    min_credit_score INT DEFAULT 650,
    min_age INT DEFAULT 18,
    max_age INT DEFAULT 85
);

-- Insert a test applicant and a rule
INSERT INTO underwriting_rules (min_credit_score, min_age, max_age) VALUES (660, 21, 80);
INSERT INTO policy_applications (applicant_name, credit_score, age, has_prior_claims) 
VALUES ('John Doe', 720, 35, FALSE), ('Jane Smith', 580, 25, TRUE);