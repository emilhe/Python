# -*- coding: utf-8 -*-

#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import json
import os.path

## IMPORT DATA ##
json_data=open('C:\Users\Emil\Dropbox\highDimTest.txt')    
data = json.load(json_data)
json_data.close()

fig = plt.figure(figsize=(8,4))
ax1 = plt.subplot(2,1,1)
plt.legend()
ax2 = plt.subplot(2,1,2)
plt.legend()

for key in data:
    ax1.errorbar(data[key]["Dim"],data[key]["EvalAvg"], yerr=data[key]["EvalStd"], label = key)
    ax2.plot(data[key]["Dim"],data[key]["Succes"], label = key)

ax1.legend();
ax2.legend();

#plt.show()
