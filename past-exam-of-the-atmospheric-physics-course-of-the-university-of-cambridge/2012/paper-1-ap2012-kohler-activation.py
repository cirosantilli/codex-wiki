"""Original teaching plot. Python3.14,NumPy2.3.5,Matplotlib3.10.7. PNG basename written to cwd."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

r=np.geomspace(.06,1.3,600);A=.001;B=1.08e-5;rc=np.sqrt(3*B/A);Sc=np.exp(2*A/(3*rc))
kelvin=np.expm1(A/r)*100;solution=np.expm1(A/r-B/r**3)*100
fig,ax=plt.subplots(figsize=(7.8,4.6),layout='constrained')
ax.semilogx(r,kelvin,lw=2.2,label='Pure-water curvature');ax.semilogx(r,solution,lw=2.5,label='Dilute solution curve')
ax.axhline(.5,ls='--',color='.4',label='Illustrative ambient supersaturation');ax.scatter([rc],[(Sc-1)*100],color='#b25b28',zorder=4)
ax.annotate('Activation maximum',(rc,(Sc-1)*100),(.29,-1.1),arrowprops={'arrowstyle':'->','color':'.4'})
ax.axhline(0,color='.7',lw=.8);ax.set(xlim=(.06,1.3),ylim=(-3.9,2.0),xlabel=r'Wet radius ($\mu$m)',ylabel='Supersaturation (%)',title='Curvature and solute compete');ax.legend(loc='upper right',fontsize=9);ax.grid(alpha=.14)
fig.savefig(Path(__file__).stem+'.png',dpi=155,facecolor='white');plt.close(fig)
