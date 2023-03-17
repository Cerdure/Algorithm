-- 코드를 입력하세요
SELECT count(a.name) from (select * from ANIMAL_INS group by name) a