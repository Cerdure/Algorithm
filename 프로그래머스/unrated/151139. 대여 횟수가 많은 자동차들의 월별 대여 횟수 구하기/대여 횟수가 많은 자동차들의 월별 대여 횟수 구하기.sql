-- 코드를 입력하세요
with c as 
(select month(start_date),car_id,count(*) records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date between '2022-08-01' and '2022-10-31'
group by month(start_date),car_id)

SELECT *
from c 
where car_id in
(select car_id 
 from c
 group by car_id
 having sum(records) > 4)
 and c.records > 0
order by 1,2 desc