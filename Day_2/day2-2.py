import re

with open('day2test.txt') as f:
    lines = f.readlines()

result = 0
for line in lines:
    
    line = line.strip()
    line = line.replace('\n', '')
    line = re.split(':', line)
    subsets = re.split(';', line[1])
    for i in range(0, len(subsets)):
        instance = re.split(',', subsets[i])
        for i in range(0, len(instance)):
            instance[i] = instance[i].strip()
            instance[i] = re.split(' ', instance[i])
        print(instance)
            

        
print(result)

    