from enum import Enum
import pickle
import csv

# fileName = 'test0_detail'
fileName = 'test0'
with open(fileName+'.pickle','rb') as pickle_file:
    [step_log,gain_log,energy_con_log] = pickle.load(pickle_file)
    # [show_channel,show_user_number,show_encoding_rate,
    #  show_transcoding,qoe_mismatch,encoding_power,ttpower,request1] = pickle.load(pickle_file)
    
    


# export_files = [fileName+'show_channel.csv',fileName+'show_user_number.csv',
#              fileName+'show_encoding_rate.csv',fileName+'show_transcoding.csv',
#              fileName+'qoe_mismatch.csv',fileName+'encoding_power.csv',
#              fileName+'ttpower.csv',fileName+'request1.csv']
# filesData = [show_channel,show_user_number,show_encoding_rate,
#              show_transcoding,qoe_mismatch,encoding_power,ttpower,request1]
export_files = [ fileName+'_step_log.csv', fileName+'_gain_log.csv', fileName+'_energy_con_log.csv' ]
filesData = [step_log,gain_log,energy_con_log]

        
for counter, files in enumerate(export_files):
    with open(files, 'w') as log_file:
        writer = csv.writer(log_file)
        writer.writerow(filesData[counter])