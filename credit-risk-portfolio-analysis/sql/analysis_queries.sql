-- Default rate by loan grade
SELECT
    grade,
    COUNT(*) AS total_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct
FROM loans
GROUP BY grade
ORDER BY default_rate_pct DESC;

-- Average loan amount and credit score by default status
SELECT
    default_flag,
    ROUND(AVG(loan_amount), 2) AS avg_loan_amount,
    ROUND(AVG(credit_score), 2) AS avg_credit_score,
    ROUND(AVG(dti_ratio), 2) AS avg_dti
FROM loans
GROUP BY default_flag;

-- Higher-risk purposes
SELECT
    purpose,
    COUNT(*) AS loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct
FROM loans
GROUP BY purpose
ORDER BY default_rate_pct DESC;
