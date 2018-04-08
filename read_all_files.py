import numpy as np
import matplotlib.pyplot as plt



for i in range(1,15):
   file_name="newscan"+str(i)+".dat"
   input_signal=np.loadtxt(file_name)
   length_of_A_scan=len(input_signal)
   sample_number=np.linspace(0,length_of_A_scan-1,num=length_of_A_scan)
   plt.figure(i)
   plt.plot(sample_number,input_signal)
   plt.xlabel('Sample Number---->')
   plt.ylabel('Amplitude--------->')
   plt.title('A-scan Plot of '+file_name)
   
plt.show()
