input = ""
smallerInput = ""

with open("input.txt", "r") as file:
    input = file.read()
with open("smaller_input.txt", "r") as file:
    smallerInput = file.read()

lines = input.split("\n")

answer1 = 0
answer2 = 0

all_cards = [1] * len(lines)

for i in range(0, len(lines)):
    id = lines[i].split(": ")[0]
    line = lines[i].split(": ")[1]
    left = line.split(" | ")[0]
    right = line.split(" | ")[1]

    wnums = left.split(" ")
    mynums = right.split(" ")

    val = 0
    for mynum in mynums:
        if(mynum != "" and mynum in wnums):
            val += 1
    
    if(val > 0):
        answer1 += 2 ** (val - 1)

    for k in range(0, all_cards[i]):
        for j in range(i + 1, i + val + 1):
            all_cards[j] += 1

    answer2 += all_cards[i]
      
        
print(answer1)
print(answer2)