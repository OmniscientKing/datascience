Question 9. How many distinct California public high schools sent at least one freshman applicant to UC in fall 2025?<br>
Answer: 244

SELECT 
    COUNT(DISTINCT high_school) AS distinct_schools_with_applicants
FROM bay_area_modeling_table
WHERE fall_term = 2025
  AND campus = 'Universitywide'
  AND applicants > 0;

This code is a basic count of the schools with non-zero applicants.

This results in **244**
