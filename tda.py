import numpy as np
import matplotlib.pyplot as plt
import os 

import time
start_time = time.time()

from ripser import ripser
from persim import plot_diagrams

from skimage import io
from skimage.transform import resize

im = io.imread("Image033.tif")
#ch1 = im[400:500,400:500,1]

 #plt.show()
    #data = np.random.random((100,2))
    #data = np.loadtxt('data3d.txt', delimiter='\t')

# Resized dimensions

locs = [[200,200],[200,300],[300,300],[300,200]]
for i in range(len(locs)):
    m = locs[i][0]
    n = locs[i][1]
    #was 50
    crop = 100
    N = 21
    ch1 = resize(im[m:m+crop,n:n+crop,1],[N,N], anti_aliasing=True)
    idx = np.indices((N,N))
    x = idx[0].flatten()
    y = idx[1].flatten()
    v = ch1.flatten()*N

    data = np.stack((x,y,v)).T

    plt.figure()
    plt.imshow(ch1)
    plt.savefig("im_"+str(m)+"_"+str(n)+".png")
   


    diagrams = ripser(data,maxdim=1)['dgms']
    print("--- %s seconds ---" % (time.time() - start_time))

    plt.figure()
    plot_diagrams(diagrams)
    plt.savefig("pd_"+str(m)+"_"+str(n)+".png")
