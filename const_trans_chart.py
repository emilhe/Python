# -*- coding: utf-8 -*-

#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import json
import utils
import os.path

## CHART DEFINITION ##
colors = utils.get_color_mappings()
labels = utils.get_label_mappings()
## IMPORT DATA ##
json_data=open(r'constTrans/trailData.txt')
data = json.load(json_data)
json_data.close()
## PLOT STUFF ##
plt.figure(figsize=(7,4))
ax1 = plt.subplot(111)
# Prepare labels
x_labels = [x for x in data]
x_labels.sort(key = float)
N = len(x_labels)
ind = np.arange(N)
width = 0.75   
base = np.zeros(N)
# Order keys correctly.
orderedKeys = []
for key in ['Backup', 'Fuel', 'Transmission']:
    if(key in data['1']):
        orderedKeys.append(key)
print(orderedKeys)
# Plot data
for sub in orderedKeys:
    lst = []    
    for key in x_labels:
        lst.append(data[key][sub])
    # Plot stuff
    plt.bar(ind, lst, width, bottom = base, color=colors[sub], label=labels[sub])    
    base = np.add(lst, base)
plt.ylabel(u"LCOE [€]") 
plt.xticks(ind+width/2,x_labels)
plt.xlim(-1,N+1)

 ## PLOT STYLING ##
plt.rc('text', usetex=True)
plt.rcParams['text.latex.unicode'] = True 
plt.rc('font', family='Arial')
lgd1 = ax1.legend(bbox_to_anchor=(0, -1.5, 1.0, 2.6-3.1*0), loc='upper center', ncol=6, mode="expand", borderaxespad=0.0, prop={'size':8}, numpoints=1,)

plt.show()
#plt.savefig(r'constTrans\constrained.pdf', bbox_inches='tight')
#plt.close();
