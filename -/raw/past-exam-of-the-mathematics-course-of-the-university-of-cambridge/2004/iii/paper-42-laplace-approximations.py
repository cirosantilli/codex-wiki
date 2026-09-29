"""Original Laplace-sum density comparison; Python 3.14, NumPy, Matplotlib.

Write the PNG basename to the caller's current working directory.
"""
from pathlib import Path
from math import factorial,comb,pi,sqrt
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

n=8
scale=sqrt(2*n)
def exact(z):
 s=np.abs(np.asarray(z))*scale
 polynomial=sum(comb(n-1,k)*s**(n-1-k)*factorial(n+k-1)/2**(n+k) for k in range(n))
 return scale*np.exp(-s)*polynomial/factorial(n-1)**2
def edgeworth(z):return np.exp(-np.asarray(z)**2/2)/sqrt(2*pi)
def saddlepoint(z):
 s=np.asarray(z)*scale;y=s/n;d=np.sqrt(1+y*y)
 return scale*np.exp(n*(np.log((1+d)/2)-d+1))/np.sqrt(2*pi*n*d*(1+d))

fig,axes=plt.subplots(1,2,figsize=(8.8,4.1),layout='constrained',facecolor='white')
for ax,z in zip(axes,[np.linspace(-3.4,3.4,401),np.linspace(0,7,401)]):
 ax.set_facecolor('white')
 ax.plot(z,exact(z),color='#222222',lw=2.3,label='Exact')
 ax.plot(z,edgeworth(z),color='#c64624',lw=1.7,ls='--',label='Leading Edgeworth')
 ax.plot(z,saddlepoint(z),color='#166da0',lw=1.7,ls='-.',label='Saddlepoint')
 ax.set_xlabel(r'$z=S_n/\sqrt{2n}$')
 ax.spines[['top','right']].set_visible(False)
axes[0].set_title('Central density');axes[0].set_ylabel('Density of the standardized sum')
axes[0].legend(frameon=False,fontsize=9)
axes[1].set_title('Positive tail');axes[1].set_yscale('log');axes[1].set_ylabel('Density (log scale)')
fig.suptitle('Laplace sums: leading approximations at n = 8')
fig.savefig(Path.cwd()/'paper-42-laplace-approximations.png',dpi=140,facecolor='white',transparent=False)
plt.close(fig)
