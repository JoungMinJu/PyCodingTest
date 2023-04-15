# 주차 요금 계산
from collections import defaultdict
import math

now_fees = []

def calc_minute(time) :
    time_lst = time.split(":")
    return int(time_lst[0]) * 60 + int(time_lst[1])

def calc_fee(result_minute) :
    if result_minute <= now_fees[0] :
        return now_fees[1]
    return now_fees[1] + math.ceil((result_minute - now_fees[0]) / now_fees[2]) * now_fees[3]

def calculate(record) : # 시간들이 있음
    answer = 0
    while record :
        in_time = record.pop(0)
        if not record :
            out_time = "23:59"
        else :
            out_time = record.pop(0)
        answer += (calc_minute(out_time) - calc_minute(in_time))
    return calc_fee(answer)

def solution(fees, records):
    global now_fees
    answer = []
    now_fees = fees
    record_dict = defaultdict(list)
    for record in records :
        info = record.split(" ")
        record_dict[info[1]].append(info[0])
    keys = list(record_dict.keys())
    keys.sort()
    for key in keys :
        now_record = record_dict[key]
        answer.append(calculate(now_record))
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))


