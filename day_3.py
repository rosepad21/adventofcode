fh = open('input.txt')
priorities = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8,
            'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16,
            'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v': 22, 'w' : 23, 'x' : 24,
            'y' : 25, 'z' : 26, 'A' : 27, 'B' : 28, 'C' : 29, 'D' : 30, 'E' : 31, 'F' : 32,
            'G' : 33, 'H' : 34, 'I' : 35, 'J' : 36, 'K' : 37, 'L' : 38, 'M' : 39, 'N' : 40,
            'O' : 41, 'P' : 42, 'Q' : 43, 'R' : 44, 'S' : 45, 'T' : 46, 'U' : 47, 'V' : 48,
            'W' : 49, 'X' : 50, 'Y' : 51, 'Z' : 52}
# for the first half of the problem:
old_count = 0
# for the second half of the problem:
badges = []
new_count = 0
for line in fh:
    line = line.rstrip()
    badges.append(set(line)) # we append every line as a set to remove duplicates
    mid = len(line) // 2
    first_half = set(line[:mid])
    second_half = set(line[mid:])
    for i in first_half:
        if i in second_half: # we check whether a character is both in the first and second half of the line
            old_count += priorities[i]
        else:
            continue
    if len(badges) == 3:
        for j in badges[0]:
            if j in badges[1] and j in badges[2]: # we check whether a character appears in all sets in the list
                new_count += priorities[j] 
            else:
                continue
        badges.clear() # we clear the list so we can start over with the next three lines
    else:
        continue
    
print(f"The priority of the items that appear in both parts of the rucksacks is {old_count}, while the priority of the elves' badges is {new_count}")
