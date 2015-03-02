# -*- coding: utf-8 -*-

#!/usr/bin/env python
import json
import numpy as np
import matplotlib.pyplot as plt

def make_chart(key):
    # Setting one max_val ensures that the scale is the same across all plots.
    max_val = 7.0/100
    
    fig, ax = plt.subplots()
#    max_val = np.ceil(np.max(np.abs((np.array(data[key])*100))))
    plt.contourf(np.array(data['Alpha']), np.array(data['Gamma']), np.array(data[key]), cmap = 'seismic', vmin = -max_val, vmax = max_val)  
#    formatter = FuncFormatter(mjrFormatter)
    cb = plt.colorbar()
#    cb.ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(x)))
    plt.contour(np.array(data['Alpha']), np.array(data['Gamma']), np.array(data[key]), colors = 'black',  linestyles='-', linewidths = 2) 
    plt.xlim(0.5,1.0)
    plt.ylim(0.5,2.0)
    plt.xlabel('$\\alpha$')
    plt.ylabel('$\gamma$') 

json_data=open(r'modelYear\errorAnalysis.txt')
data = json.load(json_data)
json_data.close()

make_chart('BE')
plt.title('Relative error, $E^B$')
#plt.show()
plt.savefig(r'modelYear\be_error.pdf', bbox_inches='tight')
plt.close()

make_chart('BC')
plt.title('Relative error, $\mathcal{K}^B$')
plt.savefig(r'modelYear\bc_error.pdf', bbox_inches='tight')
#plt.show()
plt.close()

make_chart('TC')
plt.title('Relative error, $\mathcal{K}^T$')
plt.savefig(r'modelYear\tc_error.pdf', bbox_inches='tight')
#plt.show()
plt.close()