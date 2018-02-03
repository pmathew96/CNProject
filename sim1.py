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
        self.resting = p
        self.threshold = t


N1 = Neuron('Neuron 1', -70, -55)

N2 = Neuron('Neuron 2', -70, -55)

f = open('test.txt', 'w')
ctr = 0


def depolarize(N):
    N.potential += 2

i = 0

while i < 1000000:

    if N1.firing == 1:
        N1.firing = 0

    if N2.firing == 1:
        N2.firing = 0

    #generating random numbers
    randNum1 = random.randint(0,5)
    if randNum1 != 0:
        randNum1 -= random.uniform(0,1)
    randNum2 = random.randint(0,5)
    if randNum2 != 0:
        randNum2 -= random.uniform(0,1)
    N1.resting += randNum1
    N2.resting += randNum2

    if N1.resting > N1.threshold:
        N1.firing = 1
        N2.inhibited = 1

    if N2.resting > N2.threshold:
        N2.firing = 1
        N1.inhibited = 1

    if N1.inhibited == 1:
        N1.resting -= 20
        N1.firing = 0
        N1.inhibited = 0

    if N2.inhibited == 1:
        N2.resting -= 20
        N2.firing = 0
        N2.inhibited = 0


    print('N1:(' + str(N1.resting) + ')' + '\t\tN2:(' + str(N2.resting) + ',' + ')')
    print(str(N1.firing)+','+str(N2.firing))

    if N1.firing == 1:
        N1.resting = -75

    if N2.firing == 1:
        N2.resting = -75

    ret = str(N1.firing) + ',' + str(N2.firing)
    f.write(ret+'\n')

    #time.sleep(1)

f.close()



