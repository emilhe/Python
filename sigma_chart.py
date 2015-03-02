# -*- coding: utf-8 -*-

#!/usr/bin/env python
import matplotlib.pyplot as plt
import json
import os.path
import utils

def make_chart(base_path, file_name): 
    ## IMPORT DATA ##
    json_data=open('{}/{}.txt'.format(base_path,file_name))
    data = json.load(json_data)
    json_data.close()
    ## PLOT STUFF ##
    fig = plt.figure(figsize=(6,3))
    fig.subplots_adjust(hspace=.30)
    fig.subplots_adjust(wspace=.30)
    # BE plot.
    ax1 = fig.add_subplot(1,2,1)
    utils.fill_chart(data, 'CF')
    plt.ylabel('$\\nu$')
    plt.xlabel('$\\sigma$')
    plt.xticks([0.4,0.6,0.8, 1.0])
    plt.xlim([0.3,1.1])
    # LCOE plot
    ax2 = fig.add_subplot(1,2,2)
    utils.fill_chart(data, 'LCOE')
    plt.ylabel(u"LCOE [€]")    
    plt.xlabel('$\\sigma$')
    plt.xticks([0.4,0.6,0.8, 1.0])
    plt.xlim([0.3,1.1])    
    
    lgd1 = utils.custom_legend(ax1) 
    
    plt.show()
#    plt.savefig('{}/{}.pdf'.format(base_path,file_name), bbox_extra_artists=(lgd1, lgd1),  bbox_inches='tight')
    plt.close();

## EXECUTION ##

base_path = 'sigmas'
for fn in os.listdir(base_path):
    if(os.path.splitext(fn)[1] == '.txt'):
        make_chart(base_path,os.path.splitext(fn)[0])