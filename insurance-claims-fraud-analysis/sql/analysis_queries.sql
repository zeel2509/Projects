-- Fraud rate by incident type
SELECT
    incident_type,
    COUNT(*) AS claims,
    ROUND(AVG(fraud_reported) * 100, 2) AS fraud_rate_pct,
    ROUND(AVG(claim_amount), 2) AS avg_claim_amount
FROM claims
GROUP BY incident_type
ORDER BY fraud_rate_pct DESC;

-- Fraud rate by region
SELECT
    region,
    COUNT(*) AS claims,
    ROUND(AVG(fraud_reported) * 100, 2) AS fraud_rate_pct,
    ROUND(AVG(settlement_days), 2) AS avg_settlement_days
FROM claims
GROUP BY region
ORDER BY fraud_rate_pct DESC;

-- Severity mix
SELECT
    incident_severity,
    COUNT(*) AS claims,
    ROUND(AVG(claim_amount), 2) AS avg_claim_amount
FROM claims
GROUP BY incident_severity
ORDER BY avg_claim_amount DESC;
