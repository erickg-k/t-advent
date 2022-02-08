PADDING_VAL = 9999999999

heightmap = [[]]

with open("input") as infile:
    for line in infile:
        nums = list(map(int, list(line.strip())))
        heightmap.append([PADDING_VAL] + nums + [PADDING_VAL])

max_rows = len(heightmap)
max_columns = len(heightmap[-1]) - 1
heightmap[0] = [PADDING_VAL] * len(heightmap[-1])
heightmap.append([PADDING_VAL] * len(heightmap[-1]))

risk_level = 0
for r in range(1, max_rows):
    for c in range(1, max_columns):
        if (heightmap[r][c] < heightmap[r][c+1] and 
            heightmap[r][c] < heightmap[r][c-1] and
            heightmap[r][c] < heightmap[r+1][c] and
            heightmap[r][c] < heightmap[r-1][c]):
            # print(r, c, heightmap[r][c])
            risk_level += 1 + heightmap[r][c]

print(risk_level)