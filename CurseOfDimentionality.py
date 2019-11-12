
# coding: utf-8

# In[ ]:


import numpy as np
import random
from scipy.spatial.distance import pdist
import math

n = [0] * 1800
dimension = [0] * 1800
gamma_e = [0] * 1800
gamma_c = [0] * 1800
values = [0] * 1800
dist = [0] * 1800
city_dist = [0] * 1800

dist_min = [0] * 1800
dist_max = [0] * 1800

cdist_min = [0] * 1800
cdist_max = [0] * 1800

i = 0

for i in range(0,300):
    #Part 1
    #randomly generating number of n-points and d-dimensions
    n[i] = random.randint(100,1000)
    dimension[i] = random.randint(1,100)

    print(i)
    print(n[i])
    print(dimension[i])

    #generating values of n-points and d-dimensions
    values[i] = np.random.random_integers(low = 1, high = 100, size = (n[i], dimension[i]))

    for j in range(n[i]):
        print(values[i])

    #Part 2
    #calculating Euclidean distance of the randomly generated n-points
    dist[i] = pdist(values[i], 'euclidean')
    print(dist[i])

    #finding minimum distance
    dist_min[i] = np.amin(dist[i])

    #finding maximum distance
    dist_max[i] = np.amax(dist[i])

    print(dist_min[i])
    print(dist_max[i])

    #Part 3
    #calculating gamma - first
    if(dist_min[i] > 0):
        gamma_e[i] = math.log((dist_max[i] - dist_min[i]) / dist_min[i])
        print(gamma_e[i])

    #computing distance using l1 norm (city block)
    city_dist[i] = pdist(values[i], 'cityblock')
    print(city_dist[i])

    cdist_min[i] = np.amin(city_dist[i])
    cdist_max[i] = np.amax(city_dist[i])
    
    print(cdist_min[i])
    print(cdist_max[i])

    #calculating gamma - second
    if(cdist_min[i] > 0):
        gamma_c[i] = math.log((cdist_max[i] - cdist_min[i]) / cdist_min[i])
        print(gamma_c[i])



# In[96]:


from mpl_toolkits import mplot3d

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[88]:


ax = plt.axes(projection = '3d')
ax.scatter3D(n, dimension, gamma_e, c= gamma_e, depthshade = True, s=30)
ax.set_xlabel('n')
ax.set_ylabel('d')
ax.set_zlabel('gamma');
ax.set_title('3D plot of γ(d, n) : Euclidean distance')
plt.show()


# In[93]:


axc = plt.axes(projection = '3d')
axc.scatter3D(n, dimension, gamma_c, c = gamma_c, depthshade = True, s=25)
axc.set_xlabel('n')
axc.set_ylabel('d')
axc.set_zlabel('gamma');
axc.set_title('3D plot of γ(d, n) : l1 norm')
plt.show()

