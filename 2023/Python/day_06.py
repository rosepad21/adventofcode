import pathlib
from datetime import datetime

def main():
    input_file = pathlib.Path().cwd() / 'input.txt'

    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    first_puzzle = 1
    milliseconds = [x.strip() for x in lines[0][lines[0].find(':')+1:].strip().split(" ") if x != '']
    distance = [x.strip() for x in lines[1][lines[1].find(':')+1:].strip().split(" ") if x != '']
    ms_secondpuzzle = ''.join(milliseconds)
    ds_secondpuzzle = ''.join(distance)
    print(milliseconds, distance)

    for i in range(len(milliseconds)):
        first_puzzle *= defineWaysToWin(milliseconds[i], distance[i])
    
    second_puzzle = defineWaysToWin(ms_secondpuzzle, ds_secondpuzzle)
    print(f'Result of the first puzzle: {first_puzzle}')
    print(f'Result of the second puzzle: {second_puzzle}')
    
def defineWaysToWin(milliseconds, distance):
    counter = 0
    tmin, tmax = 0, int(milliseconds)
    while tmin <= tmax:
        if ((tmax-tmin)*tmin) > int(distance):
            counter = (tmax-(tmin*2)+1)
            break
        tmin += 1
    return counter

if __name__ == '__main__':
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
