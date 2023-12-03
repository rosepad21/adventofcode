import pathlib

def main():
    puzzle_1 = 0
    puzzle_2 = 0
    input_file = pathlib.Path().cwd() / 'input.txt'

    with open(input_file, 'r') as fh:
        lines = fh.readlines()
    for line in lines:
        puzzle_1 += first_puzzle(line)
        puzzle_2 += second_puzzle(line)
    print(f'Result of the first puzzle: {puzzle_1}')
    print(f'Result of the second puzzle: {puzzle_2}')

def first_puzzle(data):
    s1 = ''
    s2= ''
    for i in range(len(data)):
        if data[i].isdigit():
            if s1 == '':
                s1 = data[i]
            else:
                s2 = data[i]
    if s1 == '':
        s1 = s2
    if s2 == '':
        s2 = s1
    return int(s1 + s2)

def second_puzzle(data):
    numbers = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9, "o" : "o", "on" : "on", "t" : "t", "tw" : "tw",
          "th" : "th", "thr" : "thr", "thre" : "thre", "f" : "f", "fo" : "fo", "fou" : "fou", "fi" : "fi", "fiv": "fiv", "s" : "s", "si" : "si",
          "se" : "se", "sev" : "sev", "seve" : "seve", "e" : "e", "ei" : "ei", "eig" : "eig", "eigh" : "eigh", "n":"n", "ni" : "ni", "nin" : "nin"}
    s1 = ''
    s2= ''
    temp = ''

    for i in range(len(data)):
        if data[i].isdigit():
            if s1 == '':
                s1 = data[i]
            else:
                s2 = data[i]
            temp = ''
        else:
            temp += data[i]
            if temp in numbers:
                if type(numbers.get(temp)) == int:
                    if s1 == '':
                        s1 = str(numbers.get(temp))
                    else: 
                        s2 = str(numbers.get(temp))
                    temp = data[i]
                else:
                    temp = numbers.get(temp)
            else:
                if len(temp) > 1:
                    temp = temp[1:]
                else:
                    temp = ""
    if s1 == '':
        s1 = s2
    if s2 == '':
        s2 += s1
    return int(s1 + s2)

if __name__ == '__main__':
    main()
