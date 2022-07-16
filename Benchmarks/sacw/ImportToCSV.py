from enum import Enum
import pickle

fileName = 'test0'
fileLocal = 'test0_PC.pickle'
with open(fileName+'.pickle', 'rb') as pickle_file:
    [step_log, gain_log, energy_con_log] = pickle.load(pickle_file)
    
    
#print(step_log, gain_log, energy_con_log)#Print to terminals?
import csv
export_files = [ fileName+'step_log.csv', fileName+'gain_log.csv', fileName+'energy_con_log.csv' ]
filesData = [step_log, gain_log, energy_con_log]
# export_files = [ fileName+'step_log.csv', fileName+'gain_log.csv', fileName+'energy_con_log.csv' ]
# filesData = [step_log, gain_log, energy_con_log]

        
for counter, files in enumerate(export_files):
    with open(files, 'w') as log_file:
        writer = csv.writer(log_file)
        writer.writerow(filesData[counter])