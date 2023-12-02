import pathlib

def main():

    input_file = pathlib.Path().cwd() / 'input.txt'

    with open(input_file, 'r') as f:
        lines = f.readlines()
    max_values = {'red' : 12, 'blue' : 14, 'green' : 13}
    puzzle_1 = 0
    puzzle_2 = 0
    num_line = 0
    for line in lines:
        num_line += 1
        puzzle_1 += solvePuzzle(line, max_values, num_line)[0]
        puzzle_2 += solvePuzzle(line, max_values)[1]
    print("Result of the first puzzle: " + str(puzzle_1))
    print("Result of the second puzzle: " + str(puzzle_2))

def solvePuzzle(data, max_values, num_line=0):
    colours = {}
    power = 1
    data = data[data.find(':')+2:].rstrip()
    games = data.split('; ')

    for game in games:
        temp = game.split(', ')
        for tem in temp:
            couple = tem.split(" ")
            number = int(couple[0])
            colour = couple[1]
            colours[colour] = max(colours.get(colour, number), number)
    
    check = True
    for k, v in colours.items():
        power *= v
        if v > max_values.get(k, 0):
            check = False
    
    if not check:
        num_line = 0
    return [num_line, power]

if __name__ == '__main__':
    main()
