1. In fall 2025, how many UC campuses did the average applicant apply to? (round to two decimal places)
Answer: 5.74%

We want to find the # of UC campuses the average applicant applied to.
This can be calculated by the total applications for the colleges divided by the # of applicants. 

To calculate this we used the following code.

SELECT SUM(applicants) AS total_applicants 
FROM bay_area_modeling_table 
WHERE campus = 'Universitywide' AND fall_term = '2025';

SELECT SUM(applicants) AS total_applicants 
FROM bay_area_modeling_table 
WHERE campus != 'Universitywide' AND fall_term = '2025';

The first chunk of code calculates the number of applicants (26457) while the second chunk tallies the applications to each college (151775).
With this data we compute the # of UC campuses the average applicant applied to. 
151775/26457 = 5.7366670446... = which is **5.74**.
