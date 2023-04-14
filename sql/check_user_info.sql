select user_id, nickname, concat(city," ", street_address1, " ", street_address2) as "전체주소", CONCAT(substr(TLNO,1,3), '-', substr(TLNO,4,4), '-', substr(TLNO,8,4)) AS phone
from  used_goods_user
where user_id in (select writer_id
from used_goods_board
group by writer_id
having count(*) >= 3)
order by user_id desc


SELECT ID, NICKNAME, ADDRESS, PHONE
FROM (
    SELECT USER.USER_ID AS ID, USER.NICKNAME AS NICKANME, CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS ADDRESS,
           CONCAT(SUBSTR(TLNO, 1, 3), "-", SUBSTR(TLNO, 4,4), '-', SUBSTR(TLNO, 8,4)) AS PHONE,
           COUNT(*) AS USER_COUNT
    FROM USED_GOODS_USER AS USER
    INNER JOIN USED_GOODS_BOARD AS BOARD ON USER.USER_ID = BOARD.WRITER_ID
    GROUP BY USER.USER_ID
     ) USER
WHERE USR_COUNT > 2
ORDER BY ID DESC