Question 8. At Mission San Jose High School in fall 2023, what share of the school's a-g completers applied to at least one UC? 
(Universitywide `applicants` divided by `ag_completers`)<br>
Answer:99.1%

The following code computes the answer:
SELECT 
    high_school,
    applicants,
    ag_completers,
    (CAST(applicants AS FLOAT) / ag_completers) * 100 AS pct_applied
FROM bay_area_modeling_table
WHERE high_school = 'MISSION SAN JOSE HIGH SCHOOL'
  AND fall_term = 2023
  AND campus = 'Universitywide';

This code isolates the data for the applicants and a-g completers and computes the division.
It outputs 99.056% which rounds to **99.1%**
