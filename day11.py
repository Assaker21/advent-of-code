input = ""
smallerInput = ""

with open("input.txt", "r") as file:
    input = file.read()
with open("smaller_input.txt", "r") as file:
    smallerInput = file.read()

lines = input.split("\n")

original_lines = list(lines)

answer1 = 0
answer2 = 0

def replace_char(input_str, position, new_char):
    str_list = list(input_str)
    str_list[position] = new_char
    new_str = ''.join(str_list)

    return new_str

def insert_into_string(original_str, substring, position):
    part1 = original_str[:position]
    part2 = original_str[position:]
    new_str = part1 + substring + part2

    return new_str

def manhattan_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

i = 0
while(i < len(lines)):
    all_dots = True
    for j in range(0, len(lines[i])):
        if(lines[i][j] != "."):
            all_dots = False
            break
    
    if(all_dots == True):
        lines.insert(i, str(lines[i]))
        i += 1
    
    i += 1

j = 0
while(j < len(lines[0])):
    for i in range(0, len(lines)):
        all_dots = True
        if(lines[i][j] != "."):
            all_dots = False
            break
    if(all_dots == True):
        for i in range(0, len(lines)):
            lines[i] = insert_into_string(lines[i], ".", j)
        
        j += 1
    j += 1


positions = []

for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if(lines[i][j] == "#"):
            positions.append([i, j])

for i in range(0, len(positions)):
    for j in range(i + 1, len(positions)):
        answer1 += manhattan_distance(positions[i][0], positions[i][1], positions[j][0], positions[j][1])

lines = list(original_lines)

i = 0
while(i < len(lines)):
    all_dots = True
    for j in range(0, len(lines[i])):
        if(lines[i][j] != "."):
            all_dots = False
            break
    
    if(all_dots == True):
        lines[i] = lines[i].replace(".", "1")
    
    i += 1

j = 0
while(j < len(lines[0])):
    for i in range(0, len(lines)):
        all_dots = True
        if(not (lines[i][j] == "." or lines[i][j] == "1")):
            all_dots = False
            break
    if(all_dots == True):
        for i in range(0, len(lines)):
            lines[i] = replace_char(lines[i], j, "1")
    j += 1

positions = []

for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if(lines[i][j] == "#"):
            x = 0
            y = 0
            for k in range(0, j):
                if(lines[i][k] == "1"):
                    y += 1000000
                else:
                    y += 1
            for k in range(0, i):
                if(lines[k][j] == "1"):
                    x += 1000000
                else:
                    x += 1
            positions.append([x, y])

for i in range(0, len(positions)):
    for j in range(i + 1, len(positions)):
        answer2 += manhattan_distance(positions[i][0], positions[i][1], positions[j][0], positions[j][1])

print(answer1)
print(answer2)