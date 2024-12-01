import pathlib
from datetime import datetime

def main():
    puzzle_1, puzzle_2 = 0, 0
    list_1, list_2 = [], []
    input_file = pathlib.Path().cwd() / 'input.txt'

    with open(input_file, 'r') as fh:
        lines = fh.readlines()
        list_1, list_2 = create_lists(lines)
    puzzle_1 = first_puzzle(list_1, list_2)
    puzzle_2 = second_puzzle(list_1, list_2)

    print(f'Result of the first puzzle: {puzzle_1}')
    print(f'Result of the second puzzle: {puzzle_2}')

def first_puzzle(list_1, list_2):
    total = 0
    for x in range(len(list_1)):
        total += abs(list_1[x] - list_2[x])
    return total

def second_puzzle(list_1, list_2):
    count = {}
    total = 0
    for x in range(len(list_2)):
        count[list_2[x]] = count.get(list_2[x], 0) + 1
    for y in range(len(list_1)):
        total += list_1[y] * count.get(list_1[y], 0)
    return total

def create_lists(lines):
    list_1, list_2 = [], []
    for line in lines:
        line = line.split()
        list_1.append(int(line[0]))
        list_2.append(int(line[1]))
    list_1.sort()
    list_2.sort()
    return [list_1, list_2]

if __name__ == '__main__':
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
