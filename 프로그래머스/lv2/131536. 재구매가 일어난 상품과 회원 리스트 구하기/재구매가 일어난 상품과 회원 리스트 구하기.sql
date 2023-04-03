-- 코드를 입력하세요
SELECT user_id,product_id
from ONLINE_SALE 
group by 1,2
having count(*) > 1
order by 1,2 desc