"""Population lifetime regions; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run in mirrored _media cwd; outputs only the basename PNG.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
fig,axs=plt.subplots(1,2,figsize=(8.4,3),dpi=120,facecolor='white')
red='#c67556';blue='#7199bf'
m=np.linspace(.2,3,1200);endms=8/m**2;endgiant=10/m**2
ax=axs[0];ax.set_facecolor('white')
ax.fill_between(m,endms,np.minimum(endgiant,10),where=endms<10,color=red,alpha=.8)
ax.fill_between(m,endgiant,10,where=endgiant<10,color=blue,alpha=.7)
ax.plot(m,endms,color='#333333',lw=1.2);ax.plot(m,endgiant,color='#333333',ls='--',lw=1.2)
ax.text(1.55,3.5,r'$t=10/m^2$',fontsize=10);ax.text(1.95,.7,r'$t=8/m^2$',fontsize=10)
ax.set(xlim=(.2,3),ylim=(0,10),xlabel=r'Birth mass $m=M/M_\odot$',ylabel='Present age t (Gyr)',title='Mass–age regions')
x=np.linspace(0,.065,1000);low=20*x;high=25*x
ax=axs[1];ax.set_facecolor('white')
ax.fill_between(x,low,np.minimum(high,1),where=low<1,color=red,alpha=.8)
ax.fill_between(x,high,1,where=high<1,color=blue,alpha=.7)
ax.plot(x,low,color='#333333',lw=1.2);ax.plot(x,high,color='#333333',ls='--',lw=1.2)
ax.text(.013,.69,'White dwarfs',fontsize=10,ha='center',va='center',rotation=60)
ax.text(.031,.69,'Giants',fontsize=10,ha='center',va='center',rotation=67)
ax.text(.050,.47,'Main sequence',fontsize=10,ha='center',rotation=65)
ax.set(xlim=(0,.065),ylim=(0,1),xlabel=r'Mass-tail coordinate $X=0.04/m^2$',ylabel=r'Age coordinate $Y=t/(10\,\mathrm{Gyr})$',title='Uniform coordinates (zoom near X=0)')
for ax in axs:ax.grid(alpha=.12)
fig.legend(handles=[Patch(facecolor=red,label='Red giants'),Patch(facecolor=blue,label='White dwarfs')],loc='lower center',ncol=2,frameon=False,bbox_to_anchor=(.5,0),fontsize=10)
fig.subplots_adjust(left=.065,right=.985,bottom=.23,top=.87,wspace=.25)
fig.savefig('paper-322-population-regions.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
