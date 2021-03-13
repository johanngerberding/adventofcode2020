import numpy as np


class Tile:
    def __init__(self, num: int, tile: list):
        self.num = num
        self.tile = tile 
        self.borders = self.create_borders()


    def rotate(self, k=1):
        """Rotate tile k times by 90 degrees"""
        self.tile = np.rot90(self.tile, k)
        self.borders = self.create_borders()

    
    def flip(self, axis=0):
        self.tile = np.flip(self.tile, axis=axis)
        self.borders = self.create_borders()
        

    def create_borders(self) -> list:
        """Return boarder"""
        n = self.tile[0]
        s = self.tile[-1]
        e = [el[-1] for el in self.tile]
        w = [el[0] for el in self.tile]
        assert len(n) == len(s) == len(e) == len(w) == 10
        return [n, e, s, w]
        

    def print_tile(self):
        for line in self.tile:
            print(line)

    def match_tile(self, tile_2) -> list:
        bord = self.borders
        borders_1 = bord + [list(reversed(b)) for b in bord]
        borders_2 = tile_2.borders + [list(reversed(b)) for b in tile_2.borders]
        assert len(borders_1) == 8
        matches = []
        for i, border in enumerate(borders_1):
            for j, border_ in enumerate(borders_2):
                if border == border_:
                    matches.append((i,j))

        return matches



def parse(raw: str):
    data = raw.strip().split("\n\n")
    data = [tile.splitlines() for tile in data]
    tiles = []
    for el in data:
        num = int(el[0].split(" ")[1][:-1])
        tile = el[1:]
        tile = [list(row) for row in tile]
        tiles.append(Tile(num=num, tile=tile))
    
    return tiles


TEST = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""


tiles = parse(TEST)

res = {}
while len(res) < len(tiles):
    test = tiles.pop(0)
    matches = []
    for tile in tiles:
        m = test.match_tile(tile)
        if len(m) > 0:
            matches.append(tile.num)
    res[test.num] = matches
    tiles.append(test)

corners = [k for k, v in res.items() if len(v) == 2]
print(corners)
print(np.prod(corners))

with open('../inputs/day20.txt') as f: 
    tiles = parse(f.read())
    res = {}
    while len(res) < len(tiles):
        test = tiles.pop(0)
        matches = []
        for tile in tiles:
            m = test.match_tile(tile)
            if len(m) > 0:
                matches.append(tile.num)
        res[test.num] = matches
        tiles.append(test)

    corners = [k for k, v in res.items() if len(v) == 2]
    print(corners)
    print(np.prod(corners))