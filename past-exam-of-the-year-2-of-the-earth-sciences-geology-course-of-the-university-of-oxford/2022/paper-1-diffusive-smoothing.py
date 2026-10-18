"""Original mathematical solution diagram; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes its PNG to the current working directory; no source images are copied.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':10})

x=np.linspace(0,2,801);fig,axes=plt.subplots(1,2,figsize=(7.4,3.3),dpi=100)
colors=['#344654','#b34c27','#177ca4']
for t,color in zip([0,1,2],colors):
    axes[0].plot(x,np.exp(-t)*np.cos(2*np.pi*x),color=color,lw=1.8,label=f't / τ = {t}')
    axes[1].plot(x,np.exp(-t)*np.sin(2*np.pi*x)+.6*np.exp(-t/4)*np.sin(np.pi*x),
                 color=color,lw=1.8,label=f't / τshort = {t}')
for ax in axes:
    ax.axhline(0,color='#adb7bd',lw=.7);ax.grid(color='#e5eaed',lw=.6)
    ax.set(xlim=(0,2),xlabel='Distance / reference wavelength',ylabel='Temperature anomaly / A')
    ax.legend(frameon=False,fontsize=8)
axes[0].set_title('One mode: fixed shape, smaller amplitude',fontsize=10)
axes[1].set_title('Two modes: short scales fade faster',fontsize=10)
fig.tight_layout(pad=1,w_pad=2)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
