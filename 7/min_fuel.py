from functools import reduce


def read_crabs(input_filepath):
    inputs = open(input_filepath).read().strip()
    return list(map(int, inputs.split(",")))

def find_depth(depth):
    min_depth = min(depth)
    max_depth = max(depth)

    min_fuel = 100000000000000000
    for d in range(min_depth, max_depth+1):
        min_fuel = min(min_fuel, reduce(lambda s, x: s + abs(x - d), depth, 0))

    print(min_fuel)
    

def find_depth_with_weight(depth):
    min_depth = min(depth)
    max_depth = max(depth)
    weights = [0]
    for _ in range(min_depth, max_depth+1):
        weights.append(weights[-1] + len(weights))

    min_fuel = 100000000000000000
    for d in range(min_depth, max_depth+1):
        min_fuel = min(min_fuel, reduce(lambda s, x: s + weights[abs(x - d)], depth, 0))

    print(min_fuel)
    


if __name__ == "__main__":
    depth = read_crabs("input")
    find_depth_with_weight(depth)
