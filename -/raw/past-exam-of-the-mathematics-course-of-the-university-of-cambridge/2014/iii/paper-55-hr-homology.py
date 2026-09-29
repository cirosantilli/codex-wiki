"""Illustrative HR homology branches; writes only its PNG basename to cwd.
Supply MPLCONFIGDIR pointing to an owned cache. Python 3.14, numpy/matplotlib.
"""
import os
from pathlib import Path
if not os.environ.get('MPLCONFIGDIR'):
    raise RuntimeError('Supply an owned MPLCONFIGDIR before generating the figure')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
spp=284/69;scno=76/9;join=4.05
fig,ax=plt.subplots(figsize=(7.8,5.2),dpi=100,facecolor='white')
ax.set_facecolor('white')
x=np.linspace(3.45,join,200);ax.plot(x,spp*(x-join),color='#23658d',lw=2.7,label='pp: eta=4, Kramers opacity; slope 284/69')
x=np.linspace(join,4.60,200);ax.plot(x,scno*(x-join),color='#ae482b',lw=2.7,label='CNO: eta=16, electron scattering; slope 76/9')
ax.scatter([join],[0],color='#333333',s=22,zorder=3)
ax.annotate('Illustrative join',xy=(join,0),xytext=(4.38,-1.5),arrowprops={'arrowstyle':'->','color':'#555555'},fontsize=10)
ax.annotate('Increasing mass',xy=(4.48,scno*(4.48-join)),xytext=(4.30,scno*(4.30-join)),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#ae482b'},fontsize=10,rotation=-54)
ax.set_xlim(4.67,3.38);ax.set_ylim(-3,5.2)
ax.set_xlabel(r'$\log_{10}(T_{\rm eff}/{\rm K})$ — hotter to the left')
ax.set_ylabel(r'$\log_{10}(L/L_*)$')
ax.set_title('Fully radiative ideal-gas homology branches',fontsize=13,pad=13)
ax.grid(alpha=.20);ax.legend(loc='upper right',fontsize=9,framealpha=1)
fig.subplots_adjust(left=.12,right=.97,top=.88,bottom=.19)
fig.text(.5,.045,'Slope means d log L / d log T_eff. Normalization and join are schematic.',ha='center',fontsize=9)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
