-- 코드를 입력하세요
SELECT user_id, nickname, sum(price)
from USED_GOODS_BOARD join USED_GOODS_USER on writer_id = user_id
where status = 'DONE'
group by 1
having sum(price) > 699999
order by 3