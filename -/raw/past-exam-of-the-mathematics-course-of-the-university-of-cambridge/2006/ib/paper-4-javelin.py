"""Barn/javelin world lines. Output only paper-4-javelin.png to caller CWD.
Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Uses the caller's MPLCONFIGDIR unchanged. Root pyproject.toml supplies dependencies.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

beta=12/13
s=np.linspace(-5.2,5.2,400)
fig,axs=plt.subplots(1,2,figsize=(11.4,6.2),layout='constrained')
colors={'trail':'#126eae','lead':'#cb6023','entry':'#247547','exit':'#9848a3'}
for ax in axs:
    ax.set_facecolor('white')
    ax.axhline(0,color='0.7',lw=.8)
    ax.axvline(0,color='0.7',lw=.8)
    ax.plot(s,s,'--',color='0.75',lw=.8,label='Light directions')
    ax.plot(-s,s,'--',color='0.75',lw=.8)
    ax.set_ylim(-5,5)
    ax.set_xlim(-4.7,6.5)
    ax.set_aspect('equal',adjustable='box')
    ax.grid(alpha=.18)
    ax.scatter([0],[0],color='black',s=30,zorder=5)
    ax.annotate('A: (0, 0)',(0,0),xytext=(12,-26),textcoords='offset points',fontsize=9,
                bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
axs[0].set_title('Barn rest frame',fontsize=14)
axs[0].set_xlabel(r'$x$ (metres)');axs[0].set_ylabel(r'$ct$ (metres)')
axs[0].plot(beta*s,s,color=colors['trail'],lw=2,label='Javelin trailing end')
axs[0].plot(beta*s+20/13,s,color=colors['lead'],lw=2,label='Javelin leading end')
axs[0].plot(np.zeros_like(s),s,color=colors['entry'],lw=2,label='Barn entrance')
axs[0].plot(np.full_like(s,3),s,color=colors['exit'],lw=2,label='Barn exit')
axs[0].scatter([3],[19/12],color='black',s=30,zorder=5)
axs[0].annotate(r'B: $(3,19/12)$',(3,19/12),xytext=(10,13),textcoords='offset points',fontsize=9,
                bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
axs[1].set_title('Javelin rest frame',fontsize=14)
axs[1].set_xlabel(r"$x'$ (metres)");axs[1].set_ylabel(r"$ct'$ (metres)")
axs[1].plot(np.zeros_like(s),s,color=colors['trail'],lw=2,label='Javelin trailing end')
axs[1].plot(np.full_like(s,4),s,color=colors['lead'],lw=2,label='Javelin leading end')
axs[1].plot(-beta*s,s,color=colors['entry'],lw=2,label='Barn entrance')
axs[1].plot(15/13-beta*s,s,color=colors['exit'],lw=2,label='Barn exit')
axs[1].scatter([4],[-37/12],color='black',s=30,zorder=5)
axs[1].annotate(r'B: $(4,-37/12)$',(4,-37/12),xytext=(-95,-25),textcoords='offset points',fontsize=9,
                bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
for ax in axs:
    ax.legend(loc='upper left',fontsize=8,framealpha=.95)
fig.suptitle('Same events and world lines; different simultaneous time slices',fontsize=14)
fig.savefig('paper-4-javelin.png',dpi=140,facecolor='white',transparent=False)
plt.close(fig)
