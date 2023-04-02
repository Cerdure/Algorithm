-- 코드를 입력하세요
SELECT distinct c.car_id
from CAR_RENTAL_COMPANY_CAR c join CAR_RENTAL_COMPANY_RENTAL_HISTORY h
    on c.car_id = h.car_id
where car_type = '세단' and month(start_date) = 10
order by 1 desc