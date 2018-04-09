'''

'''
import random
import time
import datetime

# Class Neuron represents a neuron with variables
# representing the current potential, threshold potential,
# whether the neuron is currently firing, and whether the
# neuron is currently inhibited. An object of this class
# must be initialized with the current potential
# (usually the resting potential), and the threshold potential, in
# that order

class Neuron:
    firing = 0
    inhibited = 0
    def __init__(self, p, t):
        self.potential = p
        self.threshold = t

#Both neuron objects are initialized with
#resting potentials of -70(mV) and threshold potentials of
#-55(mV)
N1 = Neuron(-70, -55)
N2 = Neuron(-70, -55)


#This function demonstrates how a neuron fires endogenously
#when it is not coupled with another
def uncoupled_simulation(N):
    i = 0
    while i < 1000000:
        if N.firing == 1:
            print(str(N.potential)[0:6] +' '+ str(N.firing)[0:6])
            N.firing = 0
            N.potential = -75
        potential_increase = random.randint(4,6)
        N.potential += potential_increase
        if N.potential >= N.threshold:
            N.firing = 1
        time.sleep(1)
        i += 1

date = datetime.datetime.now()
f = open(str(date) + '.txt', 'w')


#This function demonstrates the behaviour of two
#synaptically coupled neurons
#The arguments are as follows:
#N1, N2: Neuron objects
#endogenous_ll, endogenous_ul: These provide the range of values
#for the increase in potential in the uninhibited neuron
#inhibited_ll, inhibited_ul: These provide the range of values
#for the increase in potential in the inhibited neuron
def coupled_simulation(N1, N2, endogenous_ll, endogenous_ul, inhibited_ll, inhibited_ul):
    i = 0
    while i < 100000:
        #After a neuron fires it gets hyperpolarized
        if N1.firing == 1:
            N1.firing = 0
            N1.potential = -75
        if N2.firing == 1:
            N2.firing = 0
            N2.potential = -75

        #This increase in potential represents the build-up
        #of potential that happens during endogenous firing
        #when the neuron is not inhibited
        if N1.inhibited == 0:
            N1.potential += random.uniform(endogenous_ll, endogenous_ul)
        #This increase in potential represents the potential
        #increase induced by the inhibitor neuron
        else:
            N1.potential += random.uniform(inhibited_ll, inhibited_ul)
        if N2.inhibited == 0:
            N2.potential += random.uniform(endogenous_ll, endogenous_ul)
        else:
            N2.potential += random.uniform(inhibited_ll, inhibited_ul)

        # If both neurons cross threshold simultaneously
        # they inhibit each other and neither fires
        if (N1.potential >= N1.threshold) & (N2.potential >= N2.threshold):
            N1.potential = -75
            N2.potential = -75

        if N1.potential >= N1.threshold:
            N1.firing = 1
            if N2.inhibited == 0:
                N2.inhibited = 1
                N2.potential = -75
            if N1.inhibited == 1:
                N1.inhibited = 0
        if N2.potential >= N2.threshold:
            N2.firing = 1
            if N1.inhibited == 0:
                N1.inhibited = 1
                N1.potential = -75
            if N2.inhibited == 1:
                N2.inhibited = 0

        #print('N1: ' + str(N1.potential)[0:6] + ' ' + str(N1.firing)[0:6])
        #print('N2: ' + str(N2.potential)[0:6] + ' ' + str(N2.firing)[0:6])
        #print(' ')
        out = str(N1.firing)+ ',' + str(N1.potential)[0:6]+ ',' + str(N2.firing) + ',' + str(N2.potential)[0:6]
        f.write(out+'\n')
        i += 1
        #time.sleep(1)

coupled_simulation(N1, N2, 4, 5, 2, 4)