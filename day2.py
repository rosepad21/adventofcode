# A = rock, B = paper, C = scissors
# X = rock, Y = paper, Z = scissors
# 1 pt rock, 2pt paper, 3pt scissors
# 0 pt lost, 3 pt draw, 6pt win

# A + x = draw
# A + y = win
# A + z = loss
# B + x = loss
# B + y = draw
# B + z = win
# C + x = win
# C + y = loss
# C + z = draw

fh = open('input.txt')
old_strategy_count = 0 
new_strategy_count = 0
# we create a dictionary that maps the old strategy with the points (first part of the problem)
old_strategy = {'A X' : 4, 'A Y' : 8, 'A Z' : 3, 'B X' : 1, 'B Y' : 5, 'B Z' : 9,
            'C X' : 7, 'C Y' : 2, 'C Z' : 6}
# then we create a new dictionary with the new strategy's points (second part of the problem)
# X = you have to lose, Y = you have to end in a draw, Z = you need to win
new_strategy = {'A X' : 3, 'A Y' : 4, 'A Z' : 8, 'B X' : 1, 'B Y' : 5, 'B Z' : 9, 'C X' : 2, 'C Y' : 6, 'C Z' : 7}
for line in fh:
    line = line.rstrip()
    if line in old_strategy.keys():
        old_strategy_count += old_strategy[line]
    if line in new_strategy.keys():
        new_strategy_count += new_strategy[line]

print(f'Points obtained using the old strategy: {old_strategy_count}; points obtained using the new strategy: {new_strategy_count}')
