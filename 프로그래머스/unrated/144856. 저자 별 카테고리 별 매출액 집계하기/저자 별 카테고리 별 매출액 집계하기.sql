-- 코드를 입력하세요
select a.author_id, author_name,category,sum(price*sales)
from book b 
    left join author a on b.author_id = a.author_id 
    join book_sales s on b.book_id = s.book_id
where year(sales_date) = 2022 and month(sales_date) = 1
group by category, author_id
order by 1,3 desc