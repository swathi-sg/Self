import numpy as np
import matplotlib.pyplot as plt

file = open(r"/home/swat/Desktop/Grammy/posty7.txt","r+")  
#print(file.read()) 
lyrics=file.read()
lyrics=lyrics.split('\n')
lyrics=' '.join(lyrics)
lyrics=lyrics.split(' ')

p=list(filter(lambda x:lyrics[x]=='',range(len(lyrics))))

l=len(lyrics)
arr=np.zeros((l,l))

for i in range(l):
    for j in range(l):
        if lyrics[j]==lyrics[i]:
            arr[i,j]=1
        else:
            arr[i,j]=0
    
plt.imshow(arr, cmap='hot', interpolation='nearest')
plt.savefig('wow.png')
plt.show()

