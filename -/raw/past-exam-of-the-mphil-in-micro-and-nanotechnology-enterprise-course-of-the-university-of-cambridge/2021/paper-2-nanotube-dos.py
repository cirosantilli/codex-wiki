"""Original explanatory model figure; Python 3.14, NumPy and Matplotlib.
Run from the desired output directory. No exam image or experimental data used.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
fig,axs=plt.subplots(1,2,figsize=(9,4.1),sharey=True,layout='constrained')
e=np.linspace(-3.8,3.8,2400)
for ax,metal in zip(axs,[False,True]):
    edges=[1.6,2.8] if metal else [.7,1.8,2.9]
    dos=np.ones_like(e)*.55 if metal else np.zeros_like(e)
    for gap in edges:
        mask=np.abs(e)>gap
        dos[mask]+=np.abs(e[mask])/np.sqrt(e[mask]**2-gap**2+.012)
    dos=np.minimum(dos,8)
    ax.fill_betweenx(e,0,dos,where=e<0,color='#2479ad',alpha=.65,label='Occupied')
    ax.fill_betweenx(e,0,dos,where=e>0,color='#e79b35',alpha=.65,label='Unoccupied')
    ax.plot(dos,e,color='#333333',lw=.7)
    ax.axhline(0,color='k',ls='--',lw=.8)
    for j,gap in enumerate(edges[:2]):
        x=8.4+j*1.6
        ax.annotate('',(x,gap),(x,-gap),arrowprops=dict(arrowstyle='<->',color='#803d81',lw=1.6))
        ax.text(x+.15,0,rf'$E_{{{j+1}{j+1}}}$',color='#803d81',va='center')
    ax.set(xlim=(0,12),ylim=(-3.8,3.8),xlabel='Density of states (schematic units)',title='Metallic tube' if metal else 'Semiconducting tube')
    ax.set_xticks([])
axs[0].set_ylabel('Energy relative to Fermi level (arbitrary units)')
axs[0].legend(loc='lower right',fontsize=8)
fig.suptitle('One-dimensional subband edges and axial optical transitions')
fig.savefig('paper-2-nanotube-dos.png',dpi=170,facecolor='white')
