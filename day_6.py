input_file = 'input.txt'

def find_marker(input_file, n):
    fh = open(input_file)
    marker = []
    count = 0
    for line in fh:
        line = line.rstrip()
        for i in line:
            marker.append(i)
            count += 1
            if len(marker) == n:
                if len(marker) == len(set(marker)):
                    break
                else:
                    marker.pop(0)
                    continue
            else:
                continue
                

    return count
  
  first_half_solution = find_marker(input_file, 4)
  second_half_solution = find_marker(input_file, 14)
  print(f'The solution to the first half of the problem is {first_half_solution}, while the solution to the second half is {second_half_solution}.')
