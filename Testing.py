import Simulation



N1 = Simulation.Neuron(-70, -55)
N2 = Simulation.Neuron(-70, -55)

file_no = 1

for i in range(2, 9, 2):        #represents endogenous_ll
    for j in range(i+2, 11, 2):  #represents endogenous_ul
        for m in range(1, j//2):  #represents inhibited_ll
            for n in range(m+1, j//2):  #represents inhibited_ul
                for p in range(j//3, j//2): #represents inhibition
                    Simulation.coupled_simulation(N1, N2, i, j, m, n, str(file_no), p)
                file_no += 1
