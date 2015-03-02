#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import json
import os.path

## CHART DEFINITION ##
def make_chart(base_path, file_name):
    # Import data.
    json_data=open('{}/{}.txt'.format(base_path,file_name))
    data = json.load(json_data)
    countries = []
    wind = []
    onshoreWind = []
    offshoreWind = []
    solar = []

    for country in data:
        countries.append(country)
        gamma = float(data[country]["Gamma"])
        alpha = float(data[country]["Alpha"])
        frac = float(data[country]["OffshoreFraction"])
        wind.append(gamma*alpha)
        solar.append(gamma*(1-alpha))
        onshoreWind.append(gamma*alpha*(1-frac))
        offshoreWind.append(gamma*alpha*frac)
    json_data.close()
    ## PLOT STUFF ##
    N = len(countries)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.75       # the width of the bars: can also be len(x) sequence
    plt.figure(figsize=(10,3))
    plt.bar(ind, onshoreWind,   width, color='darkblue', label='Onshore Wind')
    plt.bar(ind, offshoreWind,   width, color='lightblue', bottom=onshoreWind, label='Offshore Wind')
    plt.bar(ind, solar, width, color='yellow', bottom=wind, label = 'Solar')
    if(not file_name == 'k=1'): plt.plot([-1, N+1], [1,1], color='k', ls='--')
    ## PLOT STYLING ##
    #plt.rc('text', usetex=True)
    plt.ylabel('$\gamma_n$')
    plt.xticks(ind+width/2, countries)
    plt.xlim(-1,N+1)
    #plt.ylim(0,1.5)
    #plt.legend(ncol=2)
#    plt.show()
    plt.savefig('{}/{}.pdf'.format(base_path,file_name), bbox_inches='tight')
    plt.close();

## EXECUTION ##
base_path = 'chromosomes'
for fn in os.listdir(base_path):
    if(os.path.splitext(fn)[1] == '.txt'):
        make_chart(base_path,os.path.splitext(fn)[0])