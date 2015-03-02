#! /usr/bin/env python
import numpy as np
from pylab import plt
import networkx as nx
from matplotlib.colors import LinearSegmentedColormap
import os.path
import json

EUR = unichr(0x20AC)   
colwidth = (3.425)
dcolwidth = (2*3.425+0.236) 

blue = '#134b7c'
yellow = '#f8ca00'
orange = '#e97f02'
brown = '#876310'
green = '#4a8e05'
lightgreen = '#b9f73e'#'#c9f76f'
red = '#ae1215'
purple = '#4f0a3d'
darkred= '#4f1215'
pink = '#bd157d'
lightpink = '#d89bc2'
aqua = '#47fff9'
darkblue = '#09233b'
lightblue = '#8dc1e0'
grayblue = '#4a7fa2'

blue_cycle = [darkblue, blue, grayblue, lightblue]
long_blue_cycle = []
color_cycle = [blue, red, orange, purple, green, pink, lightblue, darkred, yellow]

au_cdict = {'red': ((0.0,int(yellow[1:3],16)/255.0,int(yellow[1:3],16)/255.0),
(0.5,int(green[1:3],16)/255.0,int(green[1:3],16)/255.0),
(1.0,int(blue[1:3],16)/255.0,int(blue[1:3],16)/255.0)),
'green': ((0.0,int(yellow[3:5],16)/255.0,int(yellow[3:5],16)/255.0),
(0.5,int(green[3:5],16)/255.0,int(green[3:5],16)/255.0),
(1.0,int(blue[3:5],16)/255.0,int(blue[3:5],16)/255.0)),
'blue': ((0.0,int(yellow[5:7],16)/255.0,int(yellow[5:7],16)/255.0),
(0.5,int(green[5:7],16)/255.0,int(green[5:7],16)/255.0),
(1.0,int(blue[5:7],16)/255.0,int(blue[5:7],16)/255.0))}
au_cmap = LinearSegmentedColormap('au_cmap',au_cdict,256)

# Define node positions.
def node_positions():
    pos ={}
    pos['AT']=[0.55,0.45]
    pos['FI']=[.95,1.1]
    pos['NL']=[0.40,0.85]
    pos['BA']=[0.65,0.15]
    pos['FR']=[0.15,0.60]
    pos['NO']=[0.5,1.1]
    pos['BE']=[0.275,0.775]
    pos['GB']=[0.10,1.05]
    pos['PL']=[0.75,0.8]
    pos['BG']=[0.9,0.0]
    pos['GR']=[0.7,0.0]
    pos['PT']=[0.0,0.15]
    pos['CH']=[0.4,0.45]
    pos['HR']=[0.75,0.3]
    pos['RO']=[1.0,0.15]
    pos['CZ']=[0.75,0.60]
    pos['HU']=[1.0,0.45]
    pos['RS']=[0.85,0.15]
    pos['DE']=[0.45,0.7]
    pos['IE']=[0.0,0.95]
    pos['SE']=[0.75,1.0]
    pos['DK']=[0.5,0.875]
    pos['IT']=[0.4,0.2]
    pos['SI']=[0.55,0.3]
    pos['ES']=[0.15,0.35]
    pos['LU']=[0.325,0.575]
    pos['SK']=[0.90,0.55]
    pos['EE']=[1.0,0.94]
    pos['LV']=[0.95,0.83]
    pos['LT']=[0.87,0.72]
    return pos

def eurograph(nodes, flows, path='figures'):
    # Define edge styling
    widths = [1.0,0.5,1.0,2.0,3.0,3.0,3.50,4.0,4.5,5.0]
    alphas = [1.0,0.7,0.8,0.9,1.0,0.6,0.7,0.8,0.9,1.0]
    styles = ['dotted', 'dashed', 'dashed', 'dashed', 'dashed', 'solid', 'solid', 'solid', 'solid', 'solid']       
    labels = ["$\leq$ 10\%", "$\leq$ 20\%", "$\leq$ 30\%", "$\leq$ 40\%", "$\leq$ 50\%", "$\leq$ 60\%", "$\leq$ 70\%", "$\leq$ 80\%", "$\leq$ 90\%", "$\geq$ 90\%"]
    # Define node styling
    colors = au_cmap(np.ones(30))    
    
    # Add nodes.
    G=nx.Graph()
    nodelist=nodes.keys()
    for n in nodelist:
        G.add_node(n)
    # Add edges.
#    scale = max(map(lambda x : x['LinkCapacity'], flows))
    scale = 74.2645866222 # Valid for k = 2
    print(scale)
    for i in range(0,len(flows)):
        rel_weight = flows[i]['LinkCapacity']/scale
        G.add_edge(flows[i]['CountryFrom'], flows[i]['CountryTo'] , weight= rel_weight, color = 'r' if(flows[i]['Type'] == 'DC') else 'k')
    # Inject positions.  
    pos=nx.spring_layout(G)
    for key in nodes.keys():
        pos[key] = nodes[key]   

    # Create figure.
    plt.close('all')
    plt.ioff()
    fig = plt.figure(dpi=400,figsize=(1.7*colwidth,1.7*colwidth*0.75))
    ax1= fig.add_axes([-0.125,0.135,1.25,1.0]) 
    # Draw nodes.
    nx.draw_networkx_nodes(G,pos,node_size=600,nodelist=nodelist,node_color=colors,facecolor=(1,1,1))
    # Draw edges.
    for i in range(0,10):
        edges = [(u,v) for (u,v,d) in G.edges(data=True) if d['color'] == 'k' and d['weight']>0.1*(i) and d['weight']<= (1e6 if (i==9) else 0.1*(i+1))]
        nx.draw_networkx_edges(G,pos,edgelist=edges,width=widths[i],alpha=alphas[i],style=styles[i])
        edges = [(u,v) for (u,v,d) in G.edges(data=True) if d['color'] == 'r' and d['weight']>0.1*(i) and d['weight']<= (1e6 if (i==9) else 0.1*(i+1))]
        nx.draw_networkx_edges(G,pos,edgelist=edges,edge_color='r',width=widths[i],alpha=alphas[i],style=styles[i])
    nx.draw_networkx_labels(G,pos,font_size=13,font_color='w',font_family='sans-serif')
    ax1.set_xlim(-0.2,1.2)
    ax1.set_ylim(-0.2,1.4)
    ax1.axis('off') 
    # Draw x-axis labels.
    ax4= fig.add_axes([-0.075,0.075,1.5,.15])
    for i in range(0,10):
        ax4.vlines(0.06*1.05*(i+1)+0.025,0.6,1.0,linewidth=widths[i],color='k',alpha=alphas[i],linestyles=styles[i])
        ax4.text(0.06*1.05*(i+1)+0.01,0.5,labels[i],fontsize=9,rotation=-60)
    ax4.axis([0.0,1.0,0.0,1.2])
    ax4.axis('off')

    #plt.tight_layout()
#    plt.savefig("./"+path+"/graph_"+title+".pdf")
#    plt.savefig(path)
    fig.savefig(path)
#    plt.show() # display2
    
## EXECUTION ##
base_path = r"transmission"
for fn in os.listdir(base_path):
    split = os.path.splitext(fn)
    if(not '2' in split[0]):
        continue
    if(split[1] == '.txt'):
        json_data=open('{}/{}'.format(base_path,fn))
        data = json.load(json_data)
        json_data.close()
        eurograph(node_positions(), data, '{}\{}.pdf'.format(base_path,split[0]))
        print('{}\{}.pdf'.format(base_path,split[0]))