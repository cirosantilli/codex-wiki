# Tested with Python3.14.4,numpy2.3.5,matplotlib3.10.7. Output is written to CWD.
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7,5),facecolor='white')
x=np.linspace(.015,np.sqrt(2),900);lower=1.5*(1-1/x**2);upper=3*x*x/8
ax.fill_between(x,np.maximum(lower,-2),upper,color='#dce9f8',label='Regular sheet connected to the data')
for s in [.2,.4,.6,.8,1]:
 r=np.linspace(-1.3,np.log(2)/2,400);xx=s*np.exp(r);yy=1.5*s*s*(1-np.exp(-2*r));ax.plot(xx,yy,color='#31699c',lw=1)
x2=np.linspace(0,np.sqrt(2),300);ax.plot(x2,3*x2*x2/8,color='#a62e2e',lw=2.2,label=r'First caustic $y=3x^2/8$')
ax.plot(x,lower,color='#24734c',lw=2,label='Endpoint characteristic from s=1')
ax.plot([0,1],[0,0],color='black',lw=3,label='Initial segment')
ax.scatter([0,1],[0,0],color='black',s=20,zorder=5)
ax.set(xlabel='$x$',ylabel='$y$',title='Cubic Charpit equation: characteristics and caustic',xlim=(0,1.5),ylim=(-2,.9))
ax.legend(loc='lower left',fontsize=8);ax.grid(alpha=.18);fig.tight_layout();fig.savefig('2007-charpit-caustic.png',dpi=160,facecolor='white')
