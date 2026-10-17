"""Original explanatory model; output is a basename in the working directory."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':9,'axes.titlesize':10,'axes.labelsize':10})

fig,axs=plt.subplots(1,2,figsize=(9,4),layout='constrained');q=np.linspace(-2,2,600)
for sign in [-1,1]:axs[0].plot(q,sign*abs(q),color='#2166ac',lw=2)
axs[0].axhline(0,ls=':',color='grey');axs[0].text(-1.9,1.7,'Cut through a 2D Dirac cone',fontsize=9);axs[0].set(xlabel=r'$q_x$ (chosen units), $q_y=0$',ylabel='Energy (chosen units)',title='Graphene near one valley');axs[0].grid(alpha=.15)
for sign in [-1,1]:
 axs[1].plot(q,sign*abs(q),color='#777777',ls='--',label='Metallic cut' if sign==1 else None);axs[1].plot(q,sign*np.sqrt(q*q+.6**2),color='#b2182b',lw=2,label='Gapped cut' if sign==1 else None)
axs[1].annotate('',xy=(0,.6),xytext=(0,-.6),arrowprops={'arrowstyle':'<->'});axs[1].text(.12,0,r'$E_g$',va='center');axs[1].set(xlabel=r'$q_\parallel$ (chosen units)',ylabel='Energy (chosen units)',title='Nanotube circumferential quantization');axs[1].legend(fontsize=8);axs[1].grid(alpha=.15)
fig.savefig('paper-1-graphene-nanotube-bands.png',dpi=170,facecolor='white');plt.close(fig)
