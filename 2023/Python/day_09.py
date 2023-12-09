import pathlib
from datetime import datetime

def main():
    input_file = pathlib.Path().cwd() / 'input.txt'

    with open(input_file, 'r') as f:
        lines = f.readlines()
    puzzle_1, puzzle_2 = 0, 0
    for line in lines:
        line = line.rstrip()
        nums = [int(x) for x in line.split()]
        temporary = []
        puzzle_1 = first_puzzle(nums)
        puzzle_2 += second_puzzle(nums, temporary)
    print(f'Result of the first puzzle: {puzzle_1}')
    print(f'Result of the second puzzle: {puzzle_2}')

def first_puzzle(nums, last_numbers=[]):
    last_line = [] # I make a list out of all the differences to pass to the recursive function

    # when the line is a sequence of all 0s, I sum all the last numbers of every line and return the sum
    if len(set(nums)) == 1 and 0 in nums:
        sum_nums = sum(last_numbers)
        return sum_nums
    else:
        for i in range(len(nums)-1):
            last_line.append((nums[i+1]) - nums[i])
        last_numbers.append(nums[-1])
        return first_puzzle(last_line)

# almost the same as the function used to solve the first puzzle, except I have to find the difference of all the numbers
def second_puzzle(nums, first_numbers):
    last_line = []
    if len(set(nums)) == 1 and 0 in nums:
        first_numbers.append(0)
        first_numbers = first_numbers[::-1]
        difference = 0
        for i in range(len(first_numbers)):
            difference = first_numbers[i] - difference
        return difference
    else:
        
        for i in range(len(nums)-1):
            last_line.append((nums[i+1]) - nums[i])
        first_numbers.append(nums[0])
        return second_puzzle(last_line, first_numbers)

if __name__ == '__main__':
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
