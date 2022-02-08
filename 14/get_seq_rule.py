from collections import Counter, defaultdict

def read_seq(filepath):
    template = ""
    seq_meta = {}
    seq_mapping = {}

    with open(filepath, "r") as infile:
        template = infile.readline().strip()
        seqs = []
        seq_mapping = {}

        for line in infile:
            line = line.strip()
            if not line: continue
            seq, ins = line.split("->")
            seq = seq.strip()
            ins = ins.strip()

            seqs.append(seq)
            seq_mapping[seq] = [seq[0] + ins, ins + seq[1]]

    for seq in seqs:
        # always true: if next_seq in seq_mapping
        next_seqs = [next_seq for next_seq in seq_mapping[seq]]
        seq_meta[seq] = {
            "chars": dict(Counter(seq)),
            "next_seqs": next_seqs,
        }
    

    return template, seq_meta

def prepare(template):
    cnt_seqs = defaultdict(int)
    cnt_chars = defaultdict(int)
    for idx in range(len(template)-1):
        seq = template[idx:idx+2]
        cnt_seqs[seq] += 1
        cnt_chars[template[idx]] += 1
    cnt_chars[template[-1]] += 1
    return cnt_seqs, cnt_chars

def step(cnt_seqs, cnt_chars, seq_meta):
    next_cnt_seqs = defaultdict(int)
    for seq, cnt in cnt_seqs.items():
        for next_seq in seq_meta[seq]["next_seqs"]:
            next_cnt_seqs[next_seq] += cnt
        cnt_chars[seq_meta[seq]["next_seqs"][0][1]] += cnt
    return next_cnt_seqs, cnt_chars

def polymer(num_steps, template, seq_meta):
    cnt_seqs, cnt_chars = prepare(template)
    for _ in range(num_steps):
        cnt_seqs, cnt_chars = step(cnt_seqs, cnt_chars, seq_meta)
    
    # cnt_chars = defaultdict(int)
    # for seq, cnt in cnt_seqs.items():
    #     chars = seq_meta[seq]["chars"]
    #     for char, cnt_char in chars.items():
    #         cnt_chars[char] += cnt_char * cnt
    return cnt_chars

def diff_significant_token(cnt_chars):
    cnt = Counter(cnt_chars)
    counts = list(sorted(cnt.values()))
    return (counts[-1] - counts[0])

if __name__ == "__main__":
    template, seq_meta = read_seq("input")
    # print(template)
    # pprint(seq_meta)
    # prepare(template)
    cnt_chars = polymer(40, template, seq_meta)
    diff = diff_significant_token(cnt_chars)
    print(diff)