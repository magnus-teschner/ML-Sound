from pydub import AudioSegment
import numpy as np
from scipy.io import wavfile
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go
import plotly

fs_wav, data_wav = wavfile.read("Good_Sounds/3.wav")


#Duration = Number of Samples/Sampling frequency
'''print('Signal Duration = {} seconds'.
      format(data_wav.shape[0] / fs_wav))'''





time_wav = np.arange(0, len(data_wav)) / fs_wav
plotly.offline.iplot({ "data": [go.Scatter(x=time_wav,
                                           y=data_wav[:, 0],
                                           name='left channel'),
                                go.Scatter(x=time_wav,
                                           y=data_wav[:, 1],
                                           name='right channel')]})