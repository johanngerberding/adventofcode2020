import sys 

def calc_arrival_times(raw: str):
    data = raw.splitlines()
    time = int(data[0])
    busses = [int(bus) for bus in data[1].split(',') if bus != 'x']
    arrival_times = []
    for bus in busses:
        if time % bus == 0:
            arrival_times.append(time)
        next_stop = time - time % bus + bus 
        arrival_times.append(next_stop)
    idx = arrival_times.index(min(arrival_times))
    waiting = arrival_times[idx] - time

    return time, busses, arrival_times

# my naive approachs works but only for smaller values, please use the chinese remainder theorem down below
def find_timestamp(raw: str):
    data = raw.splitlines()
    time = int(data[0])
    busses = [[idx, int(bus)] for idx, bus in enumerate(data[1].split(',')) if bus != 'x']
    step_size = max([bus[1] for bus in busses])
    print(f"step size: {step_size}")
    time = 0
    while True:
        c = 0
        if time % 1000000 == 0:
            print(time)
        for bus in busses:
            c += (time + bus[0]) % bus[1]
           
        if c == 0:
            return time
        time += 1 

        #time += busses[0][1]
        
        if time > 10000000000000000:
            return time
    

TEST = """939
7,13,x,x,59,x,31,19"""

#print(find_timestamp(TEST))


# chinese remainder code from
# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6

# theory: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
# good luck! ;)

from functools import reduce

# n = here the bus numbers
# a = factors
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 

def create_factors(raw: str) -> list:
    data = raw.splitlines()
    buslist = [int(bus) for bus in data[1].split(',') if bus != 'x']
    busses = [(idx, int(bus)) for idx, bus in enumerate(data[1].split(',')) if bus != 'x']
    factors = [(bus - idx) % bus for idx, bus in busses]
    return buslist, factors

with open("../inputs/day13.txt") as f: 
    data = f.read()
    busses, factors = create_factors(data)
    print(chinese_remainder(busses, factors))
    

        