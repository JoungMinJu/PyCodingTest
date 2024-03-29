
SELECT HISTORY_ID, CEIL(FEE * IFNULL(DISCOUNT_RATE, 1)) AS FEE
FROM (SELECT A.CAR_ID, B.HISTORY_ID, A.DAILY_FEE * B.USING_DATE AS FEE, CASE WHEN USING_DATE >=  90 THEN "90일 이상" WHEN USING_DATE >= 30 THEN "30일 이상" WHEN USING_DATE >= 7 THEN "7일 이상" ELSE "X" END AS TYPE
FROM (SELECT CAR_ID , DAILY_FEE FROM CAR_RENTAL_COMPANY_CAR WHERE CAR_TYPE = "트럭") AS A JOIN
(SELECT HISTORY_ID, CAR_ID, DATEDIFF(END_DATE, START_DATE) + 1 AS USING_DATE FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) AS B
ON A.CAR_ID = B.CAR_ID
) AS F LEFT JOIN (SELECT CAR_TYPE, DURATION_TYPE, (1-DISCOUNT_RATE*0.01) AS DISCOUNT_RATE
FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
WHERE CAR_TYPE = "트럭") AS S
ON F.TYPE = S.DURATION_TYPE
ORDER BY FEE DESC, HISTORY_ID DESC