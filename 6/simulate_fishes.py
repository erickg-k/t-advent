NEW_FISH_STATE = 8
REFRESHED_FISH_STATE = 6


def read_fishes(input_filepath):
    inputs = open(input_filepath).read().strip()
    return list(map(int, inputs.split(",")))

def simulate_fishes(raw_fishes, days):
    fishes = [0] * 9
    for fish in raw_fishes:
        fishes[fish] += 1

    cnt_new_fishes = fishes[0]
    for day in range(NEW_FISH_STATE, 0, -1):
        fishes[day-1] = fishes[day]
    fishes[NEW_FISH_STATE] = cnt_new_fishes
    fishes[REFRESHED_FISH_STATE] += cnt_new_fishes

    print(sum(fishes))
    

if __name__ == "__main__":
    raw_fishes = read_fishes("input")
    simulate_fishes(raw_fishes, 256)
