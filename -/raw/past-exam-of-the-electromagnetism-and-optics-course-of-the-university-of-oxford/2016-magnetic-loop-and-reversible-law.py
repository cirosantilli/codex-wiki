from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.labelsize': 13})
fig, ax = plt.subplots(figsize=(8.2, 4.8), dpi=130, facecolor='white')
h=np.linspace(-3.5,3.5,701);hc=0.45;br=np.tanh(hc)
ax.plot(h,np.tanh(h+hc),lw=2,color='#2268a3',label='Decreasing applied field')
ax.plot(h,np.tanh(h-hc),lw=2,color='#b13939',label='Increasing applied field')
ax.plot(h,np.tanh(h),lw=1.8,ls='--',color='0.35',label='Reversible tanh model')
ax.axhline(0,color='0.6',lw=.8);ax.axvline(0,color='0.6',lw=.8)
ax.plot([0],[br],'o',color='#2268a3');ax.annotate(r'$B_r/B_m$',xy=(0,br),xytext=(.55,.68),arrowprops={'arrowstyle':'->','color':'0.3'})
ax.plot([-hc],[0],'o',color='#2268a3');ax.annotate(r'$-H_{cB}/H_m$',xy=(-hc,0),xytext=(-2,-.27),arrowprops={'arrowstyle':'->','color':'0.3'})
for lo,hi,shift,color in [(1.5,.9,hc,'#2268a3'),(-1.5,-.9,-hc,'#b13939')]:
 ax.annotate('',xy=(hi,np.tanh(hi+shift)),xytext=(lo,np.tanh(lo+shift)),arrowprops={'arrowstyle':'->','color':color,'lw':2})
ax.set(xlim=(-3.5,3.5),ylim=(-1.17,1.18),xlabel=r'$H/H_m$',ylabel=r'$B/B_m$',title='Illustrative hysteresis and the reversible approximation')
ax.legend(loc='lower right',fontsize=10,frameon=True,facecolor='white')
ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
