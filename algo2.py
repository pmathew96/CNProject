n = input()

ans = ['0'] * 2**n

def splita(list, n):
    n = 2**n
    a = [[] for i in range(n)]
    counter = 0
    for i in range(0, len(list)):
        a[counter].append(list[i])
        if len(a[counter]) == len(list) / n:
            counter = counter + 1
            continue
    return a

inp = [1,2,3,4,5,6,7,8]
ans =  splita(ans, n)

for i in range (0, n):
    t = []
    for j in range(0,2**(i+1)):
        t = t + ans[j]
    h = len(t)/2
    htemp = []
    for k in range(0,h):
        htemp = htemp + t[k]
    print htemp
