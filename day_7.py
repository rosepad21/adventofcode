import re

input_file = ('input.txt')

def find_size_directory(input_file, second_half=False):
    file_sizes = {'start' : 0} # creating a dictionary to store paths and file sizes
    positions = ['start'] # a list to track the directory we are in
    
    fh = open(input_file)
    for line in fh:    
        line = line.rstrip()
                
        if re.search('[0-9]', line):
            num = int(re.findall("([0-9]+)", line)[0])
            path = ''
            for position in positions:
                path += '/' + position # we create a directory path with all the positions in the list
                if not path in file_sizes:
                    file_sizes[path] = 0 # if the path is not in the dictionary, we add it
                file_sizes[path] += num # and then we add the file size to that path
            # being it a loop, the file size gets added to all the sub-directories as well
        elif line == '$ cd ..':
            positions.pop() # if we move up the directories, we remove the last one from the list
        elif line.startswith('$ cd') and '/' not in line:
            new_position = re.findall('([a-z]+)', line)[-1]
            positions.append(new_position) # if we move down the directories, we add the new one to the list             
            if new_position not in file_sizes.keys(): # and if it's not already in the dictionary, we add it there as well
                file_sizes[new_position] = 0
        else:
            continue
    
    
    if not second_half: # for the first half of the problem
        count = 0
        for value in file_sizes.values():
            if value <= 100000:
                count += value
            else:
                continue
        
        return count
    
    else:
        vals = [] # creating a list of all the values in the dictionary
        size_needed = 70000000
        for value in file_sizes.values():
            vals.append(value)
        sorted_vals = sorted(vals)
        new_size = size_needed - sorted_vals[-1] # the starting size would be the size_needed minus the largest size in the list
        
        for j in sorted_vals: # to find the smallest value that would free enough space, we loop through the list
            if (new_size + j) > 30000000:
                return j
            else:
                continue
            
first_half_solution = find_size_directory(input_file)
second_half_solution = find_size_directory(input_file, True)
print(f'The solution to the first half of the problem is {first_half_solution}, and the solution to the second half is {second_half_solution})
