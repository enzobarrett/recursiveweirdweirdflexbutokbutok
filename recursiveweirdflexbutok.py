import sys

colors = ['\033[31m','\033[32m','\033[33m','\033[34m','\033[35m','\033[36m','\033[91m','\033[92m','\033[93m','\033[94m','\033[95m','\033[96m']
reset = '\033[0m'

number = int(sys.argv[1])
def weirdflexbutok(n, y):
    if n > 0:
        if n == 1:
            print(colors[y], 'Weird Flex', end='')
        else:
            print(colors[y], 'Weird', end='')
        if y == len(colors)-1:
            y = 0
            weirdflexbutok(n-1,y)
        else:
            weirdflexbutok(n-1, y+1)
        print(colors[y], 'But Ok', end='')
weirdflexbutok(number, 0)
print(reset,'')

