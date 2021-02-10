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


def adjacent_seats_2(seats: list ,seat: tuple) -> list:
    adj_seats = []
    row, col = seat
    col_max = len(seats[0])
    row_max = len(seats)

    # check same row, left 
    if col != 0:
        for i in range(col-1, -1, -1):
            if seats[row][i] != '.':
                adj_seats.append(seats[row][i])
                break
    # check right
    if col != (col_max-1):
        for i in range(col+1, col_max):
            if seats[row][i] != '.':
                adj_seats.append(seats[row][i])
                break
    # check same col, up/before
    if row > 0:
        for i in range(row-1, -1, -1):
            if seats[i][col] != '.':
                adj_seats.append(seats[i][col])
                break
    # down
    if row < (row_max-1):
        for i in range(row+1, row_max):
            if seats[i][col] != '.':
                adj_seats.append(seats[i][col])
                break
    # check diagonals
    # right up
    rest_col = col_max - col -1
    rest_row = row
    for i in range(1, (min(rest_col, rest_row) + 1)):
        if seats[row-i][col+i] != '.':
            adj_seats.append(seats[row-i][col+i])
            break
    # left down
    rest_col = col
    rest_row = row_max - row -1
    for i in range(1, (min(rest_col, rest_row) + 1)):
        if seats[row+i][col-i] != '.':
            adj_seats.append(seats[row+i][col-i])
            break
    # left up
    rest_col = col
    rest_row = row
    for i in range(1, (min(rest_col, rest_row) + 1)):
        if seats[row-i][col-i] != '.':
            adj_seats.append(seats[row-i][col-i])
            break
    # right down
    rest_col = col_max - col -1
    rest_row = row_max - row -1
    for i in range(1, (min(rest_col, rest_row) + 1)):
        if seats[row+i][col+i] != '.':
            adj_seats.append(seats[row+i][col+i])
            break

    return adj_seats


def seating_process_2(raw:str) -> list:
    
    data = read_input(raw)
    data_ = copy.deepcopy(data)
    ops = 1
    while ops != 0:
        ops = 0
        for row in range(len(data)):
            for col in range(len(data[0])):
                val = data[row][col]
                if val != '.':
                    adj_seats = adjacent_seats_2(data, (row,col))
                    assert len(adj_seats) <= 8 and len(adj_seats) >= 3
                    if (val == 'L' and len([seat for seat in adj_seats if seat == '#']) == 0):
                        data_[row][col] = '#'
                        ops += 1
                    elif (val == '#' and len([seat for seat in adj_seats if seat == '#']) >= 5):
                        data_[row][col] = 'L'
                        ops += 1

        data = copy.deepcopy(data_)

    return len([seat for seats in data for seat in seats if seat == '#'])


assert seating_process(START) == 37

assert seating_process_2(START) == 26

with open("../inputs/day11.txt") as f: 
    data = f.read()
    #print(seating_process(data))
    print(seating_process_2(data))