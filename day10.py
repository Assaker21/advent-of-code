input = ""
smallerInput = ""

import time

with open("input.txt", "r") as file:
    input = file.read()
with open("smaller_input.txt", "r") as file:
    smallerInput = file.read()

lines = input.split("\n")

answer1 = 1
answer2 = 0

def updateNext(lines, next, coming_from):
    letter = lines[next[0]][next[1]]

    old_next = list(next)

    if(letter == "|" and str(coming_from) == str([next[0] - 1, next[1]])):
        next[0] += 1
    elif(letter == "|" and str(coming_from) == str([next[0] + 1, next[1]])):
        next[0] -= 1

    elif(letter == "-" and str(coming_from) == str([next[0], next[1] + 1])):
        next[1] -= 1
    elif(letter == "-" and str(coming_from) == str([next[0], next[1] - 1])):
        next[1] += 1

    elif(letter == "L" and str(coming_from) == str([next[0] - 1, next[1]])):
        next[1] += 1
    elif(letter == "L" and str(coming_from) == str([next[0], next[1] + 1])):
        next[0] -= 1

    elif(letter == "J" and str(coming_from) == str([next[0] - 1, next[1]])):
        next[1] -= 1
    elif(letter == "J" and str(coming_from) == str([next[0], next[1] - 1])):
        next[0] -= 1

    elif(letter == "7" and str(coming_from) == str([next[0] + 1, next[1]])):
        next[1] -= 1
    elif(letter == "7" and str(coming_from) == str([next[0], next[1] - 1])):
        next[0] += 1

    elif(letter == "F" and str(coming_from) == str([next[0] + 1, next[1]])):
        next[1] += 1
    elif(letter == "F" and str(coming_from) == str([next[0], next[1] + 1])):
        next[0] += 1

    return [next, old_next]


s_pos = []

for i in range(0, len(lines)):
    done = False
    for j in range(0, len(lines[i])):
        if(lines[i][j] == "S"):
            s_pos = [i, j]
            done = True
            break
    if(done):
        break

next1 = [s_pos[0] - 1, s_pos[1]]
next2 = [s_pos[0], s_pos[1] - 1]
old_next1 = list(s_pos)
old_next2 = list(s_pos)

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.

loop_nodes = [list(s_pos), list(next1), list(next2)]
visited_nodes = []

while(not (next1[0] == next2[0] and next1[1] == next2[1])):
    
    n1 = updateNext(lines, next1, old_next1)
    next1 = n1[0]
    old_next1 = n1[1]
    loop_nodes.append(next1)

    n2 = updateNext(lines, next2, old_next2)
    next2 = n2[0]
    old_next2 = n2[1]
    loop_nodes.append(next2)

    answer1 += 1



print(answer1)
print(answer2)