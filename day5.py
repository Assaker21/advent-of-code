input = ""
smallerInput = ""

with open("input.txt", "r") as file:
    input = file.read()
with open("smaller_input.txt", "r") as file:
    smallerInput = file.read()

lines = smallerInput.split("\n\n")

seeds = lines[0].split(" ")[1:]
for i in range(0, len(seeds)):
    seeds[i] = int(seeds[i])    

lines = lines[1:]

locations = []

answer1 = 0
answer2 = -1

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
    i = 0
    while(i < len(seeds)):
        if(value <= seeds[i + 1] + seeds[i] and value >= seeds[i]):
            return True
        i += 2
    
    return False


def getDestinationRange(source, endsource, maps, i):
    if(i >= len(maps)):
        global answer2
        print(source)
        if(source != 0 and (answer2 == -1 or source < answer2)): answer2 = source
        return
    
    for map in maps[i]:
        target_source = map[1]
        target_end_source = map[1] + map[2]
        target_destination = map[0]
        target_range = map[2]

        if(source >= target_source and source <= target_end_source and endsource >= target_source and endsource <= target_end_source):
            getDestinationRange(source - target_source + target_destination, endsource - target_source + target_destination, maps, i + 1)
        elif(source >= target_source and source <= target_end_source):
            getDestinationRange(source - target_source + target_destination, target_destination + target_range, maps, i + 1)
        elif(endsource >= target_source and endsource <= target_end_source):
            getDestinationRange(target_destination, endsource - target_source + target_destination, maps, i + 1)
        else:
            getDestinationRange(source, endsource, maps, i + 1)
            


lines = lines[0 : (len(lines) - 1)]

sranges = []
i = 0
while(i < len(seeds)):
    sranges.append([seeds[i], seeds[i + 1] + seeds[i]])
    i += 2

maps = []
for j in range(0, len(lines)):
    lines[j] = lines[j].split(":\n")[1]
    arr = []
    for l in lines[j].split("\n"):
        v = l.split(" ")
        for k in range(0, 3):
            v[k] = int(v[k])
        arr.append(v)
    maps.append(arr)

for srange in sranges:
    getDestinationRange(srange[0], srange[1], maps, 0)

print("")
print(answer1)
print(answer2)