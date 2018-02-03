import matplotlib.pyplot as plt
import numpy as np


flag1 = 0
flag2 = 0

ctr = 0

alt = 0
nalt = 0

with open("test.txt") as f:
    for line in f:
        line = line.strip()
        if line == "1,0":
            if flag2 == 1:
                flag2 = 0
                flag1 = 1
                alt += 1
                ctr = 0
            elif flag2 == 0:
                ctr = 0
                flag1 = 1
                nalt += 1
            else:
                ctr += 1
        elif line == "0,1":
            if flag1 == 1:
                flag1 = 0
                flag2 = 1
                alt += 1
                ctr = 0
            elif flag1 == 0:
                ctr = 0
                flag2 = 1
                nalt += 1
            else:
                ctr += 1
        else:
            ctr += 1

freqList = [alt, nalt]
labelList = ['Alternating', 'Not Alternating']



y = np.arange(1,3)
x = np.arange(1,3)
plt.bar(y, freqList)
plt.xticks(x, labelList)
plt.yticks(np.arange(1,31,4))
plt.show()


f.close()

