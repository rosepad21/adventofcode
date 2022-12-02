fh = open('input.txt')
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
        elves_calories.append(count)
        count = 0

max_calories = max(elves_calories)
          
# now on to find the sum of the top three elves' calories
sorted_list = sorted(elves_calories, reverse=True)
top_three = sum(sorted_list[:3])
