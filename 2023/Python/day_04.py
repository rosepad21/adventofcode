import pathlib

doubles = {}

def main():
    input_file = pathlib.Path().cwd() / 'input.txt'

    with open(input_file, 'r') as f:
        lines = f.readlines()
    puzzle_1 = 0
    puzzle_2 = 0
    num_line = 1
    set_doubles(len(lines))
    for line in lines:
        line = line.rstrip()
        puzzle_1 += first_puzzle(line, num_line)
        num_line += 1
    puzzle_2 = second_puzzle()
    print(f'Result of the first puzzle: {puzzle_1}')
    print(f'Result of the second puzzle: {puzzle_2}')

def first_puzzle(line, num_line):
    length = split_first(line)
    add_scratchcards(num_line, length)    
    if length == 0:
        return 0
    else:
        return 2**(length-1)

def second_puzzle():
    the_sum = 0
    for v in doubles.values():
        the_sum += v
    return the_sum

def split_first(line):
    line1 = set([x for x in line[line.find(':') + 2:line.find('|')].split(' ') if x != ''])
    line2 = set([x for x in line[line.find('|') + 2:].split(' ') if x != ''])
    return len(line1 & line2)

def set_doubles(length):
    for i in range(1, length+1):
        doubles[i] = 1

def add_scratchcards(num_line, length):
    temp = doubles.get(num_line, 1)
    while temp > 0:
        for i in range(1, length+1):
            doubles[num_line+i] = doubles.get(num_line+i, 1) + 1
        temp -= 1

if __name__ == '__main__':
    main()
