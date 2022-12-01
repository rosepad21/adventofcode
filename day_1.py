def calories_count(x):
    fh = open(x)
    elves_calories = [] # list containing all the calories every elf is carrying
    count = 0
    for line in fh:
        line = line.strip()
        if line.isdigit():
            # if the line contains a digit, we add it to the count variable
            count += int(line)
        else:
            # else, it means we counted all the calories for that elf
            # we append the total to the list and we reset the count
            new.append(count)
            count = 0
    # returning the max value from the list
    return max(new)
