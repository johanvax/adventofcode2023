with open('day1input.txt') as f:
    lines = f.readlines()

result = 0

for line in lines:
    num = []
    for c in line:
        if c.isdigit():
            num.append(c)
        
    if len(num) > 0:
        num1 = int(num[0])*10
        num2 = int(num[len(num)-1]) + num1
        result += num2

print(result)