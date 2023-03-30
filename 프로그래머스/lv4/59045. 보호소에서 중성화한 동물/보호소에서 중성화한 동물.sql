-- 코드를 입력하세요
SELECT o.animal_id,o.animal_type,o.name
from animal_ins i join animal_outs o on i.animal_id = o.animal_id
where sex_upon_intake not in ('Spayed%','Neutered%')
    and sex_upon_intake != sex_upon_outcome
order by 1
