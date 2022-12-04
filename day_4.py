fh = open('input.txt')
first_half_count = 0
second_half_count = 0
for line in fh:
    line = line.rstrip()
    hyphen = line.find('-')
    comma = line.find(',')
    hyphen_2 = line.find('-', comma)
    # finding all the pairs that overlap completely
    if int(line[:hyphen]) <= int(line[comma+1:hyphen_2]) and int(line[hyphen+1:comma]) >= int(line[hyphen_2+1:]):
        first_half_count += 1
    elif int(line[comma+1:hyphen_2]) <= int(line[:hyphen]) and int(line[hyphen+1:comma]) <= int(line[hyphen_2+1:]):
        first_half_count += 1
    else:
        continue
    # for the second half of the problem, we just need to exclude the lines where the largest number of one pair /
    # is less than the smallest of the second pair and viceversa
    if int(line[:hyphen]) > int(line[hyphen_2+1:]) or int(line[comma+1:hyphen_2]) > int(line[hyphen+1:comma]):
        continue
    else:
        second_half_count += 1

print(f'The number of pairs that overlap completely is {first_half_count}, while the pairs that only partially overlap are {second_half_count}')
