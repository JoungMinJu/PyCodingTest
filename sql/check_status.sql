# 조건에 부합하는 중고거래 상태 조회하기
# 2022년 10월 5일에 등록된. -> 게시글 ID, 작성자 ID, 게시글 제목, 가격, 거래 상태
# 거래 상태 sale = 판매중 reserved 예약중 done 거래 완료
# 게시글 ID des

SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, case when STATUS = "SALE" THEN "판매중" WHEN STATUS = "RESERVED" THEN "예약중" WHEN STATUS = "DONE" THEN "거래완료" END AS STATUS
FROM USED_GOODS_BOARD
WHERE DATE(CREATED_DATE) = "2022-10-05"
ORDER BY BOARD_ID DESC