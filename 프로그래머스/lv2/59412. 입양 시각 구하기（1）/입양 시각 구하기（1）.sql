-- 코드를 입력하세요
SELECT date_format(datetime,"%H"), count(*)
from ANIMAL_OUTS
where date_format(datetime,"%H") between 9 and 19
group by 1
order by 1