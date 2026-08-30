Question 3: Fall 2025: at which UC campus does applying to Computer Science cost the most admit rate, versus that campus's overall admit rate?
Answer: UC Davis


This can be computed by calculating the general admission rate and the computer science admission rate and calculating the percent difference.
Luckily each admission rate is already computed for us.

SELECT 
    campus,
    MAX(CASE WHEN broad_discipline = 'All disciplines' THEN admit_rate END) AS overall_admit_rate,
    MAX(CASE WHEN broad_discipline = 'Computer Science' THEN admit_rate END) AS cs_admit_rate,
    (MAX(CASE WHEN broad_discipline = 'All disciplines' THEN admit_rate END) - 
     MAX(CASE WHEN broad_discipline = 'Computer Science' THEN admit_rate END)) AS admit_rate_cost
FROM uc_freshman_admission_by_discipline
WHERE campus = 'Berkeley' 
  AND fall_term = '2025'
GROUP BY campus;

We tried all the colleges and found that **UC DAVIS* had the biggest difference at 25% and the biggest shift with 56.8% decrease in acceptance.
