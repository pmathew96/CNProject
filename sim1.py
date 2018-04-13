'''
1.
'''




import random
import time
import datetime


class Neuron:
    firing = 0
    firedPreviously = 0
    inhibited = 0
    def __init__(self, name, p, t):
        self.name = name
        self.potential = p
        self.threshold = t

def inhib(N):
    N.potential += 30

date = datetime.datetime.now()


N1 = Neuron('Neuron 1', -70, -55)

N2 = Neuron('Neuron 2', -70, -55)

N3 = Neuron('Neuron 3', -70, -55)

#f = open(str(date) + '.txt', 'w')
ctr = 0


def depolarize(N):
    N.potential += 2

i = 0

# def inhib(N):
#     global inhibCtr
#     if inhibCtr == 0:
#         N.potential -= 30
#     inhibCtr += 1
#     if inhibCtr == 8:
#         inhibCtr = 0
#         N.inhibited = 0
#         N.potential += 40


while i < 1000000:

    if N1.firing == 1:
        N1.firing = 0
        N1.potential = -75

    if N2.firing == 1:
        N2.firing = 0
        N2.potential = -75


    #generating random numbers
    randNum1 = random.randint(4,8)
    if randNum1 != 0:
        randNum1 -= random.uniform(0,1)
    randNum2 = random.randint(4,8)
    if randNum2 != 0:
        randNum2 -= random.uniform(0,1)
    N1.potential += randNum1
    N2.potential += randNum2

    if N1.potential > N1.threshold:
        N1.firing = 1
        N2.inhibited = 1
        N2.potential -= random.randint(6,8)


    if N2.potential > N2.threshold:
        N2.firing = 1
        N1.inhibited = 1
        N1.potential -= random.randint(6,8)



    # if N1.firing == 1:
    #     N3.potential += 20
    #
    # if N2.firing == 1:
    #     N3.potential += 20
    #
    # if N3.potential >= N3.threshold:
    #     N3.firing = 1
    #
    # else:
    #     N3.firing = 0

    #print(str(N3.firing)+', '+str(N3.potential))

    # print('N1:(' + str(N1.potential) + ')' + '\t\tN2:(' + str(N2.potential) + ',' + ')')
    # print(str(N1.firing)+','+str(N2.firing))

    ret = str(N1.firing) + ',' + str(N1.potential)[:6] + ',' + str(N2.firing) + ',' + str(N2.potential)[:6]
    print(ret)
    #f.write(ret+'\n')

    if N3.firing == 1:
        N3.firing = 0
        N3.potential = -70

    # if N1.inhibited == 1 & N2.inhibited == 1:
    #     N1.inhibited = 0
    #     N2.inhibited = 0
    #     N1.potential += random.uniform(10,15)
    #     N2.potential += random.uniform(10,15)
    #
    # if N1.inhibited == 1:
    #     N1.inhibited = 0
    #     N1.potential += random.uniform(25,30)
    #
    # if N2.inhibited == 1:
    #     N2.inhibited = 0
    #     N2.potential += random.uniform(25,30)

    # if N1.inhibited == 1 & N2.inhibited == 1:
    #     N2.inhibited = 0
    #     N1.inhibited = 0


    i += 1
    #time.sleep(1)

#f.close()



