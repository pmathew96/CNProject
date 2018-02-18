'''
1. Neuron fires
2. Neuron inhibits other neuron
3.
'''




import random
import time


class Neuron:
    firing = 0
    firedPreviously = 0
    inhibited = 0
    def __init__(self, name, p, t):
        self.name = name
        self.potential = p
        self.threshold = t


N1 = Neuron('Neuron 1', -70, -55)

N2 = Neuron('Neuron 2', -70, -55)

N3 = Neuron('Neuron 3', -70, -55)

f = open('test1.txt', 'w')
ctr = 0


def depolarize(N):
    N.potential += 2

i = 0

while i < 1000000:

    if N1.firing == 1:
        N1.firing = 0
        N1.potential -= 25

    if N2.firing == 1:
        N2.firing = 0
        N2.potential -= 25

    #generating random numbers
    randNum1 = random.randint(0,5)
    if randNum1 != 0:
        randNum1 -= random.uniform(0,1)
    randNum2 = random.randint(0,5)
    if randNum2 != 0:
        randNum2 -= random.uniform(0,1)
    N1.potential += randNum1
    N2.potential += randNum2

    if N1.potential > N1.threshold:
        N1.firing = 1
        N2.inhibited = 1

    if N2.potential > N2.threshold:
        N2.firing = 1
        N1.inhibited = 1

    if N1.inhibited == 1:
        N1.potential -= 20
        N1.firing = 0

    if N2.inhibited == 1:
        N2.potential -= 20
        N2.firing = 0

    if N1.firing == 1:
        N3.potential += 20

    if N2.firing == 1:
        N3.potential += 20

    if N3.potential >= N3.threshold:
        N3.firing = 1

    else:
        N3.firing = 0

    #print(str(N3.firing)+', '+str(N3.potential))

    print('N1:(' + str(N1.potential) + ')' + '\t\tN2:(' + str(N2.potential) + ',' + ')')
    print(str(N1.firing)+','+str(N2.firing))

    ret = str(N1.firing) + ',' + str(N2.firing)


    if N3.firing == 1:
        N3.firing = 0
        N3.potential = -70

    # if N1.inhibited == 1 & N2.inhibited == 1:
    #     N2.inhibited = 0
    #     N1.inhibited = 0

    if N1.inhibited == 1:
        N1.inhibited = 0
        N1.potential += random.uniform(10, 15)

    if N2.inhibited == 1:
        N2.inhibited = 0
        N2.potential += random.uniform(10, 15)
    f.write(ret+'\n')

    i += 1
    time.sleep(1)

f.close()



