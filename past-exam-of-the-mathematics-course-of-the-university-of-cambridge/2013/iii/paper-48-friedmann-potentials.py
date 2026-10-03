"""Original potential sketches. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Emit only own PNG basename to cwd; caller controls MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(1,3,figsize=(11,3.5),dpi=100,facecolor='white')
a=np.linspace(.13,2.25,1000)
for z in ax:
 z.axhline(0,color='black',lw=.9);z.set(xlim=(0,2.3),ylim=(-2.5,2.5),xlabel='Scale factor a',ylabel='Potential V(a)');z.grid(alpha=.18)
ax[0].plot(a,-.5/a+.5*a*a,color='#a65a25',lw=2);ax[0].plot(1,0,'o',color='#a65a25');ax[0].annotate('turnaround',xy=(1,0),xytext=(1.16,-.65),arrowprops={'arrowstyle':'->'},fontsize=10);ax[0].set_title('k = 0, negative Lambda',fontsize=11)
ax[1].plot(a,-.5/a+.5,label='k = +1',color='#a65a25',lw=2);ax[1].plot(a,-.5/a-.5,label='k = -1',color='#236c99',lw=2);ax[1].plot(1,0,'o',color='#a65a25');ax[1].legend(fontsize=10,loc='lower right');ax[1].set_title('Zero Lambda',fontsize=11)
ax[2].plot(a,-.5/a-.5*a*a,color='#236c99',lw=2);ax[2].set_title('k = 0, positive Lambda',fontsize=11);ax[2].text(1.12,.45,'No zero of V',ha='center',fontsize=11)
fig.suptitle('Representative dust curves: rho0 = 3, Lambda = -3, 0 or +3',fontsize=11)
fig.subplots_adjust(left=.065,right=.985,bottom=.16,top=.78,wspace=.38)
fig.savefig(Path.cwd()/'paper-48-friedmann-potentials.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
