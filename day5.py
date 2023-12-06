input = ""
smallerInput = ""

with open("input.txt", "r") as file:
    input = file.read()
with open("smaller_input.txt", "r") as file:
    smallerInput = file.read()

lines = input.split("\n\n")

seeds = lines[0].split(" ")[1:]
for i in range(0, len(seeds)):
    seeds[i] = int(seeds[i])    

lines = lines[1:]

locations = []

answer1 = 0
answer2 = 0

for seed in seeds:
    next = seed
    for maps in lines:
        maps = maps.split("\n")[1:]

        for map in maps:
            source = int(map.split(" ")[1])
            destination = int(map.split(" ")[0])
            r = int(map.split(" ")[2])
            if(next >= source and next <= source + r):
                next = next - source + destination
                break
    
    locations.append(next)
    if(next < answer1 or answer1 == 0):
        answer1 = next

def inSeeds(seeds, value):
    i = -2
    while(i < len(seeds)):
        i += 2
        if(value <= max(seeds[i], seeds[i + 1]) and value >= min(seeds[i], seeds[i + 1])):
            return True
    
    return False

location_map = lines[-1] #0 3024237462 156854744
lines = lines[0 : (len(lines) - 1)]

for k in range(3024237462, 3024237462 + 156854744):
    i = len(lines)
    next = k

    while(i >= 0):
        i -= 1
        maps = lines[i].split("\n")[1:]
        for map in maps:
            source = int(map.split(" ")[1])
            destination = int(map.split(" ")[0])
            range = int(map.split(" ")[2])
            if(next >= destination and next <= destination + range):
                next = next - destination + source
                break

    if(inSeeds(seeds, next)):
        print(next)
        answer2 = next
        break
    

print(answer1)
print(answer2)