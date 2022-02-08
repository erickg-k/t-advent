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
OPENNING_SYMBOLS = set(CLOSING_MAPPING.keys())
CLOSING_SYMBOLS = set(CLOSING_MAPPING.values())

def process_chunk(chunk):
    symbol_stack = []
    for c in chunk:
        if c in OPENNING_SYMBOLS:
            symbol_stack.append(c)
        elif c in CLOSING_SYMBOLS:
            if symbol_stack:
                last_open_symbol = symbol_stack.pop()
                if CLOSING_MAPPING[last_open_symbol] != c:
                    return WRONG_SYMBOL_SCORE[c]
            else:
                print("no more symbol")
        else:
            print("unknown characters.")
    
    return 0

scores = 0
with open("input") as infile:
    for line in infile:
        scores += process_chunk(line.strip())

print(scores)
