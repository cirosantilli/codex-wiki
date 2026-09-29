"""Original exact eight-site Hückel spectrum; Python 3.14.4, matplotlib/numpy."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
roots=np.sort(np.roots([1,0,-4,1]))[::-1]
vals=[(1+np.sqrt(13))/2,roots[0],1,1,roots[1],-1,(1-np.sqrt(13))/2,roots[2]]
labels=['B₁u','B₃g','B₁u','B₂g','B₃g (LUMO)','Aᵤ','B₁u','B₃g']
fig,ax=plt.subplots(figsize=(7.3,5.3),layout='constrained')
for i,(lam,label) in enumerate(zip(vals,labels)):
 y=-lam;x=.58 if i!=3 else 2.3
 if i==2:x=.58
 ax.plot([x,x+1], [y,y],color='#1262a6',lw=2)
 ax.text(x+1.10,y,label,va='center',fontsize=11)
 if i<4:
  ax.text(x+.40,y+.08,'↑↓',ha='center',fontsize=14)
 ax.text(5.2,y,f'λ = {lam:.4f}',va='center',fontsize=10)
ax.set_xlim(0,6.6);ax.set_ylim(-2.8,2.65);ax.set_xticks([]);ax.set_ylabel('(E − α)/|β| = −λ',fontsize=12)
ax.set_title('p-Quinone: eight π electrons in the neutral molecule\nβ < 0; the anion adds one electron to the LUMO',fontsize=12)
ax.spines[['top','right','bottom']].set_visible(False)
fig.savefig(Path(Path(__file__).stem + '.png'),dpi=115,facecolor='white');plt.close(fig)
