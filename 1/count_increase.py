cnt_inc = 0

with open('input.txt') as infile:
    cur_num = int(next(infile).strip())

    for line in infile:
        num = int(line.strip())

        if num > cur_num:
            cnt_inc += 1

        cur_num = num

print(cnt_inc)