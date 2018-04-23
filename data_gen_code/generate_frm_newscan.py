import math
from random import gauss
import numpy as np
import matplotlib.pyplot as plt


#i----> File index of Newscan
#j----> Rotation index
#k----> std_dev_factor

# Loading data from the file using numpy 
i=14
file_name="/home/kushal/Desktop/Simulation/POC/Ultrasonic_dataset_14/newscan"+str(i)+".dat"
input_signal=np.loadtxt(file_name)

# Creating sample numbers for plotting/indexing
length_of_A_scan=len(input_signal)
sample_number=np.linspace(0,length_of_A_scan-1,num=length_of_A_scan)


#Finding mean and variance of the input signal
input_mean=np.mean(input_signal)
input_stddev=np.std(input_signal)


#division factor can be changed to change rotation factor
rotated_signals=input_signal;
rotate_by=int(length_of_A_scan/15);

#Rotating signal to simulate flaws at different position
for j in range(9):
      temp_rot=np.roll(input_signal,(j+1)*rotate_by)
      rotated_signals=np.vstack((rotated_signals,temp_rot))

#Adding gaussian noise to simulate noise due to grain or due to system
noise_added_signals=input_signal


for signal in rotated_signals:
    #plt.figure()
    #plt.plot(sample_number,signal)
    #plt.xlabel('Sample Number---->')
    #plt.ylabel('Amplitude--------->')
    #plt.title('Rotated A-scan Plot')
    #plt.show()
    std_dev=np.arange(1,5,0.4)
    std_mean=np.arange(input_mean+50,input_mean+80,3)
    for k in range(1,11):
        noise=[gauss(std_mean[k-1],std_dev[k-1]) for l in range(length_of_A_scan)]
        temp_sig=signal+np.array(noise)
        #plt.figure()
        #plt.plot(sample_number,temp_sig)
        #plt.xlabel('Sample Number---->')
        #plt.ylabel('Amplitude--------->')
        #plt.title('Noise added A-scan Plot')
        #plt.show()
        noise_added_signals=np.vstack((noise_added_signals,temp_sig))
    

#disable comments upto plt.show() to display the synthetic data
#for signal in noise_added_signals:   
#   plt.figure()
#   plt.plot(sample_number,signal)
    
#plt.show()

#Writing data to file
np.savetxt(fname="/home/kushal/Desktop/Simulation/POC/Ultrasonic_dataset_14/generated_data/genarated_newscan"+str(i)+".dat",X=noise_added_signals,fmt='%1.7e',delimiter=' ')



