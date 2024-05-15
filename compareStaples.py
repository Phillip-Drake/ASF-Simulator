file1 = open("stapleSet1.txt", 'r')

file2 = open('stapleSet2.txt', 'r')

file3 = open('stapleSet3.txt', 'r')

stapleSetString = file1.read().replace('\n', ' ').split()
stapleSets1 = []
for i in range(0,len(stapleSetString), 2) :
    stapleSets1.append(
        [min(int(stapleSetString[i]), int(stapleSetString[i+1])),
                         max(int(stapleSetString[i]), int(stapleSetString[i+1]))]
                         )
print(len(stapleSets1))

stapleSetString = file2.read().replace('\n', ' ').split()
stapleSets2 = []
for i in range(0,len(stapleSetString), 2) :
    stapleSets2.append(
        [min(int(stapleSetString[i]), int(stapleSetString[i+1])),
                         max(int(stapleSetString[i]), int(stapleSetString[i+1]))]
                         )
    
stapleSetString = file3.read().replace('\n', ' ').split()
stapleSets3 = []
for i in range(0,len(stapleSetString), 2) :
    stapleSets3.append(
        [min(int(stapleSetString[i]), int(stapleSetString[i+1])),
                         max(int(stapleSetString[i]), int(stapleSetString[i+1]))]
                         )
    
print(len(stapleSets2))
numSame1 = 0
numSame2 = 0
numSame3 = 0
for i in range(0, len(stapleSets1)):
    for j in range(0, len(stapleSets2)):
        if(stapleSets1[i][0] == stapleSets2[j][0]):
            if(stapleSets1[i][1] == stapleSets2[j][1]):
                numSame1 += 1
    for j in range(0, len(stapleSets3)):
        if(stapleSets3[j][0] == stapleSets1[i][0]):
            if(stapleSets1[i][1] == stapleSets3[j][1]):
                numSame2 += 1
for i in range(0, len(stapleSets2)):
    for j in range(0, len(stapleSets3)):
        if(stapleSets2[i][0] == stapleSets3[j][0]):
            if(stapleSets2[i][1] == stapleSets3[j][1]):
                numSame3 += 1
                #print(stapleSets1[i])
print(f'Duplicate staples between sets 1 and 2 : {numSame1}')
print(f'Duplicate staples between sets 1 and 3 : {numSame2}')
print(f'Duplicate staples between sets 2 and 3 : {numSame3s}')