def print_paper(paper, dimension):
    print(dimension)
    for y in range(dimension[0]):
        for x in range(dimension[1]):
            dot = paper[y][x]
            if dot:
                print('#', end="")
            else:
                print('.', end="")
        print()
    print()

def count_visilble(paper, dimension):
    cnt = 0
    for y in range(dimension[0]):
        for x in range(dimension[1]):
            dot = paper[y][x]
            if dot:
                cnt += 1
    return cnt

def read_paper(filepath):
    max_x, max_y = 0, 0
    pairs = []
    foldings = []
    with open(filepath, "r") as infile:
        for line in infile:
            line = line.strip()
            if line.startswith("fold along "):
                line = line.removeprefix("fold along ")
                dir, amount = line.split("=")
                foldings.append((dir.strip(), int(amount)))
            elif line:
                x, y = line.split(",")
                x = int(x)
                y = int(y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)
                pairs.append((x, y))

    paper = []
    max_y+=1
    max_x+=1
    
    for _ in range(max_y):
        paper.append([False] * max_x)
    for pair in pairs:
        x, y = pair
        # print_paper(paper)
        paper[y][x] = True
        
    return paper, foldings, (max_y, max_x)

def fold_papers(paper, foldings, dimension):
    for axis, cut in foldings:
        print(axis, cut)
        if axis == "y":
            for y in range(cut):
                folded_y = dimension[0] - y - 1
                bottom_slice = paper[folded_y]
                for x in range(dimension[1]):
                    paper[y][x] = paper[y][x] or bottom_slice[x]
            dimension = (cut, dimension[1])
        else:
                # folded_x = dimension[1] - x -1
                # # print(dimension[1], cut, x, folded_x)
            for y in range(dimension[0]):
                right_slice = paper[y][cut:]
                try:
                    for x in range(cut):
                        paper[y][x] = paper[y][x] or right_slice[-1-x]
                        # print(cut, -1-x, len(right_slice))
                except:
                    pass
            dimension = (dimension[0], cut)
        # print_paper(paper, dimension)
    return paper, dimension

    

if __name__ == "__main__":
    paper, foldings, dimension = read_paper("input")
    # print_paper(paper, dimension)
    print(dimension)
    # exit()
    # paper, dimension = fold_papers(paper, [foldings[0]], dimension)
    # paper, dimension = fold_papers(paper, foldings, dimension)

    print_paper(paper, dimension)
    print(count_visilble(paper, dimension))