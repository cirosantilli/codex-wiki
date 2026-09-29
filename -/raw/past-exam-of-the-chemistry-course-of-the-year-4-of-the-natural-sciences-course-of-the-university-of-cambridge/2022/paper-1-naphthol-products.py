"""Original explanatory figure; output basename to the current directory.

Tested with the repository Python 3.14 / NumPy / Matplotlib environment.
"""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import bond, atom, wedge, ring, flow, finish, save
OUT=Path(__file__).stem+'.png'

fig,axs=plt.subplots(1,2,figsize=(10,5.1))
for ax,product in zip(axs,['F','H']):
 left=np.array([(0,.5),(-.866,1),(-1.732,.5),(-1.732,-.5),(-.866,-1),(0,-.5)])
 right=np.array([(0,.5),(.866,1),(1.732,.5),(1.732,-.5),(.866,-1),(0,-.5)])
 ring(ax,left,{0:2,2:2,4:2});ring(ax,right,{1:2,3:2} if product=='F' else {1:2})
 for point,end,t in [(left[2],(-2.5,.9),'MeO'),(left[3],(-2.5,-.9),'MOMO')]:bond(ax,point,end);atom(ax,end,t,size=12)
 if product=='F':
  bond(ax,right[3],(2.5,-.95));atom(ax,(2.8,-1.08),'O-CH2-CH=CH2',size=11)
 else:
  bond(ax,right[3],(2.65,-.85),2);atom(ax,(2.65,-.85),'O',size=14)
  q=right[4];wedge(ax,q,(.1,-2),True);atom(ax,(-.15,-2.25),'CH2CH=CH2',size=11)
  wedge(ax,q,(1.7,-2),False);atom(ax,(2,-2.25),'CH2CH2NO2',size=11)
  ax.text(.1,-2.95,'Racemic quaternary stereocenter;\nketone carbon near 202 ppm',ha='center',fontsize=10)
 finish(ax,(-3.2,4),(-3.4,1.7),'F: allyl ether' if product=='F' else 'H: dearomative conjugate addition')
fig.tight_layout();save(fig,OUT)
