-- 코드를 입력하세요
SELECT product_code,sum(price*sales_amount)
from product p join offline_sale o on p.product_id = o.product_id
group by 1
order by 2 desc, 1