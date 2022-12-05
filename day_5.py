input_file = 'input.txt'

# implementing functions to make the code a bit more readable
def parse_crate(input_file):
    fh = open(input_file)
    automatic_crates = [[] for _ in range(9)] 
    for line in fh:
        if not line.startswith('move') and line:
            line = line.replace(']', ' ')
            line = line.replace('[', ' ')
            for i in range(len(line)):
                if line[i].isalpha(): # checking for letters so to exclude spaces
                    automatic_crates[i//4].append(line[i])
                else:
                    continue
        else:
            break
    for crate in automatic_crates: # since we parsed from above, we reverse the crates
        crate.reverse()

    return automatic_crates


def move_crates(crates, input_file, second_half=False): 
    fh = open(input_file)
    for line in fh:
        line = line.strip()

        if not line.startswith('move'):
            continue
        else:
            moves = int(line[line.find(' ', 3)+1:line.find(' ', 5)]) # moves to do
            froms = int(line[line.find(' ', 9)+1:line.find(' ', 13)]) # from which crate
            str_to = int(line[line.find(' ', 15)+1:]) # to which crate
            from_crate = crates[froms-1]
            to_crate = crates[str_to-1]
         
            while moves > 0:
                for _ in range(moves):
                    if second_half:
                    # for the second half of the problem, we take the crates starting from the one in the lowest position
                    # since they have to be moved all together
                        to_crate.append(from_crate.pop(-moves)) 
                        moves -= 1
                    else: 
                    # for the first half of the problem, we move the last crate from each pile
                        to_crate.append(from_crate.pop(-1))
                        moves -= 1
        
    return crates



#first half solution
automatic_crates_first = parse_crate(input_file)
first_half_crates = move_crates(automatic_crates_first, input_file)
first_solution = ''
for crate in first_half_crates:
    first_solution += str(crate[-1])

# second half solution:
automatic_crates_second = parse_crate(input_file)
second_half_crates = move_crates(automatic_crates_second, input_file, True)
second_solution = ''
for crate in second_half_crates:
    second_solution += str(crate[-1])

print(f"The solution to the first problem is {first_solution}, and the solution to the second one is {second_solution}")



