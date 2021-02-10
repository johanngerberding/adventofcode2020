from typing import NamedTuple
import copy 

START = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

def read_input(raw: str) -> list:
    data_str = [line.strip("\n") for line in raw.splitlines()]
    data = []
    for line in data_str:
        data.append([el for el in line])
    return data


def adjacent_seats(seats: list ,seat: tuple) -> list:
    adj_seats = []
    y, x = seat
    x_max = len(seats[0])
    y_max = len(seats)
    for i in range(max(0, y-1), min(y+2,y_max)):
        for j in range(max(0, x-1), min(x+2, x_max)):
            if (i == y and j == x):
                continue
            adj_seats.append(seats[i][j])

    return adj_seats


def seating_process(raw:str) -> list:
    
    data = read_input(raw)
    data_ = copy.deepcopy(data)
    ops = 1
    while ops != 0:
        ops = 0
        for row in range(len(data)):
            for col in range(len(data[0])):
                val = data[row][col]
                if val != '.':
                    adj_seats = adjacent_seats(data, (row,col))
                    assert len(adj_seats) <= 8 and len(adj_seats) >= 3
                    if (val == 'L' and len([seat for seat in adj_seats if seat == '#']) == 0):
                        data_[row][col] = '#'
                        ops += 1
                    elif (val == '#' and len([seat for seat in adj_seats if seat == '#']) >= 4):
                        data_[row][col] = 'L'
                        ops += 1

        data = copy.deepcopy(data_)

    return len([seat for seats in data for seat in seats if seat == '#'])


assert seating_process(START) == 37

with open("../inputs/day11.txt") as f: 
    data = f.read()
    print(seating_process(data))