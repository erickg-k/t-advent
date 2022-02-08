from collections import defaultdict


def read_caves(filepath):
    caves = defaultdict(list)
    with open(filepath, "r") as infile:
        for line in infile:
            begin, end = line.strip().split("-")

            caves[begin].append(end)
            caves[end].append(begin)
    
    return caves

def bfs(caves):
    paths = []
    
    stack = [("start", ["start"])]
    while stack:
        elem, path = stack.pop()
        for next_element in caves[elem]:
            if next_element == "end":
                paths.append(path + [next_element])
            elif next_element.isupper():
                stack.append((next_element, path + [next_element]))
            else:
                if next_element in path:
                    continue 
                stack.append((next_element, path + [next_element]))
            
    return paths


if __name__ == "__main__":
    C = read_caves("input")
    paths = bfs(C)
    print(paths, len(paths))