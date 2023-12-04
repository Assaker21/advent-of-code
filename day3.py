input = ""
smallerInput = ""

with open("input.txt", "r") as file:
    input = file.read()
with open("smaller_input.txt", "r") as file:
    smallerInput = file.read()

lines = input.split("\n")

answer1 = 0
answer2 = 0

def GetNumber(lines, i, j):
    num = lines[i][j]

    left = True
    right = True

    startIndex = j
    endIndex = j

    for k in range(1, 4):
        if(j + k < len(lines[i])):
            if(right and lines[i][j + k].isdigit()):
                num += lines[i][j + k]
                endIndex = j + k
            else: 
                right = False

        if(j - k >= 0):
            if(left and lines[i][j - k].isdigit()):
                num = lines[i][j - k] + num
                startIndex = j - k
            else:
                left = False
    
    return [[startIndex, endIndex], int(num)]
    
for i in range(0, len(lines)):
    j = 0
    while(j < len(lines[i])):
        if(lines[i][j].isdigit()):
            numi = GetNumber(lines, i, j)
            j = numi[0][1]

            exit = False

            for k in range(numi[0][0], numi[0][1] + 1):
                if(exit):
                    break
                for m in [-1, 0, 1]:
                    if(exit):
                        break
                    for n in [-1, 0, 1]:
                        if(exit):
                            break
                        if(m == 0 and n == 0):
                            continue
                        else:
                            if(i + m < len(lines) and i + m >= 0 and k + n < len(lines[i + m]) and k + n >= 0):
                                if(ord(lines[i + m][k + n]) == 46 or (ord(lines[i + m][k + n]) > 47 and ord(lines[i + m][k + n]) < 58)):
                                    pass
                                else:
                                    answer1 += numi[1]
                                    exit = True
                                    
                                
        
        j += 1

for i in range(0, len(lines)):
    j = 0
    while(j < len(lines[i])):
        nums = []
        if(ord(lines[i][j]) == 42):
            for m in [-1, 0, 1]:
                for n in [-1, 0, 1]:
                    if(m == 0 and n == 0):
                        continue
                    elif(i + m >= 0 and i + m < len(lines) and j + n >= 0 and j + n < len(lines[i + m])):
                        if(lines[i + m][j + n].isdigit()):
                            numi = GetNumber(lines, i + m, j + n)
                            nums.append(str(numi[0][0]) + " " + str(numi[0][1]) + " " + str(numi[1]))
        
        if(len(nums) != 0):
            nums = list(set(nums))
            if(len(nums) == 2):
                value = int(nums[0].split(" ")[-1]) * int(nums[1].split(" ")[-1])
                answer2 += value

        j += 1

        
print(answer1)
print(answer2)