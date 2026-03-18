CREATE TABLE claims (
    claim_id VARCHAR(20),
    customer_id VARCHAR(20),
    policy_type VARCHAR(20),
    premium_amount DECIMAL(10,2),
    claim_amount DECIMAL(12,2),
    incident_type VARCHAR(30),
    incident_severity VARCHAR(20),
    claim_date DATE,
    settlement_days INT,
    region VARCHAR(10),
    policy_tenure_years INT,
    customer_age INT,
    fraud_reported INT,
    claim_status VARCHAR(20)
);
