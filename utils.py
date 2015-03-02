# -*- coding: utf-8 -*-

#!/usr/bin/env python
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import json
import os.path

# Standard label mappings.
def get_label_mappings():
    return {'Wind':'Wind', 'Onshore wind':'Onshore Wind', 'Offshore wind':'Offshore Wind','Solar':'Solar', 'Transmission':'$\mathcal{K}^{T}$', 'Fuel':'$E^{B}$', 'Backup':'$\mathcal{K}^{B}$'}

def get_short_label_mappings():
    return {'Wind':'W', 'Onshore wind':'onW','Offshore wind':'offW','Solar':'S', 'Transmission':'\mathcal{K}^{T}', 'Fuel':'E^{B}', 'Backup':'\mathcal{K}^{B}'}

# Standard color mappings.
def get_color_mappings(name = "rolando"):
    if(name is "rolando"):
        return {'Wind':'darkblue', 'Onshore wind':'darkblue', 'Offshore wind':'lightblue', 'Solar':'yellow', 'Transmission':'green', 'Fuel':'orange', 'Backup':'darkred'}
    return []

# Standard color maps.
def get_color_map(name = "rolando"):
    if(name is "rolando"):
        return ['darkblue', 'orange','green', 'darkred', 'purple']
    return []

# Fills a chart with data from the default JSON object. Currently, default colormap is loaded.
def fill_chart(data, key, scale = 1):
    colors = get_color_map()
    idx = 0
    for subkey in sorted(data[key]):
        plt.plot(data[key][subkey]['BetaX'],np.multiply(data[key][subkey]['BetaY'], scale), color=colors[idx], linewidth=2)
        plt.plot(data[key][subkey]['MaxCfX'],np.multiply(data[key][subkey]['MaxCfY'], scale), color=colors[idx], ls='--', linewidth=2)
        idx = idx +1
    idx = 0
    for subkey in sorted(data[key]):
        plt.plot(data[key][subkey]['GeneticX'],np.multiply(data[key][subkey]['GeneticY'], scale), color=colors[idx], marker='o')
        idx = idx + 1
        
# Creates the custom above-chart legend. Currently, default colormap is loaded.
def custom_legend(axis, anchor = (0, -1.4, 2.3, 2.6-3.1*0)):
    colors = get_color_map()
    patches = []  
    patches.append(mlines.Line2D([],[],color='black', label='$\\beta$ ', linewidth=2))
    patches.append(mlines.Line2D([],[],color='black', label='$\\nu_{max}$', linewidth=2, ls = '--'))
    patches.append(mlines.Line2D([],[],color='black', label='$CS$', marker='o'))
    for k in np.arange(1,4,1):
        patches.append(mpatches.Patch(color=colors[k-1], label='K = {}'.format(k)))
#    patches.sort(key = lambda patch: patch.get_label())
    return axis.legend(handles=patches, bbox_to_anchor=anchor, loc='upper center', ncol=6, mode="expand", borderaxespad=0.0, prop={'size':8}, numpoints=1,)
        
    