-- 코드를 입력하세요
select category,sum(sales)
from book b join book_sales s on b.book_id = s.book_id
where year(sales_date)='2022' and month(sales_date)='1'
group by category
order by 1