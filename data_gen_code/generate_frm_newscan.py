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
#div for different newscan 1-1,2-4,3-6,4-5,5-7,6-5,7-6,8-6,9-1,10-1,11-2,12-4,13-8,14-7
div=7
for signal in rotated_signals:
    plt.figure()
    plt.plot(sample_number,signal)
    plt.xlabel('Sample Number---->')
    plt.ylabel('Amplitude--------->')
    plt.title('Rotated A-scan Plot')
    plt.show()
    std_dev=1
    for k in range(1,11):
        noise=[gauss(0,std_dev) for l in range(length_of_A_scan)]
        temp_sig=signal+np.array(noise)
        plt.figure()
        plt.plot(sample_number,temp_sig)
        plt.xlabel('Sample Number---->')
        plt.ylabel('Amplitude--------->')
        plt.title('Noise added A-scan Plot')
        plt.show()
        decision=input('Do you want to store the plot?')
        if decision=='y':
           noise_added_signals=np.vstack((noise_added_signals,temp_sig))
        std_dev=float(input('Enter std deviation'))
    std_dev=1 

#disable comments upto plt.show() to display the synthetic data
#for signal in noise_added_signals:   
#   plt.figure()
#   plt.plot(sample_number,signal)
    
#plt.show()

#Writing data to file
np.savetxt(fname="/home/kushal/Desktop/Simulation/POC/Ultrasonic_dataset_14/generated_data/genarated_newscan"+str(i)+".dat",X=noise_added_signals,fmt='%1.7e',delimiter=' ')



