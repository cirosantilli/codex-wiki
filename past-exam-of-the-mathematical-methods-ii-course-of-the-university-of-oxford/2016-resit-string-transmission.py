"""String amplitudes and power fractions at density ratio nine."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,(ax,bars)=plt.subplots(1,2,figsize=(10,4.6),layout='constrained',gridspec_kw={'width_ratios':[2.5,1]})
x=np.linspace(-2*np.pi,0,700);xr=np.linspace(0,np.pi,700);phase=.7
inc=np.cos(x-phase);ref=-.5*np.cos(-x-phase);trans=.5*np.cos(3*xr-phase)
ax.plot(x,inc,ls='--',color='.6',lw=1,label='incident')
ax.plot(x,ref,ls=':',color='#a33',lw=1.5,label='reflected')
ax.plot(x,inc+ref,color='#176ca6',lw=2,label='total on light string')
ax.plot(xr,trans,color='#d57420',lw=2,label='transmitted on heavy string')
ax.axvline(0,color='.35',lw=.9);ax.axhline(0,color='.6',lw=.6)
ax.set(title='One instant; displacement and slope match at x = 0',xlabel=r'$k_1x$',ylabel=r'$y/A$',ylim=(-1.7,1.7));ax.legend(fontsize=8,loc='lower left');ax.grid(alpha=.15)
bars.bar(['Reflected','Transmitted'],[.25,.75],color=['#a33','#d57420'])
for i,y in enumerate([.25,.75]):bars.text(i,y+.04,f'{y:.0%}',ha='center',fontsize=12)
bars.set(title='Incident power = 1',ylabel='Power fraction',ylim=(0,1));bars.grid(axis='y',alpha=.15)
fig.suptitle(r'$k_2=3k_1,\quad r=-1/2,\quad t=1/2$',fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
