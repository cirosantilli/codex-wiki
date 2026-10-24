"""Original cubic/hysteresis diagram. Python3.14.4; root pyproject dependencies. Output: CWD."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
P=lambda n:(n-.5)*(n-1)*(2-n)
m=(7-np.sqrt(7))/6;M=(7+np.sqrt(7))/6
fig,(ax,bx)=plt.subplots(1,2,figsize=(10,4),layout='constrained',facecolor='white')
n=np.linspace(0,2.45,1000)
for a,color in [(-.5,'#c65b22'),(0,'#176b9c'),(.5,'#33834c')]:
 ax.plot(n,P(n)+a,color=color,label=f'a = {a:g}')
 ax.scatter([m,M],[P(m)+a,P(M)+a],s=23,color=color,zorder=4)
ax.axhline(0,color='black',lw=.8);ax.set(xlabel='N',ylabel='f(N,a)',ylim=(-1,1.55),title='Vertical shifts of the cubic');ax.legend(frameon=False);ax.grid(alpha=.15)
for lo,hi,style in [(0,m,'-'),(m,M,'--'),(M,2.3,'-')]:
 z=np.linspace(lo,hi,300);bx.plot(-P(z),z,style,color='#176b9c',lw=2)
bx.scatter([-P(m),-P(M)],[m,M],color='#b32940',zorder=4)
a_up=-P(m);a_down=-P(M)
# The other root at each double-root fold follows from the root sum 7/2.
upper=3.5-2*m;lower=3.5-2*M
for a,start,end in [(a_up,m,upper),(a_down,M,lower)]:
 bx.annotate('',xy=(a,end),xytext=(a,start),arrowprops=dict(arrowstyle='->',lw=1.6,color='#b32940'))
bx.plot([],[],'-',color='#176b9c',label='Attracting');bx.plot([],[],'--',color='#176b9c',label='Repelling');bx.plot([],[],color='#b32940',label='Quasistatic jump')
bx.set(xlim=(-.5,.5),ylim=(0,2.35),xlabel='a',ylabel='Equilibrium N',title='Different upward and downward thresholds');bx.grid(alpha=.15);bx.legend(frameon=False,loc='upper left',fontsize=9)
fig.savefig('2008-cubic-graphs.png',dpi=150,facecolor='white')
