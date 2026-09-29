"""Original explanatory model figure; Python 3.14, NumPy and Matplotlib.
Run from the desired output directory. No exam image or experimental data used.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
fig,ax=plt.subplots(figsize=(8,4.2),layout='constrained')
for q in range(4):
    y=q+1
    for j in range(q+1):
        x=j-(q/2)
        ax.plot([x-.3,x+.3],[y,y],color='#2479ad',lw=2)
        ax.annotate('',(x-.1,y+.40),(x-.1,y+.04),arrowprops=dict(arrowstyle='->',color='#555555'))
        ax.annotate('',(x+.1,y+.04),(x+.1,y+.40),arrowprops=dict(arrowstyle='->',color='#555555'))
    ax.text(2.3,y+.1,rf'$q={q}$: {q+1} orbitals, {2*(q+1)} spins',va='center')
    ax.text(2.3,y-.22,f'Closed shell: {(q+1)*(q+2)} electrons',fontsize=9,color='#803d81')
ax.set(xlim=(-2,6.4),ylim=(.6,4.8),ylabel=r'Energy / $\hbar\omega_0$',yticks=[1,2,3,4],xticks=[],title='Two-dimensional harmonic shells with spin degeneracy two')
ax.spines['bottom'].set_visible(False)
fig.savefig('paper-2-shell-filling.png',dpi=170,facecolor='white')
