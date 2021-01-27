INPUT = ["..##.......",
         "#...#...#..",
         ".#....#..#.",
         "..#.#...#.#",
         ".#...##..#.",
         "..#.##.....",
         ".#.#.#....#",
         ".#........#",
         "#.##...#...",
         "#...##....#",
         ".#..#...#.#"]

SLOPES = [(1,1), (3,1), (5,1), (7,1), (1,2)]

def traverse_forrest(inp, steps_right=3, steps_down=1):
    # (row, col)
    start = (0,0)
    trees = 0

    while start[0] < (len(inp) - 1):
        row = start[0] + steps_down
        col = start[1] + steps_right
        if col > (len(inp[row]) - 1):
            col = col - len(inp[row])
        start = (row, col)
        if inp[row][col] == '#':
            trees += 1

    return trees

assert traverse_forrest(inp=INPUT) == 7

def multiply_trees(input, slopes):
    trees = []
    for slope in slopes:
        trees.append(traverse_forrest(inp=input, steps_right=slope[0], steps_down=slope[1]))
    mul = 1
    for tree in trees:
        mul *= tree
    return mul

assert multiply_trees(input=INPUT, slopes=SLOPES) == 336

with open('../inputs/day03.txt', 'r') as f:
    data = [l.strip() for l in f]
    print(multiply_trees(input=data, slopes=SLOPES))
