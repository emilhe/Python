# -*- coding: utf-8 -*-

#!/usr/bin/env python
import json

import matplotlib.pyplot as plt

def un_wrap(data,key):
    x = []
    y = []
    for year in sorted(map(int, data[key].keys())):
        x.append(year+1979)
        y.append(data[key][str(year)])
    return (x, y)

def make_chart(data, color, titles, ylabel):
    centreX, centreY = un_wrap(data, 'centre')

    fig = plt.figure(figsize=(8,5))
    fig.subplots_adjust(hspace=.50)
    fig.subplots_adjust(wspace=.30)
    ax = plt.subplot(2,1,1)
    aMinX, aMinY = un_wrap(data, 'aMin')
    aMaxX, aMaxY = un_wrap(data, 'aMax')
    
    plt.plot(aMinX,aMinY, color = color)
    plt.plot(aMaxX,aMaxY, color = color)
    plt.plot(centreX,centreY, color = 'black')
    ax.fill_between(aMinX, aMinY, aMaxY, facecolor=color, interpolate=True, alpha = 0.25)
    plt.plot([1980,2010], [1,1], '--', color='black')
    plt.xlim(1979,2010)    
    plt.locator_params(nbins=5)
#    plt.title(titles[0])    
    plt.xlabel('Year')    
    plt.ylabel(ylabel)
    
    ax = plt.subplot(2,1,2) 
    gMinX, gMinY = un_wrap(data, 'gMin')
    gMaxX, gMaxY = un_wrap(data, 'gMax')
    
    plt.plot(gMinX,gMinY, color = color)
    plt.plot(gMaxX,gMaxY, color = color)
    plt.plot(centreX,centreY, color = 'black')
    ax.fill_between(gMinX, gMinY, gMaxY, facecolor=color, interpolate=True, alpha = 0.25)
    plt.plot([1980,2010], [1,1], '--', color='black')
    plt.xlim(1979,2010)
    plt.locator_params(nbins=5)
#    plt.title(titles[1])
    plt.xlabel('Year')    
    plt.ylabel(ylabel)
    
# Do BE
json_data=open(r'modelYear\be.txt')
data = json.load(json_data)
json_data.close()

titlesBe = []
titlesBe.append("Backup energy with $\gamma = 1.00$ and $\\alpha \in$[0.5:1]")
titlesBe.append("Backup energy with $\\alpha = 0.75$ and $\gamma \in$[0.5:2]")
ylabel = '$E^B_i / E^B$'
make_chart(data,'orange', titlesBe, ylabel)
#plt.show()
plt.savefig(r'modelYear\be.pdf', bbox_inches='tight')
plt.close();

# Do BC
json_data=open(r'modelYear\bc.txt')
data = json.load(json_data)
json_data.close()

titlesBc = []
titlesBc.append("Backup capacity with $\gamma = 1.00$ and $\\alpha \in$[0.5:1]")
titlesBc.append("Backup capacity with $\\alpha = 0.75$ and $\gamma \in$[0.5:2]")
ylabel = '$\mathcal{K}^B_i / \mathcal{K}^B$'
make_chart(data,'darkred', titlesBc, ylabel)
plt.savefig(r'modelYear\bc.pdf', bbox_inches='tight')
plt.close();

# Do TC
json_data=open(r'modelYear\bc.txt')
data = json.load(json_data)
json_data.close()

titlesTc = []
titlesTc.append("Transmission capacity with $\gamma = 1.00$ and $\\alpha \in$[0.5:1]")
titlesTc.append("Transmission capacity with $\\alpha = 0.75$ and $\gamma \in$[0.5:2]")
ylabel = '$\mathcal{K}^T_i / \mathcal{K}^T$'
make_chart(data,'green', titlesTc, ylabel)
plt.savefig(r'modelYear\tc.pdf', bbox_inches='tight')
plt.close();