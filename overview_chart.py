# -*- coding: utf-8 -*-

#!/usr/bin/env python
import matplotlib.pyplot as plt
import json
import os.path
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
import utils

def make_chart(base_path, file_name): 
    ## IMPORT DATA ##
    json_data=open('{}/{}.txt'.format(base_path,file_name))
    data = json.load(json_data)
    json_data.close()
    for key in data:
        print(key)    
    
    ## PLOT STUFF ##
    fig = plt.figure(figsize=(6,6))
    fig.subplots_adjust(hspace=.25)
    fig.subplots_adjust(wspace=.30)
    # BE plot.
    ax1 = fig.add_subplot(2,2,1)
    utils.fill_chart(data, 'BE')
    plt.ylabel('$E^{B}$')
    plt.xlabel('$\\alpha$')
    plt.xticks([0.2,0.4,0.6,0.8])
    # Zoom region
    axins1 = zoomed_inset_axes(ax1,12, loc=1)
    axins1.set_xlim(0.96, 1.00)
    axins1.set_ylim(0.18, 0.20)
    utils.fill_chart(data, 'BE')
    plt.xticks(visible=False)
    plt.yticks(visible=False)  
    # BC plot.
    ax2 = fig.add_subplot(2,2,2)
    utils.fill_chart(data, 'BC')
    plt.ylabel('$\mathcal{K}^{B}$')   
    plt.xlabel('$\\alpha$')
    plt.xticks([0.2,0.4,0.6,0.8])
    # Zoom region
    axins2 = zoomed_inset_axes(ax2, 7, loc=1)
    axins2.set_xlim(0.93, 1.00)
    axins2.set_ylim(0.78, 0.83)
    utils.fill_chart(data, 'BC')
    plt.xticks(visible=False)
    plt.yticks(visible=False)  
    # TC plot.
    ax4 = fig.add_subplot(2,2,3)
    if 'TC' in data:
        utils.fill_chart(data, 'TC', 1e-6)
    plt.ylabel('$\mathcal{K}^{T}$')   
    plt.xlabel('$\\alpha$')  
    plt.xticks([0.2,0.4,0.6,0.8])
    # Zoom region
#    axins4 = zoomed_inset_axes(ax4, 1.2, loc=1)
#    axins4.set_xlim(0.80, 1.00)
#    axins4.set_ylim(1000*1e-3, 1500*1e-3)
#    fill_chart(data, 'TC', 1e-3)
#    plt.xticks(visible=False)
#    plt.yticks(visible=False)  
    # LCOE plot
    ax3 = fig.add_subplot(2,2,4)
    utils.fill_chart(data, 'LCOE')
    plt.ylabel(u"LCOE [€]")    
#    plt.ylabel(unicode('$LCOE$ $[€]$', 'utf-8'))    
    plt.xlabel('$\\alpha$')
    plt.xticks([0.2,0.4,0.6,0.8])
    # Zoom region
    axins3 = zoomed_inset_axes(ax3, 5, loc=1)
    axins3.set_xlim(0.91, 1.00)
    axins3.set_ylim(52.5, 60)
    utils.fill_chart(data, 'LCOE')
    plt.xticks(visible=False)
    plt.yticks(visible=False)    

    lgd1 = utils.custom_legend(ax1,(0, -1.35, 2.3, 2.6-3.1*0))
    
#    plt.show()
    plt.savefig('{}/{}.pdf'.format(base_path,file_name), bbox_extra_artists=(lgd1,lgd1),  bbox_inches='tight')
    plt.close();

## EXECUTION ##
base_path = 'overviews'
for fn in os.listdir(base_path):
    if(os.path.splitext(fn)[1] == '.txt'):
        make_chart(base_path,os.path.splitext(fn)[0])