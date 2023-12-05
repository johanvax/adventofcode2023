import re

colors = {'red' : 12, 'green' : 13, 'blue' : 14}

with open('day2input.txt') as f:
    lines = f.readlines()

id = 1
result = 0
for line in lines:
    temp = True
    line = line.strip()
    line = line.replace('\n', '')
    line = re.split(':', line)
    subsets = re.split(';', line[1])
    for i in range(0, len(subsets)):
        instance = re.split(',', subsets[i])
        for i in range(0, len(instance)):
            instance[i] = instance[i].strip()
            instance[i] = re.split(' ', instance[i])
            for color in colors:
                if instance[i][1] == color and int(instance[i][0]) > colors[color]:
                    temp = False

    if temp:
        result += id
        
    id = id + 1
print(result)

    