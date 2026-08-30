Question 2: Fall 2025 admit rate at UCLA for applicants from California public high schools.<br>
Answer: 8.28% <br>

We wish to find the admit rate at UCLA in 2025 for public schools.<br>

This can be computed by dividing the admissions by the applications of private schools.<br>

SELECT <br>
&emsp;    SUM(admits) AS total_admits,<br>
&emsp;    SUM(applicants) AS total_applicants,<br>
&emsp;    ROUND((SUM(admits) * 100.0 / SUM(applicants)), 2) AS admit_rate_percentage<br>
FROM bay_area_modeling_table <br>
WHERE lower(school_type) LIKE '%public%'
<br>&emsp;  AND fall_term = '2025'  <br>
&emsp;  AND campus = 'Los Angeles'<br>

With our newfound knowledge from the first question we combine two chunks which compute the admissions and the applications.
This outputs **8.28%**
