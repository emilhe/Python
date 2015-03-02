# -*- coding: utf-8 -*-

#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import json
import os.path

## IMPORT DATA ##
json_data=open('C:\Users\Emil\Dropbox\Master Thesis\Python\sTmp\distsNew.txt')    
data = json.load(json_data)
json_data.close()

start = -3
end = 3
step = 0.02
weight = np.ones_like(data['LevyOld'])/len(data['LevyOld'])/step

keys = ['SimpleLevy', 'Levy', 'Bug']

idx = 1
for key in data:
    print(key)
#    plt.subplot(1,2,idx)
    plt.hist(data[key], np.arange(start,end, step), weights=weight, histtype="stepfilled", label = key)
    plt.title(key)
    plt.legend()
    idx = idx+1

plt.plot([0,0],[0,0.5])

     ## PLOT STYLING ##
#    plt.rc('text', usetex=True)
#    plt.rcParams['text.latex.unicode'] = True 
#    plt.rc('font', family='Arial')
#    lgd1 = ax1.legend(bbox_to_anchor=(0, -1.5, 1.0, 2.6-3.1*0), loc='upper center', ncol=6, mode="expand", borderaxespad=0.0, prop={'size':8}, numpoints=1,)
#    


#plt.show()    

#    plt.savefig('{}/{}{}.pdf'.format(base_path,file_name, "VE50"),  bbox_inches='tight')
#    plt.close();
