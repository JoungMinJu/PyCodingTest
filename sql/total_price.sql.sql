select a.writer_id as USER_ID, b.nickname AS NICKNAME, sum(a.price) AS TOTAL_SALES
from used_goods_board as a join used_goods_user as b on a.writer_id = b.user_id
where a.status = "DONE"
group by a.writer_id
HAVING TOTAL_SALES >= 700000
order by TOTAL_SALES