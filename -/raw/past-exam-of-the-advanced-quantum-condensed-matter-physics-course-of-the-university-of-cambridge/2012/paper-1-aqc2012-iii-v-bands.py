"""Original teaching figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Writes PNG basename to cwd."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

k=np.linspace(-.8,.8,500)
fig,ax=plt.subplots(figsize=(8,4.8),layout='constrained')
curves=[(1+.9*k*k,'#286895',r'Conduction $\Gamma_6$',1.48),(-.22*k*k,'#648a30','Heavy hole',-.1),(-1.2*k*k,'#bc672b','Light hole',-.57),(-.32-.7*k*k,'#884f97',r'Split-off $\Gamma_7$',-.86)]
for e,col,label,yy in curves:ax.plot(k,e,lw=2.2,color=col);ax.text(.84,yy,label,color=col,va='center',fontsize=10)
ax.axvline(0,color='.75',ls=':',lw=1);ax.annotate('',(0,1),(0,0),arrowprops={'arrowstyle':'<->','color':'.3'});ax.text(.04,.5,r'$E_g$',va='center')
ax.annotate('',(-.14,0),(-.14,-.32),arrowprops={'arrowstyle':'<->','color':'.4'});ax.text(-.19,-.18,r'$\Delta_{\rm so}$',ha='right',va='center')
ax.text(-.17,.1,r'$\Gamma_8$: HH/LH degenerate',ha='right',fontsize=9)
ax.set(xlim=(-.9,1.36),ylim=(-1.1,1.8),xlabel='Crystal wavevector along one direction',ylabel='Energy (illustrative units)',title='Illustrative unstrained cubic III-V bands')
ax.set_xticks([-.8,0,.8],[r'$-k$',r'$\Gamma$',r'$+k$']);ax.grid(alpha=.12)
fig.savefig(Path(__file__).stem+'.png',dpi=155,facecolor='white');plt.close(fig)
