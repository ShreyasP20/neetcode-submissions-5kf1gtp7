-- Write your query below
select s.name
from sales_person s 
where sales_id not in ( select o.sales_id from orders o where o.com_id = (select com_id from company where name ='CRIMSON'))