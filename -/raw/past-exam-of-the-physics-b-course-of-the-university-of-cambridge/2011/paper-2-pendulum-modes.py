"""Original three-pendulum mode profiles and release response; Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
fig=plt.figure(figsize=(9.5,5.1),layout='constrained');gs=fig.add_gridspec(2,3,height_ratios=[1,1.25]);colors=['#246d9c','#bd7831','#7a5d9b'];vectors=[[1,1,1],[1,0,-1],[1,-1,1]]
for j,v in enumerate(vectors):
 ax=fig.add_subplot(gs[0,j]);ax.axhline(0,color='grey',lw=.7);ax.plot([1,2,3],v,'o-',color=colors[j],lw=1.8);ax.set(xticks=[1,2,3],xticklabels=['m','M = 2m','m'],ylim=(-1.3,1.35),title=[r'$\omega_0=\sqrt{g/l}$',r'$\omega_a=\sqrt{2g/l}$',r'$\omega_s=\sqrt{3g/l}$'][j]);ax.grid(alpha=.12)
 if j==0:ax.set_ylabel('relative displacement')
t=np.linspace(0,14,1000);c0=.25*np.cos(t);ca=.5*np.cos(np.sqrt(2)*t);cs=.25*np.cos(np.sqrt(3)*t);ys=[c0-ca+cs,c0-cs,c0+ca+cs];ax=fig.add_subplot(gs[1,:])
for j,y in enumerate(ys):ax.plot(t,y,color=colors[j],label=f'x{j+1}/d',lw=1.7)
ax.set(xlabel=r'time $t\sqrt{g/l}$',ylabel='displacement / d',title='Release from rest: (x₁, x₂, x₃) = (0, 0, d), with k/m = g/l');ax.legend(fontsize=8,ncol=3);ax.grid(alpha=.15)
fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
