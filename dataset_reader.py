import numpy as np
import matplotlib.pyplot as plt

print("\nFiles processed are in *.dat format")

file_name=input("Enter the file name without extension: \n")
file_name=file_name+".dat"
input_signal=np.loadtxt(file_name)
length_of_A_scan=len(input_signal)
sample_number=np.linspace(0,length_of_A_scan-1,num=length_of_A_scan)

plt.plot(sample_number,input_signal)
plt.xlabel('Sample Number---->')
plt.ylabel('Amplitude--------->')
plt.title('A-scan Plot')
plt.show()
