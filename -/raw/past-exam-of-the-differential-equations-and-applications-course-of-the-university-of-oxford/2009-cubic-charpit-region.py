"""Original characteristic-chart diagram. Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from output directory; dependencies in wiki pyproject.toml.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7.5,5.4),constrained_layout=True)
Y=np.linspace(.001,np.sqrt(2),700);lower=7-6/Y**2;upper=1+1.5*Y**2
ax.fill_betweenx(1+Y,lower,upper,color='#e0ebf5',label='continuation before first fold')
ax.fill_betweenx(1+Y,np.maximum(1,lower),upper,color='#77aed0',label='forward from initial data')
for s in [.15,.3,.5,.7,.9,1.]:
    t=np.linspace(-1.4,np.log(2)/2,250);x=1+6*s*s*(1-np.exp(-2*t));y=1+s*np.exp(t)
    ax.plot(x,y,color='#365e7a',lw=.8)
ax.plot(lower,1+Y,color='#d07a25',lw=2,label='$s=1$ endpoint curve')
ax.plot(upper,1+Y,'--',color='#b53b39',lw=2,label='fold caustic')
ax.plot([1,1],[1,2],color='black',lw=3,label='initial segment')
ax.scatter([4],[1+np.sqrt(2)],color='#b53b39',s=22)
ax.set(xlim=(-2.5,4.4),ylim=(1,2.55),xlabel='$x$',ylabel='$y$',title='Cubic-gradient characteristic chart')
ax.grid(alpha=.15);ax.legend(loc='upper left',fontsize=8)
fig.savefig('2009-cubic-charpit-region.png',dpi=150,facecolor='white')
