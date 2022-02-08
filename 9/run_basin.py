import heapq
from functools import reduce

PADDING_VAL = 9

DIRS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

def dfs(heights, r, c):
    if heights[r][c] == PADDING_VAL:
        return 0
    
    counts = 1
    heights[r][c] = PADDING_VAL
    for dr, dc in DIRS:
        counts += dfs(heights, r+dr, c+dc)

    return counts

heightmap = [[]]

with open("input") as infile:
    for line in infile:
        nums = list(map(int, list(line.strip())))
        heightmap.append([PADDING_VAL] + nums + [PADDING_VAL])

max_rows = len(heightmap)
max_columns = len(heightmap[-1]) - 1
heightmap[0] = [PADDING_VAL] * len(heightmap[-1])
heightmap.append([PADDING_VAL] * len(heightmap[-1]))

basins = []
for r in range(1, max_rows):
    for c in range(1, max_columns):
        if heightmap[r][c] != PADDING_VAL:
            val = dfs(heightmap, r, c)
            # print(f"{val}, {r}, {c}")
            if len(basins) < 3:
                heapq.heappush(basins, val)
            else:
                heapq.heappushpop(basins, val)

print(reduce(lambda a, b: a * b, basins, 1))