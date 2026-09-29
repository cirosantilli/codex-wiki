from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})

# Original amplitude diagrams; illustrative end/centre mass ratio M/m=2.
fig, axes = plt.subplots(1, 3, figsize=(10.2, 3.7), sharey=True, constrained_layout=True)
x = np.arange(3)
profiles = [(np.ones(3), r"Translation: $\omega^2=0$"),
            (np.array([1.,0.,-1.]), r"Antisymmetric: $\omega^2=k/M$"),
            (np.array([.25,-1.,.25]), r"Symmetric: $\omega^2=k/M+2k/m$")]
for ax, (u, title) in zip(axes, profiles):
    ax.axhline(0,color='.7',lw=1)
    ax.plot(x,u,'-',color='#2166ac',lw=1.5)
    ax.scatter(x,u,s=[130,80,130],c='#2166ac',zorder=3)
    for xi,ui in zip(x,u):
        if ui: ax.annotate('',(xi,ui),(xi,0),arrowprops={'arrowstyle':'->','color':'#b2182b','lw':1.7})
    ax.set(xticks=x,xticklabels=['left M','centre m','right M'],ylim=(-1.22,1.3),title=title)
    ax.grid(axis='y',alpha=.18)
axes[0].set_ylabel('Relative longitudinal displacement')
fig.suptitle('Free three-mass chain: mode amplitudes\nIllustration M = 2m; each mode scaled separately',fontsize=13)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
