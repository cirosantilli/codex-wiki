"""Original qualitative CVD sketches; Python 3.14, numpy and matplotlib.

Output is a PNG basename in the current directory, as required by Makefile.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

fig,axes=plt.subplots(1,2,figsize=(10,4.4),layout='constrained')
fig.patch.set_facecolor('white')
for ax in axes:
    ax.set(xlim=(0,10),ylim=(0,7))
    ax.axis('off')

def arrow(ax,a,b,label=None,color='#33748c'):
    ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'-|>','lw':1.7,'color':color})
    if label:
        ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.25,label,ha='center',fontsize=10)

ax=axes[0]
ax.set_title('Delivery-limited example: cold-wall flow reactor',fontsize=11.5)
ax.add_patch(Rectangle((1.1,1.5),7.8,3.8,fc='#f5f8fa',ec='#3d5261',lw=1.6))
ax.add_patch(Rectangle((2.3,1.8),5.3,.55,fc='#e5a080',ec='#9f4e2c'))
ax.add_patch(Rectangle((2.3,2.35),5.3,.3,fc='#627d7a',ec='#365650'))
ax.plot([2.3,7.6],[2.7,2.7],color='#355a93',lw=3)
xs=np.linspace(2.1,8,100)
ax.plot(xs,3.0+.23*np.sqrt(xs-2.1),ls='--',color='#6a8ca7')
ax.text(4.3,3.5,'Gas boundary layer',fontsize=10,color='#496f89')
for y in [4.1,4.7]:arrow(ax,(.2,y),(9.6,y))
arrow(ax,(4.7,3.5),(4.7,2.75),color='#496f89')
ax.text(5,5.6,'Controlled flow; cool chamber walls',ha='center',fontsize=10)
ax.text(4.9,1.0,'Hot substrate / susceptor',ha='center',fontsize=10)
ax.text(5,.25,r'$k_s\gg h_m$: control transport and depletion',ha='center',fontsize=11)
ax=axes[1]
ax.set_title('Surface-reaction-limited example: hot-wall tube',fontsize=11.5)
ax.add_patch(Rectangle((1.0,2.0),8,2.7,fc='#fff5ee',ec='#56616c',lw=1.6))
for y in [1.65,5.05]:
    x=np.linspace(1,9,180)
    ax.plot(x,y+.12*np.sin(8*np.pi*(x-1)/8),color='#b55b36',lw=2)
for x in np.linspace(2.4,7.5,6):
    ax.add_patch(Rectangle((x,2.4),.14,1.9,fc='#5d7c83',ec='#35515a'))
arrow(ax,(.1,3.3),(1.9,3.3),'Feed')
arrow(ax,(8.3,3.3),(9.8,3.3),'Pump')
ax.text(5,5.65,'Uniform-temperature heated zone',ha='center',fontsize=10)
ax.text(5,1.0,'Wafer batch; rapid delivery at low pressure',ha='center',fontsize=10)
ax.text(5,.25,r'$k_s\ll h_m$: control surface temperature',ha='center',fontsize=11)
fig.savefig('paper-1-additional-cvd.png',dpi=160,facecolor='white')
plt.close(fig)
