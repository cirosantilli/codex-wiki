"""Original plot of exam count data and specified models; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
n=np.arange(1,9);y=np.array([723,244,95,35,8,5,6,5]);N0=2018.5
# Optional background illustration: exact total-reference normalization.
# Maximize Poisson likelihood in B at fixed b=1 using scalar bisection.
e=np.exp(-n)
def score(B):
 mu=N0*e+B*(1-e)
 return np.sum((y/mu-1)*(1-e))
lo,hi=0.,20.
for _ in range(80):
 mid=(lo+hi)/2
 if score(mid)>0:lo=mid
 else:hi=mid
B=(lo+hi)/2
print(f'Fixed b=1, total-reference Poisson background estimate: {B:.8f} counts/s')
x=np.linspace(0,8.5,500)
fig,ax=plt.subplots(figsize=(8.5,5),layout='constrained')
ax.errorbar(n,y,yerr=np.sqrt(y),fmt='o',color='#111827',capsize=3,label='Measured 1 s counts ± estimated SD',zorder=5)
for b,ls in [(1,'-'),(1.1,'--')]:ax.semilogy(x,N0*np.exp(-b*x),lw=2,ls=ls,label=f'Pure attenuation, b = {b:g}')
ax.semilogy(x,(N0-B)*np.exp(-x)+B,lw=1.8,ls='-.',color='#059669',label=f'b = 1 with illustrative background B = {B:.2f}')
ax.set(xlabel='Number of sheets n',ylabel='Count rate (counts/s), logarithmic scale',title='Late counts flatten instead of following a pure exponential',xlim=(0,8.5),ylim=(.15,3000))
ax.grid(alpha=.2,which='major');ax.legend(loc='upper right',fontsize=8.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
