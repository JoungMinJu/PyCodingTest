
-- 코드를 입력하세요
SELECT S.TITLE, S.BOARD_ID,  F.REPLY_ID, F.WRITER_ID, F.CONTENTS, DATE_FORMAT(F.CREATED_DATE, "%Y-%m-%d") AS CREATED_DATE
FROM (
SELECT TITLE, BOARD_ID
FROM USED_GOODS_BOARD
WHERE CREATED_DATE >= "2022-10-01" AND CREATED_DATE <= "2022-10-31") AS S
JOIN (SELECT BOARD_ID, REPLY_ID, WRITER_ID, CONTENTS, CREATED_DATE FROM USED_GOODS_REPLY) AS F
ON S.BOARD_ID = F.BOARD_ID
ORDER BY F.CREATED_DATE, S.TITLE