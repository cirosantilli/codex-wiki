"""Original explanatory model figure; Python 3.14, NumPy and Matplotlib.
Run from the desired output directory. No exam image or experimental data used.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
n=np.logspace(0,5,400)
fig,axs=plt.subplots(1,2,figsize=(9.5,4.1),layout='constrained')
for nu,label in [(.5,'Theta: exponent 1/2'),(.588,'Good solvent: exponent 0.588'),(1/3,'Poor, compact: exponent 1/3')]:
    axs[0].loglog(n,n**nu,lw=2,label=label)
axs[0].set(xlabel='Number of statistical segments N',ylabel='Size / segment length (scaling)',title='Conformation in three solvent regimes')
axs[0].legend(fontsize=8)
axs[1].loglog(n,1/n,lw=2,label='Additive monomer drag')
axs[1].loglog(n,.5/np.sqrt(n),lw=2,label='Stipulated effective sphere')
axs[1].set(xlabel='Number of statistical segments N',ylabel='D / single-monomer D',title='Different hydrodynamic assumptions')
axs[1].legend(fontsize=8)
fig.savefig('paper-2-polymer-scaling.png',dpi=170,facecolor='white')
