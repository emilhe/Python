# -*- coding: utf-8 -*-

#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import json
import utils
import os.path

## IMPORT DATA ##
json_data=open(r'optimization\data.txt')
data = json.load(json_data)
json_data.close()
json_data=open(r'optimization\meta.txt')
meta = json.load(json_data)
json_data.close()

colors = utils.get_color_map()

idx = 2
for key in data:
    matrix = np.array(data[key])
    avg = matrix.mean(0)
    std = matrix.std(0)
    x = np.arange(0,len(avg))*float(meta[key])

    plt.plot(np.arange(0,len(avg))*float(meta[key]),avg, label = key, color = colors[idx]) 
    plt.errorbar(x[::20],avg[::20],yerr=std[::20], linestyle='None', color = colors[idx])
    
    idx = idx + 1
#    plt.subplot(1,2,idx)

plt.plot([0,0],[0,0.5])
plt.ylim(40,70)
plt.legend()
plt.savefig(r'optimization\algorithms.pdf')
#plt.show()