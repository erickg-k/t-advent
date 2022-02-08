import numpy as np

def deduct_number_by_matrix(raw_matrix, select_more_1):
    matrix = raw_matrix.copy()
    num_bit = 0

    while matrix.shape[0] > 1:
        sum_1 = np.sum(matrix[:,num_bit], axis=0)
        size = matrix.shape[0]
        sum_0 = size - sum_1

        if select_more_1:
            if sum_1 >= sum_0:
                selection = matrix[:,num_bit]
            else:
                selection = ~matrix[:,num_bit]
        else:
            if sum_0 > sum_1:
                selection = matrix[:,num_bit]
            else:
                selection = ~matrix[:,num_bit]

        matrix = matrix[selection]
        num_bit += 1
        # print(sum_1, sum_0, num_bit, matrix)
    
    return int("".join(map(str, map(int, matrix[0]))), 2)

def read_matrix():
    matrix = []

    with open('input') as infile:
        for line in infile:
            nums = np.array(list(map(int, list(line.strip()))), dtype=np.bool_)
            matrix.append(nums)

    return np.array(matrix)

matrix = read_matrix()
sums = np.sum(matrix, axis=0)

oxygen = deduct_number_by_matrix(matrix, True)
co2 = deduct_number_by_matrix(matrix, False)

print(oxygen, co2, oxygen * co2)
