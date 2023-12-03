import pathlib

positions = {} # I use a dictionary to track whether positions have a symbol or not, by mapping a tuple with indexes to a boolean
numbers = {} # Same as the positions dictionary, I map a tuple of indexes to numbers to use in the second puzzle
stars = set()

def main():
    input_file = pathlib.Path().cwd() / 'input.txt'

    with open(input_file, 'r') as f:
        lines = f.readlines()

    the_sum = 0
    gears = 0
    num_line = 0

    for line in lines:
        line = line.rstrip()
        number = ''
        check = False
        start_idx, end_idx = 0, 0

        for i in range(len(line)):
            
            if line[i] == '.':
                positions[(num_line, i)] = positions.get((num_line, i), False)
                if number != '':
                    end_idx = i
                    if num_line+1 < len(lines):
                        check = dfs(start_idx, end_idx, num_line, lines[num_line+1])
                    else:
                        check = dfs(start_idx, end_idx, num_line)
                    if check:
                        the_sum += int(number)
                        check = False
                    for x in range(start_idx, i):
                        numbers[(num_line, x)] = numbers.get((num_line, x), int(number))
                    number = ''
                    
            elif line[i].isdigit():
                positions[(num_line, i)] = positions.get((num_line, i), False)
                if number == '':
                    start_idx = i
                number += line[i]
                if i+1 == len(line):
                    if (num_line + 1) < len(lines):
                        check = dfs(start_idx, i, num_line, lines[num_line+1])
                    else:
                        check = dfs(start_idx, i, num_line)
                    
                    for x in range(start_idx, i+1):
                        numbers[(num_line, x)] = numbers.get((num_line, x), int(number))
                    if check:
                        the_sum += int(number)
                        number = ''
                      
            else:
                positions[(num_line, i)] = positions.get((num_line, i), True)
                if line[i] == '*':
                    stars.add((num_line, i))
                if number != '':
                    # since I found a symbol, I'm sure the number has to be counted towards our sum
                    for x in range(start_idx, i):
                        numbers[(num_line, x)] = numbers.get((num_line, x), int(number))
                    the_sum += int(number)
                    check = False
                    number = ''
                        
        num_line += 1
    
    for x in stars:
        gears += star(x[0], x[1])
    print(f'Result of the first puzzle: {the_sum}')
    print(f'Result of the second puzzle: {gears}')

# Helper function that returns a boolean to check whether a number has adjacent symbols
def dfs(start_idx, end_idx, idx, next_line=''):
    check = set()
    if idx == 0:
        print(start_idx, end_idx)
    if start_idx != 0:
        start_idx -= 1
    for i in range(start_idx, end_idx+1):
        check.add(positions.get((idx-1, i)))
        check.add(positions.get((idx, i)))
        if next_line != '':
            if not next_line[i].isdigit() and not next_line[i] == '.':
                positions[(idx+1, i)] = positions.get((idx+1, i), True)
                check.add(True)
            
            else:
                positions[(idx+1, i)] = positions.get((idx+1, i), False)
                check.add(False)
    return True in check

def star(i, j):
    nums = []
    counter = i-1
    # Since I mapped the whole range of indexes for each number, it's hard to detect whether it's the same number or a different one
    # That's why I set a flag: if there's a dot or a symbol between two digits, the flag is set to False, and I add the number to my list
    # If the flag is set to True, instead, it means it's the same number I already found
    flag = False
    to_compare = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
    for x in to_compare:
        if counter != x[0]:
            counter = x[0]
            flag = False
        
        res = numbers.get(x, -1)
        if res != -1 and not flag:
            flag = True
            nums.append(res)
        elif res == -1 and flag:
            flag = False
        
    result = [x for x in nums if x > 0]
    
    if len(result) != 2:
        return 0
    else:
        return result[0] * result[1]

if __name__ == '__main__':
    main()
