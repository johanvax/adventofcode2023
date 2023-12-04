dictionary = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9
}

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('day1input.txt') as f:
    lines = f.readlines()

result = 0

for line in lines:
    # list of tuples [index, value]
    num = []
    # to check for names of digits
    temp = ''

    for c in range(0, len(line)):
        # add index and value if digit
        if line[c].isdigit():
            num.append([c, int(line[c])])
            temp = ''
        else:
            # checks is temp is name of digit
            temp += line[c]
            for digit in digits:
                if digit in temp:
                    # add to list [start index, value as int]
                    num.append([c-len(digit)+1, dictionary[digit]])
                    # save the last letter
                    temp = temp[len(temp)-1]
                    break
                
    # sort, concatenate and sum up
    num.sort()
    #print(num)
    result += num[0][1]*10 + num[len(num)-1][1]
    
print(result)