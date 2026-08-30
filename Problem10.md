Question 10: Five schools are listed on the answer form. Using UC Berkeley 2022-2025, which one most OUTPERFORMS its expected admit rate, after controlling for a-g completion, poverty, applicant GPA and school size?
<br>Options:HERCULES HIGH SCHOOL, MISSION SENIOR HIGH SCHOOL, MONTEREY TRAIL HIGH SCHOOL, PHILLIP & SALA BURTON ACAD HS, RANCHO SAN JUAN HIGH SCHOOL

SELECT 
    high_school,
    AVG(admit_rate_residual) AS avg_admit_rate_residual
FROM dashboard_data
WHERE campus = 'Berkeley' 
  AND fall_term BETWEEN 2022 AND 2025
  AND high_school IN (
      'HERCULES HIGH SCHOOL',
      'MISSION SENIOR HIGH SCHOOL',
      'MONTEREY TRAIL HIGH SCHOOL',
      'PHILLIP & SALA BURTON ACAD HS',
      'RANCHO SAN JUAN HIGH SCHOOL'
  )
GROUP BY high_school
ORDER BY avg_admit_rate_residual DESC;

The code outputs the data for 3 of the schools (the other two don't have data)<br>
<img width="240" height="132" alt="image" src="https://github.com/user-attachments/assets/810149e2-216f-4e9c-8522-c26a5c4f636e" /><br>
** MISSION SENIOR HIGH SCHOOL** outperforms its expected admit rate by the highest amount.
