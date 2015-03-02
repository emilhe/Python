# -*- coding: utf-8 -*-

#!/usr/bin/env python
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import json
import os.path
import utils

## VARIABLES ##
styles = ['solid', 'dashed']            
subLabels = ['$\\beta$', '$\\nu_{max}$']   

def make_chart(base_path, file_name):
    ## IMPORT DATA ##
    json_data=open('{}/{}.txt'.format(base_path,file_name))
    data = json.load(json_data)
    json_data.close()
    
    fig = plt.figure(figsize=(6,3))
    fig.subplots_adjust(hspace=.30)
    fig.subplots_adjust(wspace=.30)
    idx = 1
    axes = []
    for scale in data:     
        print(scale)
        # Include scale = 1 reference?
        if('1,' in scale):
            continue
        axes.append(fig.add_subplot(1,2,idx))
        utils.fill_chart(data, scale)
        plt.xticks([0.2,0.4,0.6,0.8])
        plt.ylabel(u"LCOE [€]")
        plt.xlabel('$\\alpha$') 
        idx = idx + 1 
    lgd1 = utils.custom_legend(axes[0])
    
#    plt.show()
    plt.savefig('{}/{}.pdf'.format(base_path,file_name), bbox_extra_artists=(lgd1,lgd1),  bbox_inches='tight')
#    plt.close();

## Execution
base_path = 'solar'
for fn in os.listdir(base_path):
    if(os.path.splitext(fn)[1] == '.txt'):
        make_chart(base_path,os.path.splitext(fn)[0])