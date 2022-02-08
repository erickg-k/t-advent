def process_sum(digit):
    sum_1_4_7_8 = 0
    if len(digit) in {2, 3, 4, 7}:
        sum_1_4_7_8 += 1

    return sum_1_4_7_8 
    
def read_digits(input_filepath):
    with open(input_filepath) as infile:
        for line in infile:
            signals, digits = line.strip().split("|")
            
            digits = digits.strip().split()
            yield digits

def sum_digits(digits_iter):
    sum_simple = 0
    for digits in digits_iter:
        sum_simple += sum(map(process_sum, digits))
    
    print(sum_simple)

if __name__ == "__main__":
    digits_iter = read_digits("input")
    sum_digits(digits_iter)
    