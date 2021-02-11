TEST = """F10
N3
F7
R90
F11"""



DIRECTIONS = ['E', 'S', 'W', 'N']

class Ship:
    def __init__(self):
        self.direction = 0
        self.north = 0
        self.east = 0
    
    def move(self, instruction: tuple):
        if instruction[0] == 'E':
            self.east += instruction[1]
        elif instruction[0] == 'W':
            self.east -= instruction[1]
        elif instruction[0] == 'N':
            self.north += instruction[1]
        elif instruction[0] == 'S':
            self.north -= instruction[1]

        # go forward in direction we already have
        elif instruction[0] == 'F':
            if self.direction % 4 == 0:
                self.east += instruction[1]
            elif self.direction % 4 == 1:
                self.north -= instruction[1]
            elif self.direction % 4 == 2:
                self.east -= instruction[1]
            elif self.direction % 4 == 3:
                self.north += instruction[1] 
        # direction change [E, S, W, N]
        elif (instruction[0] == 'L' or instruction[0] == 'R'):
            degree = instruction[1] // 90
            if instruction[0] == 'L':
                self.direction += degree * 3
            else: 
                self.direction += degree * 1
    
    def get_direction(self):
        return DIRECTIONS[self.direction % 4]
    
    def get_manhattan_distance(self):
        return abs(self.east) + abs(self.north)


data = [line.strip() for line in TEST.splitlines()]
data = [(line[:1], int(line[1:])) for line in data]
ship = Ship()
for mv in data:
    ship.move(mv)

assert ship.get_manhattan_distance() == 25


with open("../inputs/day12.txt") as f: 
    data = f.read()
    data = [line.strip() for line in data.splitlines()]
    data = [(line[:1], int(line[1:])) for line in data]
    ship = Ship()
    for mv in data:
        ship.move(mv)
    print(ship.get_manhattan_distance())
