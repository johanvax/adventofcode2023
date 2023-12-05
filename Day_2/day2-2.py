import re

with open('day2input.txt') as f:
    lines = f.readlines()

result = 0
for line in lines:
    subsets = []
    redvals = []
    greenvals = []
    bluevals = []
    line = line.strip()
    line = line.replace('\n', '')
    line = re.split(':', line)
    temp = re.split(';', line[1])
    for i in range(0, len(temp)):
        instance = re.split(',', temp[i])
        for i in range(0, len(instance)):
            instance[i] = instance[i].strip()
            instance[i] = re.split(' ', instance[i])
            subsets.append(instance[i])

    for i in range(0, len(subsets)):
        if subsets[i][1] == 'green':
            redvals.append(int(subsets[i][0]))
        elif subsets[i][1] == 'blue':
            bluevals.append(int(subsets[i][0]))
        else:
            greenvals.append(int(subsets[i][0]))

    result += max(greenvals)*max(redvals)*max(bluevals)
    
              
print(result)

    