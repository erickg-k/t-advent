SIGNAL_NUM_LEN_MAPPING = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}

def analyze_signals(signals):
    pattern_sets = [set()] * 10
    len_5_patterns_sets = []
    len_6_patterns_sets = []

    for signal in signals:
        len_pattern = len(signal)
        if len_pattern in SIGNAL_NUM_LEN_MAPPING:
            pattern_sets[SIGNAL_NUM_LEN_MAPPING[len_pattern]] = set(signal)
        elif len_pattern == 5:
            len_5_patterns_sets.append(set(signal))
        elif len_pattern == 6:
            len_6_patterns_sets.append(set(signal))

    patterns = {
        frozenset('a'): (pattern_sets[7] - pattern_sets[1]).pop(),
        frozenset('bd'): pattern_sets[4] - pattern_sets[1],
        frozenset('bdeg'): pattern_sets[8] - pattern_sets[7],
        frozenset('cf'): pattern_sets[1],
    }
    patterns[frozenset('eg')] = patterns[frozenset('bdeg')] - patterns[frozenset('bd')]
    diff_sets = set()
    for sets in len_6_patterns_sets:
        diff_sets = diff_sets.union(pattern_sets[8] - sets)
    patterns[frozenset('dce')] = diff_sets
    patterns[frozenset('d')] = patterns[frozenset('dce')] - patterns[frozenset('cf')] - patterns[frozenset('eg')]
    patterns[frozenset('b')] = patterns[frozenset('bd')] - patterns[frozenset('d')]
    patterns[frozenset('e')] = patterns[frozenset('dce')] - patterns[frozenset('d')] - patterns[frozenset('cf')]
    patterns[frozenset('g')] = patterns[frozenset('bdeg')] - patterns[frozenset('bd')] - patterns[frozenset('e')]
    patterns[frozenset('c')] = patterns[frozenset('dce')] - patterns[frozenset('d')] - patterns[frozenset('e')]
    patterns[frozenset('f')] = patterns[frozenset('cf')] - patterns[frozenset('c')]

    num_patterns = [
        pattern_sets[8] - patterns[frozenset('d')],
        pattern_sets[1],
        pattern_sets[8] - patterns[frozenset('b')] - patterns[frozenset('f')],
        pattern_sets[8] - patterns[frozenset('b')] - patterns[frozenset('e')],
        pattern_sets[1].copy().union(patterns[frozenset('bd')]),
        pattern_sets[8] - patterns[frozenset('c')] - patterns[frozenset('e')],
        pattern_sets[8] - patterns[frozenset('c')],
        pattern_sets[1].copy().union(patterns[frozenset('a')]),
        pattern_sets[8],
        pattern_sets[8] - patterns[frozenset('e')]
    ]
    return [frozenset(p) for p in num_patterns]



def read_input(input_filepath):
    with open(input_filepath) as infile:
        for line in infile:
            signals, digits = line.strip().split("|")
            
            digits = digits.strip().split()
            signals = signals.strip().split()
            yield signals, digits


def reveals(patterns, digits):
    patterns_to_num = {}
    for num, p in enumerate(patterns):
        patterns_to_num[p] = num
    
    num = 0
    for d in digits:
        num = num*10+ patterns_to_num[frozenset(d)]
    return num

def sum_all(signals_digits_iter):
    sums = 0
    for signals, digits in signals_digits_iter:
        patterns = analyze_signals(signals)
        sums += reveals(patterns, digits)
    
    print(sums)
    
def run():
    signals_digits_iter = read_input("input")
    sum_all(signals_digits_iter)

if __name__ == "__main__":
    import timeit
    print(timeit.timeit("run()", number=1000, globals=locals()))
