input = ""
smallerInput = ""

import math

with open("input.txt", "r") as file:
    input = file.read()
with open("smaller_input.txt", "r") as file:
    smallerInput = file.read()

lines = input.split("\n")

answer1 = 1
answer2 = 0

times = lines[0].split(": ")[1].split(" ")
distances = lines[1].split(": ")[1].split(" ")

for i in range(0, len(times)):
    times[i] = int(times[i])
    distances[i] = int(distances[i])

for i in range(0, len(times)):
    delta = times[i] ** 2 - 4 * distances[i]
    t1 = 0.5 * (times[i] - math.sqrt(delta))
    t2 = 0.5 * (times[i] + math.sqrt(delta))

    r = int(t2) - (int(t1))

    if(t2 == int(t2) and t1 == int(t1)):
        r -= 1

    answer1 *= r

time = int(lines[0].split(": ")[1].replace(" ", ""))
distance = int(lines[1].split(": ")[1].replace(" ", ""))

delta = time ** 2 - 4 * distance
t1 = 0.5 * (time - math.sqrt(delta))
t2 = 0.5 * (time + math.sqrt(delta))

answer2 = int(t2) - (int(t1))

if(t2 == int(t2) and t1 == int(t1)):
    answer2 -= 1


print(answer1)
print(answer2)