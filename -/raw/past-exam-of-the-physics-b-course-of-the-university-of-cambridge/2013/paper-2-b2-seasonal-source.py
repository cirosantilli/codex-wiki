"""Original explanatory figure; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(10.5,4),layout='constrained',gridspec_kw={'width_ratios':[1.6,1]})
year=np.linspace(0,1,700);angle=2*np.pi*year;air=15-20*np.cos(angle)
axs[0].plot(year,air,color='#2871a1',label='air / ground surface')
for x,col,label in [(np.pi/2,'#b34f28','ground: z = πδ / 2'),(np.pi,'#438a51','ground: z = πδ')]:axs[0].plot(year,15-20*np.exp(-x)*np.cos(angle-x),color=col,label=label)
axs[0].axhline(20,c='gray',ls='--',lw=1,label='indoor temperature')
axs[0].set(xlim=(0,1),ylim=(-7,37),xticks=[0,.25,.5,.75,1],xticklabels=['Jan','Apr','Jul','Oct','Jan'],ylabel='temperature (°C)',title='Attenuation and phase delay with depth');axs[0].legend(loc='upper left',fontsize=8)
x=np.linspace(0,7,600);source=15-20*np.exp(-x)*np.cos(x);cost=(20-source)/293.15
axs[1].plot(x,cost,color='#6a509a');axs[1].axhline(5/293.15,c='gray',ls=':',label='deep-ground limit');xs=3*np.pi/4;ys=(5+20*np.exp(-xs)*np.cos(xs))/293.15;axs[1].scatter([xs],[ys],c='#c53432',zorder=4);axs[1].annotate('minimum at 3π / 4',xy=(xs,ys),xytext=(2.7,.038),arrowprops={'arrowstyle':'->'},fontsize=9)
axs[1].set(xlabel='depth z / δ',ylabel='reversible electrical input / delivered heat',title='Coldest-day input for the same heat');axs[1].legend(loc='upper right',fontsize=8)
for ax in axs:ax.grid(alpha=.2)
fig.suptitle('Seasonal source model; heat extraction neglected')

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
