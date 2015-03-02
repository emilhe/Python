#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import json
import os.path
import utils

base_path = 'dist'
colors = utils.get_color_mappings()

plt.hist(np.load('{}/{}.npy'.format(base_path, 'DNK_solar')))
solar = np.load('{}/{}.npy'.format(base_path, 'DNK_solar'))    
solar = solar/(156*8766*32)
onshore = np.load('{}/{}.npy'.format(base_path, 'DNK_onshore'))    
onshore = onshore/(3*8766*32)
offshore = np.load('{}/{}.npy'.format(base_path, 'DNK_offshore'))   
offshore = offshore/(3*8766*32)

## PLOT STUFF ##
fig=plt.figure(figsize=(9,3))
fig.subplots_adjust(wspace=.30)
plt.subplot(1,3,1)
plt.title('Solar PV')
plt.hist(solar, color=colors['Solar'])
plt.xlabel('Capacity factor')
plt.ylabel('Occurance')
plt.xticks(np.linspace(0.115, 0.13, 4))
plt.yticks([2,6,10])
plt.subplot(1,3,2)
plt.title('Onshore Wind')
plt.hist(onshore, color=colors['Wind'])
plt.xlabel('Capacity factor')
plt.ylabel('Occurance')
plt.xticks(np.linspace(0.32, 0.62, 4))
plt.yticks([2,4,6,8])
plt.subplot(1,3,3)
plt.title('Offshore Wind')  
plt.hist(offshore, color=colors['Wind'])
plt.xlabel('Capacity factor')
plt.ylabel('Occurance')
plt.xticks(np.linspace(0.49, 0.59, 6))
plt.yticks([2,6,10,14])

# plt.show()
plt.savefig('{}/{}.pdf'.format(base_path,'cf_dist'), bbox_inches='tight')
plt.close()