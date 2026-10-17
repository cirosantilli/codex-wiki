"""Original explanatory figure; Python3.14, NumPy2.3.5, Matplotlib3.10.7.
Write the PNG basename in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(9.6,4.8),layout='constrained')
ax=axs[0];levels=[0,2.48,5.32]
for y,label in zip(levels,[r'${}^3P$ ground term',r'${}^1D_2$',r'${}^1S_0$']):
 ax.plot([0,1],[y,y],color='.3',lw=1.6);ax.text(1.05,y,label,va='center')
ax.annotate('',xy=(.2,2.48),xytext=(.2,5.32),arrowprops={'arrowstyle':'->','lw':2,'color':'#6e5598'});ax.text(.25,3.9,'436.3 nm',color='#6e5598',rotation=90,va='center')
ax.annotate('',xy=(.65,0),xytext=(.65,2.48),arrowprops={'arrowstyle':'->','lw':2,'color':'#287baf'});ax.text(.71,1.1,'495.9 / 500.7 nm',color='#287baf',rotation=90,va='center')
ax.set(xlim=(-.15,1.9),ylim=(-.45,6),xticks=[],ylabel='Approximate excitation energy (eV)',title='Oxygen ion: schematic levels');ax.spines[['top','right','bottom']].set_visible(False)
T=np.linspace(6000,30000,500);R=7.9*np.exp(32900/T)
axs[1].semilogy(T,R,color='#287baf',lw=2);axs[1].set(xlabel=r'Electron temperature $T_e$ (K)',ylabel=r'$(I_{4959}+I_{5007})/I_{4363}$',title='Low-density Maxwellian approximation');axs[1].grid(alpha=.2)
fig.savefig('paper-1-oxygen-thermometer.png',dpi=165)
