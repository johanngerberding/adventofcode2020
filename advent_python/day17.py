import collections 
import itertools 

INPUT = """#......#
##.#..#.
#.#.###.
.##.....
.##.#...
##.#....
#####.#.
##.#.###"""

TEST = """.#.
..#
###"""


def part_1(raw: str) -> int:
    grid = collections.defaultdict(int)

    for x, row in enumerate(raw.split('\n')):
        for y, val in enumerate(row):
            if val == '#':
                grid[(x,y,0)] = 1

    for _ in range(6):
        # create a new neighbors dict
        neighbors = collections.defaultdict(int)
        # iterate over active cubes
        for coord, val in grid.items():
            if val:
                # itertools product -> cartesian product
                for delta in itertools.product([-1, 0, 1], repeat=3):
                    # for any delta thats not (0,0,0)
                    if any(delta):
                        neighbors[tuple(map(sum, zip(coord, delta)))] += 1



        _grid = collections.defaultdict(int)

        for coords, val in neighbors.items():
            if val == 3 or (grid[coords] and val == 2):
                _grid[coords] = 1
        
        grid = _grid

    return len(grid)


def part_2(raw: str) -> int:
    grid = collections.defaultdict(int)

    for x, row in enumerate(raw.split('\n')):
        for y, val in enumerate(row):
            if val == '#':
                grid[(x,y,0,0)] = 1

    for _ in range(6):
        # create a new neighbors dict
        neighbors = collections.defaultdict(int)
        # iterate over active cubes
        for coord, val in grid.items():
            if val:
                # itertools product -> cartesian product
                for delta in itertools.product([-1, 0, 1], repeat=4):
                    # for any delta thats not (0,0,0,0)
                    if any(delta):
                        neighbors[tuple(map(sum, zip(coord, delta)))] += 1



        _grid = collections.defaultdict(int)

        for coords, val in neighbors.items():
            if val == 3 or (grid[coords] and val == 2):
                _grid[coords] = 1
        
        grid = _grid

    return len(grid)

print(f"part 1: {part_1(INPUT)}")
print(f"part 2: {part_2(INPUT)}")