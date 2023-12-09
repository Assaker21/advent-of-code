input = ""
smallerInput = ""

with open("input.txt", "r") as file:
    input = file.read()
with open("smaller_input.txt", "r") as file:
    smallerInput = file.read()

lines = input.split("\n")

answer1 = 0
answer2 = 0

values = []
for i in range(0, len(lines)):
    values.append([])
    for num in lines[i].split(" "):
        values[i].append(int(num))

def FindEndPosition(line, steps):
    steps[0].append(line[-1])
    steps[1].append(line[0])
    all_zeros = True

    for i in range(0, len(line)):
        if(line[i] != 0):
            all_zeros = False
            break
    
    if(all_zeros):
        return steps
    
    new_line = []
    for i in range(0, len(line) - 1):
        new_line.append(line[i + 1] - line[i])

    return FindEndPosition(new_line, steps)

def FindNextNumber(steps):
    nextValue = 0
    j = len(steps) - 1

    while(j > 0):
        nextValue = steps[j - 1] + nextValue
        j -= 1
    
    return nextValue

def FindPrevNumber(steps):
    prevValue = 0
    j = len(steps) - 2

    while(j >= 0):
        prevValue = steps[j] - prevValue
        j -= 1
    
    return prevValue

for line in values:
    steps = FindEndPosition(line, [[], []])
    answer1 += FindNextNumber(steps[0])
    answer2 += FindPrevNumber(steps[1])
        
print(answer1)
print(answer2)