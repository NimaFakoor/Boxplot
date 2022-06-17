import matplotlib.pyplot as plt
import numpy as np
import os

import logging

logging.basicConfig(filename='file.log',format='[%(funcName)s] - %(levelname)s [%(asctime)s] %(message)s' , level=logging.DEBUG) 
   
path = os.getcwd()
logging.info(f' {path} ')
paths = [os.path.abspath(name) for name in os.listdir(".") if os.path.isdir(name)]
logging.info(f' {paths} ')
i = 0
k = 1
c_changed = np.zeros((11, 10), dtype=int)
while k < 11:
    i = 0
    while i < 11:
        path = os.path.join(paths[k - 1], "c" + str(i) + '.txt')
        with open(path, 'r') as f:
            lines = f.readlines()
        for j in range(1, len(lines)):
            c_changed[int(lines[j][-5:-3]), int(paths[k - 1][-1])] += 1
        i += 1

    k += 1

fig = plt.figure(figsize=(10, 7))

data = []
for i in range(11):
    data.append(c_changed[i, :])

# Creating plot
plt.boxplot(data)

fig.savefig('result.png')
# show plot
plt.show()
