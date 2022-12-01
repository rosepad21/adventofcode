def calories_count(x):
    fh = open(x)
    new = []
    count = 0
    for line in fh:
        line = line.strip()
        if line.isdigit():
            count += int(line)
        else:
            new.append(count)
            count = 0
    return max(new)

print(calories_count('input.txt'))