import numpy as np

def force_by_frequency(frequency, force_arr): #creates list of force values based on frequency of DIC
    force_array = np.array(force_arr)
    #print(force_array)
    choose_every = int(10/frequency)
    freq_force_array = force_array[0::choose_every]
    return freq_force_array.tolist()
    #print(freq_force_array)
    #print(force_array)