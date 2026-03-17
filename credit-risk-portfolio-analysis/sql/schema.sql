CREATE TABLE loans (
    customer_id VARCHAR(20),
    age INT,
    annual_income INT,
    loan_amount INT,
    interest_rate DECIMAL(5,2),
    credit_score INT,
    dti_ratio DECIMAL(5,2),
    utilization_rate DECIMAL(5,2),
    employment_length_years INT,
    grade VARCHAR(2),
    purpose VARCHAR(50),
    home_ownership VARCHAR(20),
    region VARCHAR(20),
    loan_status VARCHAR(50),
    default_flag INT
);
