"""Sketch the stable positive-Weiss-temperature paramagnetic response. Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':12,'figure.facecolor':'white'})
t=np.linspace(1.025,4.5,1200)
fig,axes=plt.subplots(1,2,figsize=(10,4.5),layout='constrained')
axes[0].plot(t,1/(t-1),color='#245fa0',lw=2.5,label='Curie–Weiss')
axes[0].plot(t,1/t,color='#777777',linestyle='--',lw=1.5,label='Independent moments')
axes[0].set_ylim(0,8)
axes[0].set_ylabel(r'Scaled susceptibility $\chi\theta/C$')
axes[0].legend(frameon=False)
axes[1].plot(t,t-1,color='#245fa0',lw=2.5)
axes[1].plot([1],[0],'o',color='#245fa0',markerfacecolor='white')
axes[1].set_ylim(0,4)
axes[1].set_ylabel(r'Inverse scaled susceptibility $C/(\chi\theta)$')
for ax in axes:
    ax.axvline(1,color='#ad4828',linestyle=':',lw=1.5)
    ax.set_xlim(.8,4.5)
    ax.set_xlabel(r'Temperature $T/\theta$')
    ax.axvspan(.8,1,color='#eeeeee')
    ax.grid(alpha=.2)
fig.suptitle(r'Positive Weiss temperature: $\chi=C/(T-\theta)$ only for $T>\theta$',fontsize=15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
plt.close(fig)
