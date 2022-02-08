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
    
    stack = [("start", ["start"], False)]
    while stack:
        elem, path, a_small_cave_visit_twice= stack.pop()
        for next_element in caves[elem]:
            if next_element == "start":
                continue
            elif next_element == "end":
                paths.append(path + [next_element])
            elif next_element.isupper():
                stack.append((next_element, path + [next_element], a_small_cave_visit_twice))
            else:
                if next_element in path:
                    if not a_small_cave_visit_twice:
                        stack.append((next_element, path + [next_element], True))
                    continue
                stack.append((next_element, path + [next_element], a_small_cave_visit_twice))

    return paths


if __name__ == "__main__":
    C = read_caves("input")
    paths = bfs(C)
    print(paths, len(paths))

    # sorted_pathes = list(sorted([",".join(p) for p in paths]))
    # for p in sorted_pathes:
    #     print(p)