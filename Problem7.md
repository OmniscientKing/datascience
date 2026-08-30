Question 7: Of Bay Area high school graduates in the class of 2023, what share enrolled at a California Community College within 12 months?
Answer: 34%

The following code sums the high school grads with these properties.

SELECT 
    SUM(enrolled_ccc) AS total_enrolled_ccc,
    SUM(graduates) AS total_graduates,
    ROUND((SUM(enrolled_ccc) * 100.0 / SUM(graduates)), 2) AS share_enrolled_ccc_pct
FROM bay_area_modeling_table
WHERE fall_term = 2023
  AND campus = 'Universitywide';

  It outputs 34.04%, which rounds to **34%**
