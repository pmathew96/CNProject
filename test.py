'''
1. Neuron fires
2. Neuron inhibits other neuron
3.
'''




import random
import time


class Neuron:
    name = ''
    firing = 0
    firedPreviously = 0
    inhibited = 0
    def __init__(self, name, p, t):
        self.name = name
        self.potential = p
        self.threshold = t


N1 = Neuron('Neuron 1', -70, -68)
N2 = Neuron('Neuron 2', -70, -68)
# N3 = Neuron('Neuron 3', -70, -69)
# N4 = Neuron('Neuron 4', -70, -69)

f = open('test.txt', 'w')
ctr = 0


def depolarize(N):
    N.potential += 2

while True:


    #generating random numbers
    randNum1 = random.uniform(0,1)
    randNum2 = random.uniform(0,1)
    N1.potential += randNum1
    N2.potential += randNum2
    # if N1.potential >= N1.threshold & N2.potential >= N2.threshold:
    #     randNum3 = 1#random.randint(0,1)
    #     if randNum3 == 1:
    #         N1.firing = 1
    #         N2.potential -= 1
    #         N3.potential += 1
    #     if randNum3 == 1:
    #         N2.firing = 1
    #         N1.potential -= 1
    #         N3.potential += 1
    #The neurons fire when the potential goes above the threshold
    # if N1.potential >= N1.threshold:
    #     N1.firing = 1
        #N2.potential -= 1
        #N3.potential += 1
    # if N2.potential >= N2.threshold:
    #     N2.firing = 1
        #N1.potential -= 1
        #N4.potential += 1







    # The neurons inhibit each other by hyperpolarizing each other

    if N1.firedPreviously == 1:
        N2.potential -= 2
        N2.inhibited = 1

    if N2.firedPreviously == 1:
        N1.potential -= 2
        N1.inhibited = 1

    # Checking the potential of each neuron and setting the firing variable

    if N1.potential < N1.threshold:
        N1.firing = 0
        N1.firedPreviously = 0
    else:
        N1.firing = 1

    if N2.potential < N2.threshold:
        N2.firing = 0
        N2.firedPreviously = 0
    else:
        N2.firing = 1

    print('N1:(' + str(N1.potential)+',' + str(N1.firing)+')'+'\t\tN2:(' + str(N2.potential)+',' + str(N2.firing) + ')')
    ret = str(N1.firing) + ',' + str(N2.firing)
    f.write(ret+'\n')

    if N1.inhibited == 1:
        N1.inhibited = 0
        N1.potential += 2
    if N2.inhibited == 1:
        N2.inhibited = 0
        N2.potential += 2

        # Once the neurons fire, the potential is reset to resting potential
        # and the firing variable is reset to 0.
        # The hyperpolarized neurons get depolarized.
    if N1.firing == 1:
        N1.potential = -70
        N1.firing = 0
        N1.firedPreviously = 1
        # depolarize(N2)
        # if N3.potential == N3.threshold:
        #     N1.potential = -70
        #     N3.potential = -70
    if N2.firing == 1:
        N2.potential = -70
        N2.firing = 0
        N2.firedPreviously = 1
        # depolarize(N1)
        # if N4.potential == N4.threshold:
        #     N2.potential = -70
        #     N4.potential = -70


    time.sleep(1)

#f.close()