"""Original explanatory model figure; Python 3.14, NumPy and Matplotlib.
Run from the desired output directory. No exam image or experimental data used.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
fig,axs=plt.subplots(3,1,figsize=(7.5,5.3),sharex=True,layout='constrained')
t=np.linspace(0,np.pi,200)
for j,ax in enumerate(axs,1):
    radius=1/(2*j)
    for k in range(j):
        centre=(2*k+1)*radius
        ax.plot(centre-radius*np.cos(t),radius*np.sin(t),color='#2479ad',lw=2)
    ax.axhline(0,color='#555555',lw=2)
    ax.scatter([0,1],[0,0],c=['#d87b28','#803d81'],s=40,zorder=5)
    ax.set(xlim=(-.08,1.08),ylim=(-.06,.56),yticks=[],ylabel=rf'$j={j}$',title=rf'$|B_j|={j}B_1={j*.1806562913:.3f}\ \mathrm{{T}}$',aspect='equal')
    ax.spines[['left','bottom']].set_visible(False)
axs[-1].set_xticks([0,.5,1],['Opening 1','Separation / L','Opening 2'])
fig.suptitle('Specular semicircle connections, L = 1 µm\nUnoriented paths: field polarity selects the carrier direction',fontsize=11)
fig.savefig('paper-2-electron-focusing.png',dpi=170,facecolor='white')
