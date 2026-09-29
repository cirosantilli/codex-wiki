"""Plot post-explosion binding regions from relative orbital energy. Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':12,'figure.facecolor':'white'})
fig,axes=plt.subplots(1,2,figsize=(10,4.9),layout='constrained',sharey=True)
q=np.linspace(0,2.5,801)
for ax,sign,title in zip(axes,[1,-1],['Kick along original motion','Kick opposite original motion']):
    boundary=.5*(1+sign*q)**2
    ax.fill_between(q,boundary,1,where=boundary<1,color='#c9dff0',label='bound energy')
    ax.plot(q,boundary,color='#205c96',lw=2)
    ax.axhline(.5,color='#777777',linestyle='--',lw=1)
    ax.text(.06,.52,'half the initial mass retained',fontsize=10,color='#555555')
    ax.set_xlim(0,2.5);ax.set_ylim(0,1)
    ax.set_xlabel(r'Kick / initial relative speed, $q$')
    ax.set_title(title,fontsize=14)
    ax.grid(alpha=.18)
    ax.text(.10,.9,'BOUND',fontsize=13,color='#205c96')
axes[0].set_ylabel(r'Retained total mass fraction $f=M^{\prime}/M_0$')
axes[0].text(1.1,.23,'UNBOUND',fontsize=13,color='#777777')
axes[1].axvline(1,color='#a43c2a',linestyle=':',lw=1.5)
axes[1].text(1.04,.12,'zero angular momentum:\nradial plunge',color='#a43c2a',fontsize=10)
fig.suptitle(r'Bound if $|1\pm q|<\sqrt{2f}$; equality is marginal escape',fontsize=16)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
plt.close(fig)
