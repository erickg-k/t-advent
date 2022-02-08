from collections import deque

cnt_inc = 0
q = deque(maxlen=3)

def _read_int(line: str) -> int:
    return int(line.strip())

with open('input.txt') as infile:
    try:
        for _ in range(3):
            q.append(_read_int(next(infile)))
    except:
        pass
    cur_window = num_window = sum(q)

    for line in infile:
        num = _read_int(line)
        q.append(num)

        cur_window = sum(q)
        if cur_window > num_window:
            cnt_inc += 1

        num_window = cur_window

print(cnt_inc)