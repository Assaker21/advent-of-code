input = ""
smallerInput = ""

import time
import math

with open("input.txt", "r") as file:
    input = file.read()
with open("smaller_input.txt", "r") as file:
    smallerInput = file.read()

instructions = input.split("\n")[0]
lines = input.split("\n\n")[1].split("\n")

answer1 = 0
answer2 = 0

maps = {}

for line in lines:
    maps[line.split(" ")[0]] = [line[7] + line[8] + line[9], line[12] + line[13] + line[14]]

last_position = "AAA"
index = 0

keys = list(maps.keys())
starting_positions = []

for i in range(0, len(keys)):
    if(keys[i][2] == "A"):
        starting_positions.append(keys[i])

while(last_position != "ZZZ"):
    answer1 += 1

    if(instructions[index] == "L"):
        last_position = maps[last_position][0]
    elif(instructions[index] == "R"):
        last_position = maps[last_position][1]

    index = (index + 1) % len(instructions)

index = 0
vals = []

for starting_position in starting_positions:
    last_position = starting_position
    index = 0
    iterations = 0

    while(last_position[2] != "Z"):
        iterations += 1
        if(instructions[index] == "L"):
            last_position = maps[last_position][0]
        elif(instructions[index] == "R"):
            last_position = maps[last_position][1]

        index = (index + 1) % len(instructions)
    
    vals.append(iterations)

def lcm(xs):
    ans = 1
    for x in xs:
        ans = (x * ans) // math.gcd(x, ans)
    return ans

answer2 = lcm(vals)

print(answer1)
print(answer2)