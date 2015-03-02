# -*- coding: utf-8 -*-

#!/usr/bin/env python
import json
import numpy as np
import matplotlib.pyplot as plt
import utils

## CHART DEFINITION ##
def make_chart(base_path, file_name, x_labels):
    # Import data.
    json_data=open('{}/{}.txt'.format(base_path,file_name))    
    data = json.load(json_data)
    json_data.close()
    # Read from variables from utils.
    colors = utils.get_color_mappings()
    labels = utils.get_label_mappings()
    # Plot stuff.
    plt.figure(figsize=(7,4))
    ax1 = plt.subplot(111)
    N = len(data['Labels']) + 2 # HACK
    ind = np.arange(N)
    width = 0.75   
    base = np.zeros(N)
    # Order keys correctly.
    orderedKeys = []
    for key in ['Onshore wind', 'Offshore wind', 'Solar', 'Backup', 'Fuel', 'Transmission']:
        if(key in data['Costs']):
            orderedKeys.append(key)

    for key in orderedKeys:
        # Adjust data: HACK!!
        adjustedData = []
        idx = 0
        for point in data['Costs'][key]:
            adjustedData.append(point)
            idx = idx + 1
            if((idx<9) & (idx%3 == 0)): adjustedData.append(0)
        # Plot stuff
        plt.bar(ind, adjustedData, width, bottom = base, color=colors[key], label='{}'.format(labels[key]))    
        base = np.add(adjustedData, base)
    plt.ylabel(u"LCOE [€]") 
    plt.xticks(ind+width/2,x_labels)
    plt.xlim(-1,N+1)
    
     ## PLOT STYLING ##
    plt.rc('text', usetex=True)
    plt.rcParams['text.latex.unicode'] = True 
    plt.rc('font', family='Arial')
    lgd1 = ax1.legend(bbox_to_anchor=(0, -1.5, 1.0, 2.6-3.1*0), loc='upper center', ncol=6, mode="expand", borderaxespad=0.0, prop={'size':8}, numpoints=1,)
    
    # plt.show()
    plt.savefig('{}/{}{}.pdf'.format(base_path,file_name, "VE50"), bbox_inches='tight')
    plt.close();

## EXECUTION ##
base_path = 'costs'
make_chart(base_path,'cost', ['$\\beta$', '$\\nu_{max}$', '$CS$', ' ','$\\beta$', '$\\nu_{max}$', '$CS$', ' ','$\\beta$', '$\\nu_{max}$', '$CS$'])
make_chart(base_path,'costTrans', ['$\\beta$', '$\\nu_{max}$', '$CS$', ' ','$\\beta$', '$\\nu_{max}$', '$CS$', ' ','$\\beta$', '$\\nu_{max}$', '$CS$'])
make_chart(base_path,'costOffshore', ['0\%', '25\%', '50\%', ' ','0\%', '25\%', '50\%', ' ','0\%', '25\%', '50\%'])