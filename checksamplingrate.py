from scipy.io.wavfile import read as read_wav
import os
#os.chdir('path') # change to the file directory
sampling_rate, data=read_wav("0035.wav") # enter your filename
print sampling_rate