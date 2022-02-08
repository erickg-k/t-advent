from collections import Counter

def read_seq(filepath):
    with open(filepath, "r") as infile:
        template = infile.readline().strip()
        seq_map = {}

        for line in infile:
            line = line.strip()
            if not line: continue
            seq, ins = line.split("->")

            seq_map[seq.strip()] = ins.strip()

        return template, seq_map

def step(seq, seq_map):
    res = []
    for i in range(len(seq)-1):
        slice = seq[i:i+2]
        if slice in seq_map:
            res.append(slice[0] + seq_map[slice])
        else:
            res.append(slice[0])
    res.append(seq[-1])
    return "".join(res)

def polymer(num_steps, template, seq_map):
    for _ in range(num_steps):
        template = step(template, seq_map)
    return template

def diff_significant_token(sequence):
    cnt = Counter(sequence)
    counts = list(sorted(cnt.values()))
    return counts[-1] - counts[0]

if __name__ == "__main__":
    template, seq_map = read_seq("test")
    # print(template, seq_map)
    sequence = polymer(10, template, seq_map)
    diff = diff_significant_token(sequence)
    print(diff)