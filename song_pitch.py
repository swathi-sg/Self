import requests
#from bs4 import BeautifulSoup
import numpy as np
from scipy.spatial import distance
#import plotly.plotly as py
#import plotly.graph_objs as go 
#import plotly.offline as offline 
import matplotlib.pyplot as plt 

#Access_token should be provided 
acc_tok= ''


#obtaining pitch vectors of a track
track_uri='7GN9CSWLwN1rjoMEZ6PQlV'
url2='https://api.spotify.com/v1/audio-analysis/'+track_uri+'?access_token='+acc_tok
req2=requests.get(url2)
single_track=req2.json()


#ss=single_track['segments']
#print(type(ss))

seg_len=len(single_track['segments'])

seg_pitch_vec=[]

for k in range(seg_len):
    pitch_vec=[]
    for x in range(12):
        vec=single_track['segments'][k]['pitches'][x]
        pitch_vec.append(vec)
    seg_pitch_vec.append(pitch_vec)
    
new_len=len(seg_pitch_vec)
  
pitch_arr=np.array(seg_pitch_vec)
#print(pitch_arr)
    
out_arr=np.zeros((new_len,new_len)) 

for y in range(new_len):
    for z in range (new_len):
        out_arr[y,z]=distance.euclidean(pitch_arr[y],pitch_arr[z])

print(out_arr)

"""
#PLOTTING
plot_x_y=np.arange(new_len).reshape(1,new_len)
trace=go.Heatmap(z=out_arr,x=plot_x_y,y=plot_x_y)
data=[trace]
#py.iplot(data, filename='labelled-heatmap')
figure=go.Figure(data=data)
offline.plot(figure)
"""

plt.imshow(out_arr, cmap='hot', interpolation='nearest')
plt.savefig('wow.png')
plt.show()
        
    
