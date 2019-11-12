
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

#loading dataset into Pandas DataFrame
df = pd.read_csv(url, names=['sepal length','sepal width','petal length','petal width','category'])


features = ['sepal length', 'sepal width', 'petal length', 'petal width']


#Separating out the features
x = df.loc[:, features].values

#Separating out the category
y = df.loc[:,['category']].values

#Standardizing the features
x = StandardScaler().fit_transform(x)

pca = PCA(n_components = 2)

priComp = pca.fit_transform(x)

priDf = pd.DataFrame(data = priComp, columns = ['principal component 1', 'principal component 2'])
finalDf = pd.concat([priDf, df[['category']]], axis = 1)

print(finalDf)


#plot
fig = plt.figure(figsize = (8,8))

ax = fig.add_subplot(1,1,1) 

ax.set_xlabel('Principal Component 1', fontsize = 13)
ax.set_ylabel('Principal Component 2', fontsize = 13)

ax.set_title('PCA Plot', fontsize = 22)

category = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['indigo', 'orange', 'teal']

for category, color in zip(category,colors):
    ind = finalDf['category'] == category
    ax.scatter(finalDf.loc[ind, 'principal component 1'], finalDf.loc[ind, 'principal component 2'], c = color, s = 40)
ax.legend(category)
ax.grid()

