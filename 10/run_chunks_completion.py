CLOSING_MAPPING = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">"
}
WRONG_SYMBOL_SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
MISSING_SCORE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}
OPENNING_SYMBOLS = set(CLOSING_MAPPING.keys())
CLOSING_SYMBOLS = set(CLOSING_MAPPING.values())

def process_chunk(chunk):
    score = 0
    symbol_stack = []
    for c in chunk:
        if c in OPENNING_SYMBOLS:
            symbol_stack.append(c)
        elif c in CLOSING_SYMBOLS:
            if symbol_stack:
                last_open_symbol = symbol_stack.pop()
                if CLOSING_MAPPING[last_open_symbol] != c:
                    return WRONG_SYMBOL_SCORE[c], score
            else:
                score = score*5 + MISSING_SCORE[CLOSING_MAPPING[c]]
                print("no more symbol")
        else:
            print("unknown characters.")
    while symbol_stack:
        last_open_symbol = symbol_stack.pop()
        score = score*5 + MISSING_SCORE[CLOSING_MAPPING[last_open_symbol]]
    
    return 0, score

scores = []
with open("input") as infile:
    for line in infile:
        _, score = process_chunk(line.strip())
        if score == 0:
            continue
        scores.append(score)

scores = list(sorted(scores))
print(scores[len(scores)//2])
