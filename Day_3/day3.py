# Search for digits, and concatenate for the whole number
# check if any of the numbers positions are close to a symbol
# if they are, add the number to the result

with open('day3test.txt') as f:
    lines = f.readlines()

# find number of rows

def check_neighbors(row, col):
    value = 0
    if row == 0:
        if col == 0:
            if lines[row+1][col].isdigit() or lines[row+1][col] == '.':
                value += 1
            if lines[row+1][col+1].isdigit() or lines[row+1][col+1] == '.':
                value += 1
            if lines[row][col+1].isdigit() or lines[row][col+1] == '.':
                value += 1
            if value == 3:
                return False
        elif col == len(lines[row] - 1):
            if lines[row+1][col].isdigit() or lines[row+1][col] == '.':
                value += 1
            if lines[row+1][col-1].isdigit() or lines[row+1][col-1] == '.':
                value += 1
            if lines[row][col-1].isdigit() or lines[row][col-1] == '.':
                value += 1
            if value == 3:
                return False
        else:
            if lines[row+1][col].isdigit() or lines[row+1][col] == '.':
                value += 1
            if lines[row+1][col+1].isdigit() or lines[row+1][col+1] == '.':
                value += 1
            if lines[row][col+1].isdigit() or lines[row][col+1] == '.':
                value += 1
            if lines[row+1][col-1].isdigit() or lines[row+1][col-1] == '.':
                value += 1
            if lines[row][col-1].isdigit() or lines[row][col-1] == '.':
                value += 1
            if value == 5:
                return False
    elif row == len(lines) - 1:
        # do stuff

result = 0
for row in range(0, len(lines)):
    
    for i in range(0, len(lines[row])):
        if lines[row][i].isdigit():
            # check neighbors for symbols other than '.' and digits

            if check_neighbors(row, i):
                # concatenate and add to result
        