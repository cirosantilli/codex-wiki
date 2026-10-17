"""Original figure. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; PNG basename written to cwd."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

x=np.linspace(-4,4,1200);V=1.4*np.exp(-x*x/2);E=.65;turn=np.sqrt(2*np.log(1.4/E))
fig,ax=plt.subplots(figsize=(8,4.3),layout='constrained')
ax.plot(x,V,lw=2.6,label=r'Illustrative $V(x)$');ax.axhline(E,ls='--',color='#a04b20',label='Incident energy')
ax.fill_between(x,E,V,where=V>=E,color='#f3c58a',alpha=.55,label='Forbidden interval')
for xx,tag in [(-turn,r'$x_1$'),(turn,r'$x_2$')]:ax.plot([xx,xx],[0,E],':',color='.35');ax.text(xx,-.065,tag,ha='center')
ax.text(-2.9,.23,r'Oscillatory'+'\n'+r'$p^2>0$',ha='center');ax.text(2.9,.23,r'Oscillatory'+'\n'+r'$p^2>0$',ha='center');ax.text(0,.91,'Evanescent',ha='center')
ax.set(xlabel='Position (illustrative units)',ylabel='Energy (illustrative units)',xlim=(-4,4),ylim=(-.12,1.65),title='WKB oscillation, turning points and tunnelling');ax.legend(loc='upper right',fontsize=9);ax.grid(alpha=.12)
fig.savefig(Path(__file__).stem+'.png',dpi=155,facecolor='white');plt.close(fig)
