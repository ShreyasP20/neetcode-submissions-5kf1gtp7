-- Write your query below
select employee_id,
CASE 
when employee_id % 2 != 0 and name NOT LIKE 'M%'
Then salary
else 0 
End as bonus
from employees
order by employee_id;