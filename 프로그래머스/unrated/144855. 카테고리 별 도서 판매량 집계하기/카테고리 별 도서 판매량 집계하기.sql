-- 코드를 입력하세요
with s as
(select book_id,sum(sales) total
from book_sales
where sales_date between '2022-01-01' and '2022-1-31'
group by book_id)

SELECT b.category,sum(s.total)
from book b, s
where b.book_id = s.book_id
group by b.category
order by 1