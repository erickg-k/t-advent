forwarded = 0
depth = 0
aim = 0

with open('input.txt') as infile:
    for line in infile:
        line = line.strip()
        if not line: continue
        direction, num_movement = line.split(' ')
        num_movement = int(num_movement)

        if direction == "forward":
            forwarded += num_movement
            depth += aim * num_movement
        elif direction == "down":
            aim += num_movement
        elif direction == "up":
            aim += -num_movement
        else:
            pass

print(forwarded * depth)