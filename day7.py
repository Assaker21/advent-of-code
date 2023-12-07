input = ""
smallerInput = ""

import functools

with open("input.txt", "r") as file:
    input = file.read()
with open("smaller_input.txt", "r") as file:
    smallerInput = file.read()

lines = input.split("\n")

answer1 = 0
answer2 = 0

hands = []
for line in lines:
    hand = line.split(" ")
    hand[1] = int(hand[1])
    hands.append(hand)


#hands_dict = {row[0]: row[1] for row in hands}
#hands = list(hands_dict.keys())

def getValue(c):
    if(c.isdigit()):
        return int(c)
    elif(c == "T"):
        return 10
    elif(c == "J"):
        return 11
    elif(c == "Q"):
        return 12
    elif(c == "K"):
        return 13
    elif(c == "A"):
        return 14
    
    print("HERE: " + c)

def compareCards(c1, c2):
    arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    arr2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for c in c1:
        arr1[getValue(c)] += 1
    for c in c2:
        arr2[getValue(c)] += 1

    nonzero1 = 0
    nonzero2 = 0

    for k in arr1:
        if(k != 0):
            nonzero1 += 1
    for k in arr2:
        if(k != 0):
            nonzero2 += 1
    
    if(nonzero1 < nonzero2):
        return 1
    elif(nonzero1 > nonzero2):
        return -1
    else:
        if(nonzero1 == 1 or nonzero1 == 4 or nonzero1 == 5):
            for i in range(0, 5):
                if(getValue(c1[i]) > getValue(c2[i])):
                    return 1
                elif(getValue(c1[i]) < getValue(c2[i])):
                    return -1
        if(nonzero1 == 2 or nonzero1 == 3): #four of a kind or full house
            max1 = 0
            max2 = 0
            
            for item in arr1:
                if(item > max1):
                    max1 = item
            for item in arr2:
                if(item > max2):
                    max2 = item

            if(max1 > max2):
                return 1
            elif(max1 < max2):
                return -1
            else:
                for i in range(0, 5):
                    if(getValue(c1[i]) > getValue(c2[i])):
                        return 1
                    elif(getValue(c1[i]) < getValue(c2[i])):
                        return -1
    return 0

def compareFunction(c1, c2):
    return compareCards(c1[0], c2[0])

def getValue2(c):
    if(c.isdigit()):
        return int(c)
    elif(c == "T"):
        return 10
    elif(c == "J"):
        return 1
    elif(c == "Q"):
        return 12
    elif(c == "K"):
        return 13
    elif(c == "A"):
        return 14
    
    print("HERE: " + c)


def compareCards2(c1, c2):
    arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    arr2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for c in c1:
            arr1[getValue2(c)] += 1
    for c in c2:
            arr2[getValue2(c)] += 1
    
    m1 = 0
    mi1 = 0
    m2 = 0
    mi2 = 0

    for i in range(2, len(arr1)):
        if(arr1[i] > m1):
            m1 = arr1[i]
            mi1 = i
    for i in range(2, len(arr2)):
        if(arr2[i] > m2):
            m2 = arr2[i]
            mi2 = i
    
    arr1[mi1] = arr1[mi1] + arr1[1]
    arr1[1] = 0
    arr2[mi2] = arr2[mi2] + arr2[1]
    arr2[1] = 0

    nonzero1 = 0
    nonzero2 = 0

    for k in arr1:
        if(k != 0):
            nonzero1 += 1
    for k in arr2:
        if(k != 0):
            nonzero2 += 1
    
    if(nonzero1 < nonzero2):
        return 1
    elif(nonzero1 > nonzero2):
        return -1
    else:
        if(nonzero1 == 1 or nonzero1 == 4 or nonzero1 == 5):
            for i in range(0, 5):
                if(getValue2(c1[i]) > getValue2(c2[i])):
                    return 1
                elif(getValue2(c1[i]) < getValue2(c2[i])):
                    return -1
        if(nonzero1 == 2 or nonzero1 == 3): #four of a kind or full house
            max1 = 0
            max2 = 0
            
            for item in arr1:
                if(item > max1):
                    max1 = item
            for item in arr2:
                if(item > max2):
                    max2 = item

            if(max1 > max2):
                return 1
            elif(max1 < max2):
                return -1
            else:
                for i in range(0, 5):
                    if(getValue2(c1[i]) > getValue2(c2[i])):
                        return 1
                    elif(getValue2(c1[i]) < getValue2(c2[i])):
                        return -1
    return 0

def compareFunction2(c1, c2):
    return compareCards2(c1[0], c2[0])


sorted_hands1 = sorted(hands, key=functools.cmp_to_key(compareFunction))

for i in range(0, len(sorted_hands1)):
    answer1 += (i + 1) * sorted_hands1[i][1]

sorted_hands2 = sorted(hands, key=functools.cmp_to_key(compareFunction2))

for i in range(0, len(sorted_hands2)):
    answer2 += (i + 1) * sorted_hands2[i][1]

print(answer1)
print(answer2)