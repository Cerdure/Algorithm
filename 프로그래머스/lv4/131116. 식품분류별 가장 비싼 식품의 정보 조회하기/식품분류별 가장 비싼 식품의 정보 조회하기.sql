-- 코드를 입력하세요
SELECT f.category,f.price,f.product_name
from food_product f,
(select category,max(price) price
 from food_product
 group by category) m
where f.category in ('과자', '국', '김치', '식용유') 
and f.price = m.price 
and f.category = m.category
order by price desc
