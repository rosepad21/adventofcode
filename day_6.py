input_file = 'input.txt'

def find_marker(input_file, first_half_state=False):
    fh = open(input_file)
    marker = []
    count = 0
    for line in fh:
        line = line.rstrip()
        for i in line:
            marker.append(i)
            count += 1
            if first_half_state:
                if len(marker) == 4:
                    if len(marker) == len(set(marker)): # comparing it to a set to check for duplicates
                        break
                    else:
                        marker.pop(0) # if there are duplicates, we remove the first element in the list
                        continue
                else:
                    continue
            else:
                if len(marker) == 14:
                    if len(marker) == len(set(marker)):
                        break
                    else:
                        marker.pop(0)
                        continue
                else:
                    continue
                

    return count
  
  first_half_solution = find_marker(input_file, True)
  second_half_solution = find_marker(input_file)
  print(f'The solution to the first half of the problem is {first_half_solution}, while the solution to the second half is {second_half_solution}.')
