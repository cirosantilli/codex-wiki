"""Generate the opaque 1000x360 two-channel diagram into cwd.
Tested: Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,axes=plt.subplots(1,2,figsize=(10,3.6),dpi=100,facecolor='white')
fig.subplots_adjust(left=.025,right=.975,bottom=.11,top=.83,wspace=.16)
for ax,anti in zip(axes,[False,True]):
 ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
 for y in [.76,.24]:
  ax.plot([.09,.91],[y,y],color='#222222',lw=2)
  sign=-1 if anti and y==.24 else 1
  for left,right in [(.22,.36),(.66,.80)]:
   if sign<0:left,right=right,left
   ax.annotate('',xy=(right,y),xytext=(left,y),arrowprops=dict(arrowstyle='-|>',mutation_scale=15,color='#222222',lw=1.8))
 t=np.linspace(0,1,600)
 ax.plot(.5+.017*np.sin(2*np.pi*8*t),.24+.52*t,color='#246ba1',lw=2)
 ax.plot([.5,.5],[.24,.76],'o',ms=5,color='#222222')
 ax.text(.055,.85,r'$\nu_e(p)$',fontsize=14)
 ax.text(.79,.85,r'$e^-(p\prime)$',fontsize=14)
 ax.text(.055,.10,r'$\bar u(k)$' if anti else r'$d(k)$',fontsize=14)
 ax.text(.79,.10,r'$\bar d(k\prime)$' if anti else r'$u(k\prime)$',fontsize=14)
 ax.text(.57,.49,r'$W^+$',fontsize=15,color='#246ba1')
 ax.set_title('Up antiquark target' if anti else 'Down quark target',fontsize=13,pad=8)
fig.suptitle('Charged-current exchange: antiquark arrows reverse fermion flow',fontsize=13,y=.96)
fig.savefig(Path.cwd()/'paper-305-neutrino-scattering.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
