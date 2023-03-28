-- 코드를 입력하세요
SELECT count(name) from (select * from ANIMAL_INS group by name) as A