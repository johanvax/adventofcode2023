import re

colors = ['red', 'green', 'blue']

with open('day2test.txt') as f:
    lines = f.readlines()

for line in lines:
    line = re.split(': | ;')
    print(line)