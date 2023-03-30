-- 코드를 입력하세요
SELECT flavor
from first_half
group by 1
order by sum(total_order) desc, SHIPMENT_ID