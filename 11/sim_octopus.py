PADDING_VAL = -100000000

DIRS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]
MAX_GRID_SIZE = 11

def dfs(lights, i, j):
    if i < 1 or i >= MAX_GRID_SIZE or j < 1 or j >= MAX_GRID_SIZE or lights[i][j] >= 10:
        return

    lights[i][j] += 1
    if lights[i][j] >= 10:
        for di, dj in DIRS:
            dfs(lights, i+di, j+dj)

def step(lights):
    num_flashes = 0

    for i in range(1, MAX_GRID_SIZE):
        for j in range(1, MAX_GRID_SIZE):
            dfs(lights, i, j)
    
    for i in range(1, MAX_GRID_SIZE):
        for j in range(1, MAX_GRID_SIZE):
            if lights[i][j] >= 10:
                lights[i][j] = 0
                num_flashes += 1

    # print_lights(lights)
    return num_flashes


def print_lights(lights):
    for i in range(1, MAX_GRID_SIZE):
        for j in range(1, MAX_GRID_SIZE):
            print(lights[i][j], end="")
        print()
    print()

octopusmap = [[]]

with open("input") as infile:
    for line in infile:
        nums = list(map(int, list(line.strip())))
        octopusmap.append([PADDING_VAL] + nums + [PADDING_VAL])

octopusmap[0] = [PADDING_VAL] * len(octopusmap[-1])
octopusmap.append([PADDING_VAL] * len(octopusmap[-1]))

# print_lights(octopusmap)
# sum_flashes = 0
# for _ in range(100):
#     sum_flashes += step(octopusmap)

# print(sum_flashes)

idx = 0
while True:
    idx += 1
    if step(octopusmap) >= 100:
        print(idx)
        exit()