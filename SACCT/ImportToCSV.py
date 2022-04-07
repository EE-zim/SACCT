from enum import Enum
import pickle
with open('test0_detail.pickle', 'rb') as pickle_file:
    [ step_log, gain_log, energy_con_log ] = pickle.load(pickle_file)
    
    
#print(step_log, gain_log, energy_con_log)#Print to terminals?
import csv
export_files = [ 'step_log.csv', 'gain_log.csv', 'energy_con_log.csv' ]
filesData = [step_log, gain_log, energy_con_log]

# for data in filesData:
#     with open(str(data)+'.csv', 'w') as log_file:
#         writer = csv.writer(log_file)
#         writer.writerow(step_log)
        
for counter, files in enumerate(export_files):
    with open(files, 'w') as log_file:
        writer = csv.writer(log_file)
        writer.writerow(filesData[counter])