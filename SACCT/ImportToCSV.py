from enum import Enum
import pickle
with open('test1.pickle', 'rb') as pickle_file:
    [ step_log, gain_log, energy_con_log ] = pickle.load(pickle_file)
print(step_log)

import csv
# class export(Enum):
#     step_log = 1
#     gain_log = 2
#     energy_con_log = 3

# for i in range(1, 4, 1):


export_files = [ 'step_log.csv', 'gain_log.csv', 'energy_con_log.csv' ]

for file in export_files:
    with open(file, 'w') as log_file:
        # file.write('aaaaa\n')
        # file.write(','.join(log_file))
        writer = csv.writer(log_file)
        writer.writerow(step_log)
