"""Original cobweb. Python3.14.4; root pyproject dependencies. Output: CWD."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
F=lambda n:(n-.5)*(n-1)*(2-n)+.5
fig,ax=plt.subplots(figsize=(5.5,4.7),layout='constrained',facecolor='white')
n=np.linspace(0,1.6,800);ax.plot(n,F(n),color='#176b9c',lw=2,label='F(N)');ax.plot(n,n,color='#555555',lw=1,label='Diagonal')
x=1.5;y=0
for k in range(24):
 z=F(x);ax.plot([x,x],[y,z],color='#c65b22',lw=.9,alpha=.85);ax.plot([x,z],[z,z],color='#c65b22',lw=.9,alpha=.85);x,y=z,z
ax.scatter([.5],[.5],color='black',s=25,zorder=5);ax.annotate('Fixed point 1/2',xy=(.5,.5),xytext=(.65,.18),arrowprops=dict(arrowstyle='->',lw=.7),fontsize=10)
ax.scatter([1.5],[0],color='#c65b22',s=24);ax.set(xlim=(0,1.6),ylim=(0,1.6),xlabel='Current value N',ylabel='Next value F(N)',title='Alternating approach from N₀ = 3/2',aspect='equal');ax.legend(frameon=False,loc='upper left');ax.grid(alpha=.12)
fig.savefig('2008-cubic-cobweb.png',dpi=150,facecolor='white')
