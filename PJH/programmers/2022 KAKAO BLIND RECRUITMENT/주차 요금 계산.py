import math
from collections import defaultdict

class Car:

    def __init__(self, number):
        self.number = number
        self.state = "OUT"
        self.total_time = 0
        self.last_in = '00:00'
        self.last_out = '23:59'

    def calc_time(self, out_time):
        ih, im = map(int, self.last_in.split(":"))
        oh, om = map(int, out_time.split(":"))

        it = ih*60 + im
        ot = oh*60 + om

        self.total_time += ot - it


def solution(fees, records):
    answer = []

    cars = defaultdict(Car)

    for record in records:
        t, n, c = record.split()

        if n not in cars.keys():
            cars[n] = Car(n)

        cars[n].state = c
        if c == 'IN':
            cars[n].last_in = t
        elif c == 'OUT':
            cars[n].calc_time(t)

    for number in cars:
        car = cars[number]
        if car.state == "IN":
            car.calc_time('23:59')

        if car.total_time <= fees[0]:
            answer.append((number, fees[1]))
        else:
            fee = fees[1] + (math.ceil((car.total_time - fees[0]) / fees[2])) * fees[3]
            answer.append((number, fee))

    answer.sort()
    temp = []
    for n, c in answer:
        temp.append(c)
    answer = temp

    return answer


solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                                "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
