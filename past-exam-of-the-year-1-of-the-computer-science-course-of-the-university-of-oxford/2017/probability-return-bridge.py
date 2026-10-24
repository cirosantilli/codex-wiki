"""Compare exact returns and conditioned midpoint returns; output PNG to cwd."""
from pathlib import Path
from fractions import Fraction
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
n=np.arange(19)
def p(k):return Fraction(3**(k+1)+(-1)**k,4**(k+1))
returns=[float(p(int(k)))for k in n]
bridge=[float(p(int(k))**2/p(2*int(k)))for k in n]
fig,ax=plt.subplots(figsize=(9,5.2),dpi=100,facecolor='white')
ax.plot(n,returns,'o-',color='#2563a6',ms=4,label='Pr(Mₙ = X)')
ax.plot(n,bridge,'s-',color='#a35217',ms=4,label='Pr(Mₙ = X | M₂ₙ = X)')
ax.axhline(.75,color='#a35217',ls='--',lw=1,label='conditional limit 3/4')
ax.set(xlabel='n',ylabel='probability',xlim=(0,18),ylim=(-.02,1.05),title='Conditioning on a future return changes the midpoint law')
ax.set_xticks(range(0,19,2));ax.grid(alpha=.2);ax.legend(loc='center right',frameon=True)
fig.subplots_adjust(left=.1,right=.97,bottom=.13,top=.9)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white')
plt.close(fig)
