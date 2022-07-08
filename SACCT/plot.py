import pickle
import matplotlib.pyplot as plt
import numpy as np
with open('test1_PC.pickle', 'rb') as pickle_file:
    [step_log,gain_log,energy_con_log] = pickle.load(pickle_file)

    epoch_log = np.array(step_log).reshape((-1, 201)).sum(axis=1)
    print(epoch_log.shape)



    fig, axs = plt.subplots(2, 2)
    axs[0,0].plot(step_log)
    axs[0,1].plot(gain_log)
    axs[1,0].plot(energy_con_log)
    axs[1,1].plot(epoch_log)
    plt.show()







