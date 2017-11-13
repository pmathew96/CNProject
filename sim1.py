import random
import time


class Neuron:
    name = ''
    firing = 0
    def __init__(self, name, p, t):
        self.name = name
        self.potential = p
        self.threshold = t


N1 = Neuron('Neuron 1', -70, -68)
N2 = Neuron('Neuron 2', -70, -68)
N3 = Neuron('Neuron 3', -70, -69)
N4 = Neuron('Neuron 4', -70, -69)

#f = open('s10.txt', 'w')
ctr = 0

while True:
    randNum1 = random.randint(0,1)
    randNum2 = random.randint(0,1)
    N1.potential += randNum1
    N2.potential += randNum2
    if N1.potential >= N1.threshold & N2.potential >= N2.threshold:
        randNum3 = random.randint(0,1)
        if randNum3 == 0:
            N1.firing = 1
            N2.potential -= 1
            N3.potential += 1
        if randNum3 == 1:
            N2.firing = 1
            N1.potential -= 1
            N3.potential += 1
    elif N1.potential >= N1.threshold:
        N1.firing = 1
        N2.potential -= 1
        N3.potential += 1
    elif N2.potential >= N2.threshold:
        N2.firing = 1
        N1.potential -= 1
        N4.potential += 1
    #ret = str(N1.firing) + ',' + str(N2.firing)
    #f.write(ret+'\n')
    print('(' + str(N1.firing) + ',' + str(N2.firing) + ')')

    if N1.firing == 1:
        N1.potential -= 1
        N1.firing = 0
        # if N3.potential == N3.threshold:
        #     N1.potential = -70
        #     N3.potential = -70
    if N2.firing == 1:
        N2.potential -= 1
        N2.firing = 0
        # if N4.potential == N4.threshold:
        #     N2.potential = -70
        #     N4.potential = -70
    time.sleep(1)

#f.close()



