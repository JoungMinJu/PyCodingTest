select distinct(a.car_id)
from car_rental_company_car as a join
car_rental_company_rental_history as b
on a.car_id = b.car_id
where b.start_date between date("2022-10-01") and date("2022-10-31") and a.car_type = "세단"
order by a.car_id desc