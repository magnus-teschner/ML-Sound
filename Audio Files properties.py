# Load various imports
import pandas as pd
import os
import librosa
import librosa.display

from wavfilehelper import WavFileHelper

wavfilehelper = WavFileHelper()

audiodata = []
file_name = []
for i in range(1,11):
    file_name.append("Good_Sounds/"+str(i)+".wav")
for element in file_name:
    data = wavfilehelper.read_file_properties(element)
    audiodata.append(data)

# Convert into a Panda dataframe
audiodf = pd.DataFrame(audiodata, columns=['num_channels', 'sample_rate', 'bit_depth'])
print(audiodf)