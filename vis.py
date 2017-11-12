import matplotlib.pyplot as plt
import numpy as np


flag1 = 0
flag2 = 0

ctr = 0

intervalList = []

with open("s1.txt") as f:
    for line in f:
        line = line.strip()
        if line == "1,0":
            if flag2 == 1:
                flag2 = 0
                flag1 = 1
                intervalList.append(ctr+1)
                ctr = 0
            elif flag1 == 0:
                ctr = 0
                flag1 = 1
            else:
                ctr += 1
        elif line == "0,1":
            if flag1 == 1:
                flag1 = 0
                flag2 = 1
                intervalList.append(ctr+1)
                ctr = 0
            elif flag2 == 0:
                ctr = 0
                flag2 = 1
            else:
                ctr += 1
        else:
            ctr += 1

print(intervalList)
freqList = []
labelList = []

for i in range(1,13):
    freqList.append(intervalList.count(i))
    labelList.append(str(i))


print(freqList)

y = np.arange(1,13)
x = np.arange(1,13)
plt.bar(y, freqList)
plt.xticks(x, labelList)
plt.yticks(y)
plt.show()


f.close()

