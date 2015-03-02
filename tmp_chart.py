# -*- coding: utf-8 -*-

#!/usr/bin/env python
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import json
import utils
import os.path
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

def do_stuff(data):
    keys = []    
    for key in data:
        keys.append(float(key))
        print(key)
    keys = sorted(keys, reverse=True)
    
    labels = []  
    idx = 0      
    for key in keys:
        labels.append(key)        
        plt.plot(np.arange(0,1.1,0.1), data["{}".format(key)], color = colors[idx], linewidth=2 )  
        idx = idx+1
    plt.legend(labels) 
    plt.xticks([0.2,0.4,0.6,0.8])
    plt.ylabel(u"LCOE [€]")
    plt.xlabel('$\\alpha$')

fig = plt.figure(figsize=(10,5))
colors = utils.get_color_map()

## IMPORT DATA ##
json_data=open('sTmp\solarAnalysisWithTransOnshore.txt')
data = json.load(json_data)
json_data.close()
fig.add_subplot(1,2,1)
do_stuff(data)

json_data=open('sTmp\solarAnalysisWithTransOnshoreAndOffshore.txt')
data = json.load(json_data)
json_data.close()
ax1 = fig.add_subplot(1,2,2)
do_stuff(data)    

plt.savefig('sTmp\mixed.pdf',  bbox_inches='tight')
plt.close();