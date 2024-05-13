%matplotlib inline

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_breast_cancer 

cancer = load_breast_cancer()
 
X = []
for target in range(2): 
  X.append([[], [], []])
  for i in range(len(cancer.data)):   
      if cancer.target[i] == target:
         X[target][0].append(cancer.data[i][0])
         X[target][1].append(cancer.data[i][1])
         X[target][2].append(cancer.data[i][2])

colours = ("r", "b") 
fig = plt.figure(figsize=(18,15))
ax = fig.add_subplot(111, projection='3d') 
for target in range(2):
    ax.scatter(X[target][0],
               X[target][1],
               X[target][2],
               c=colours[target])

ax.set_xlabel("mean radius") 
ax.set_ylabel("mean texture") 
ax.set_zlabel("mean perimeter") 
plt.show()