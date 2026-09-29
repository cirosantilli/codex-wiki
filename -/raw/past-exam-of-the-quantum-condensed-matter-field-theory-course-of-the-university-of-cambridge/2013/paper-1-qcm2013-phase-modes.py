"""Original teaching plot. Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7. Writes PNG basename to cwd."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

x=np.linspace(0,2,400)
fig,ax=plt.subplots(figsize=(7.1,4.4),layout='constrained')
ax.plot(x,x,lw=2.6,label=r'Neutral: $\omega=c_s k$')
ax.plot(x,np.sqrt(1+x*x),lw=2.6,label=r'Charged bulk: $\omega^2=\omega_p^2+c_s^2k^2$')
ax.annotate('',(0.07,0),(0.07,1),arrowprops={'arrowstyle':'<->','color':'.3'})
ax.text(.12,.48,'Plasma gap',va='center');ax.axhline(1,ls=':',lw=1,color='.6')
ax.set(xlim=(0,2),ylim=(0,2.5),xlabel=r'$c_s k/\omega_p$',ylabel=r'$\omega/\omega_p$',title='Illustrative lossless long-wavelength phase theory')
ax.legend(loc='upper left',fontsize=10);ax.grid(alpha=.15)
fig.savefig(Path(__file__).stem+'.png',dpi=160,facecolor='white');plt.close(fig)
