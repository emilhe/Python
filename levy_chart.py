# -*- coding: utf-8 -*-

#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import json
import os.path

## IMPORT DATA ##
json_data=open(r'levy\sym1mio.txt')
sym = json.load(json_data)
json_data.close()
json_data=open(r'levy\asym1mio.txt')
asym = json.load(json_data)
json_data.close()

start = -10
end = 10
step = 0.01
weight = np.ones_like(sym)/len(sym)/step

fig = plt.figure(figsize=(8,4))

#plt.subplot(1,2,1)
plt.hist(asym, np.arange(start,end, step), weights=weight, histtype="stepfilled", alpha = 0.5, label = "$\\alpha$ = 0.5, $\\beta$ = 1")
plt.hist(sym, np.arange(start,end, step), weights=weight, histtype="stepfilled", alpha = 0.5, label = "$\\alpha$ = 1.5, $\\beta$ = 0")
plt.ylim(0,0.5)
plt.xlim(-10,10)
#plt.subplot(1,2,2)
#plt.title(u"Lévy $\\alpha$-stable distributions")
plt.legend()
# plt.show()
plt.savefig('levy\levy.pdf', bbox_inches='tight')
