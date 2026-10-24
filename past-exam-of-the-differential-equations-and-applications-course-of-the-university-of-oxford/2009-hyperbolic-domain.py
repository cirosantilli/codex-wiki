"""Original domain-of-dependence figure. Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
RK4 is used only to draw the boundary ODE, not to obtain the analytic solution.
Run from output directory; dependencies in wiki pyproject.toml.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(0,.8,1201);dx=x[1]-x[0];b=np.ones_like(x)
f=lambda xx,yy:2*np.sqrt(yy*yy+2*xx)
for i in range(len(x)-1):
    a=f(x[i],b[i]);c=f(x[i]+dx/2,b[i]+dx*a/2);d=f(x[i]+dx/2,b[i]+dx*c/2);e=f(x[i]+dx,b[i]+dx*d)
    b[i+1]=b[i]+dx*(a+2*c+2*d+e)/6
fig,ax=plt.subplots(figsize=(7.5,5.1),constrained_layout=True)
ax.fill_between(x,b,6,color='#d8eafa',label='data determine both invariants')
ax.plot(x,b,color='#b43d35',lw=2,label='outgoing plus characteristic')
for a in [1.4,2,3,4,5]:
    k=np.where(b<=a)[0]
    if len(k):ax.plot(x[k],[a]*len(k),color='#3b779d',lw=1)
ax.plot([0,0],[1,6],color='black',lw=3,label='initial half-line')
ax.text(.36,5.4,r'$\lambda_-=0$: horizontal characteristics',fontsize=10)
ax.set(xlim=(0,.8),ylim=(0,6),xlabel='$x$',ylabel='$y$',title=r'Domain determined by data at $x=0$, $y\geq1$')
ax.grid(alpha=.15);ax.legend(loc='lower right',fontsize=8)
fig.savefig('2009-hyperbolic-domain.png',dpi=150,facecolor='white')
