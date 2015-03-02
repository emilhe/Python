#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import json
import os.path

## VARIABLES ##
import utils

colors = utils.get_color_mappings()
y_labels = utils.get_short_label_mappings()
axisTicks = {'Wind':[10,30], 'Onshore wind':[10,30], 'Offshore wind':[10,30], 'Solar':[3,8], 'Transmission':[3,8], 'Fuel':[5,10], 'Backup':[2,4]}

## CHART DEFINITION ##
def make_chart(base_path, file_name): 
    ## IMPORT DATA ##
    json_data=open('{}/{}.txt'.format(base_path,file_name))    
    data = json.load(json_data)
    json_data.close()
    ## PLOT STUFF ##
    fig=plt.figure(figsize=(7,4))
    fig.subplots_adjust(hspace=0)    
    N = len(data['Labels']) + 2 # HACK
    ind = np.arange(N)
    width = 0.75   
#    orderedKeys = ['Wind', 'Solar', 'Backup', 'Fuel', 'Transmission']
    idx = 1
    for key in data['Costs']: #orderedKeys.reverse: #
        # Skip data: HACK!!
        if('Offshore' in key):
            continue
        # Adjust data: HACK!!
        adjustedData = []
        d_idx = 0
        for point in data['Costs'][key]:
            adjustedData.append(point)
            d_idx = d_idx + 1
            if((d_idx<9) & (d_idx%3 == 0)): adjustedData.append(0)
        # Plot stuff
        plt.subplot(6,1,idx)
        plt.bar(ind, adjustedData, width, color=colors[key], label=key)    
        plt.ylabel('${}$'.format(y_labels[key]))
        idx = idx + 1
        plt.xlim(-1,N+1)
        plt.xticks(ind+width/2, ['','','','',''])
        plt.yticks([0, np.round(max(data['Costs'][key])/2)])
#        plt.locator_params(axis = 'y', nbins=3)

#    plt.xticks(ind+width/2, data['Labels'])
    plt.xticks(ind+width/2, ['$\\beta$', '$\\nu_{max}$', '$GA$', ' ','$\\beta$', '$\\nu_{max}$', '$GA$', ' ','$\\beta$', '$\\nu_{max}$', '$GA$'])
    
#    plt.legend(ncol=5)
    plt.show()
#    plt.savefig('{}/{}{}.pdf'.format(base_path,file_name, "VE50split"), bbox_inches='tight')
    plt.close();

## EXECUTION ##
base_path = 'costs'
for fn in os.listdir(base_path):
    if(os.path.splitext(fn)[1] == '.txt'):
        make_chart(base_path,os.path.splitext(fn)[0])