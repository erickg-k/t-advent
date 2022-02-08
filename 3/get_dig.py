import numpy as np

matrix = []

with open('input') as infile:
    for line in infile:
        nums = np.array(list(map(int, list(line.strip()))), dtype=np.bool_)
        matrix.append(nums)

matrix = np.array(matrix)
size = matrix.shape[0]
sums = np.sum(matrix, axis=0)

digits = [s > size - s for s in sums]
gamma_digits = "".join(map(str, map(int, digits)))
epsilon_digits = "".join(map(str,map(int, map(lambda x: not x, digits))))

gamma = int(gamma_digits, 2)
epsilon = int(epsilon_digits, 2)

print(gamma * epsilon)