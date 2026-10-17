"""Original explanatory model figure; Python 3.14, NumPy and Matplotlib.
Run from the desired output directory. No exam image or experimental data used.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
fig,axs=plt.subplots(1,2,figsize=(9,4),layout='constrained',sharey=True)
for ax,centre in zip(axs,[0,-.65]):
    hc=.5
    ax.plot([-2,centre+hc,centre+hc,2],[-1,-1,1,1],color='#2479ad',lw=2)
    ax.plot([2,centre-hc,centre-hc,-2],[1,1,-1,-1],color='#2479ad',lw=2,label='FM loop')
    ax.axhline(0,color='#777777',lw=.6);ax.axvline(0,color='#777777',lw=.6)
    ax.set(xlim=(-2,2),ylim=(-1.45,1.45),xlabel='Applied field H (arbitrary units)')
    if centre==0:
        h=np.linspace(-2,2,100)
        ax.plot(h,.12*h,color='#d87b28',lw=2,label='AFM, low field')
        ax.set_title('Isolated materials: ideal easy-axis response')
        ax.legend(loc='upper left',fontsize=8)
    else:
        ax.axvline(centre,color='#803d81',ls='--',lw=1)
        ax.text(centre,-1.3,r'$H_E$',ha='center',color='#803d81')
        ax.text(centre-hc,.12,r'$H_-$',ha='center');ax.text(centre+hc,.12,r'$H_+$',ha='center')
        ax.annotate('',(centre+hc,1.2),(centre-hc,1.2),arrowprops=dict(arrowstyle='<->'))
        ax.text(centre,1.24,r'$2H_c$',ha='center')
        ax.set_title('Field-cooled bilayer: negative-bias example')
axs[0].set_ylabel('Magnetization (normalized)')
fig.savefig('paper-2-exchange-bias.png',dpi=170,facecolor='white')
