"""Original leading-model film profiles. Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7.
Run from output directory; dependencies in wiki pyproject.toml.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7.6,4.7),constrained_layout=True)
C=.948
for t,col in [(.5,'#ba7533'),(2,'#347ea6'),(8,'#548949')]:
    front=t/(1+t);x=np.linspace(0,front,240);h=C*(x+1/(1+t))**(4/3)
    ax.plot(x,h,color=col,lw=2,label=rf'$t={t:g}$');ax.plot([front,front,1.2],[C,0,0],color=col,lw=1,alpha=.8)
x=np.linspace(0,1,350);ax.plot(x,C*x**(4/3),color='black',ls='--',lw=2,label=r'$t\to\infty$')
ax.plot([1,1,1.2],[C,0,0],color='black',ls='--',lw=1.2)
ax.set(xlim=(0,1.2),ylim=(-.025,1.04),xlabel=r'height above contact point $z-z_0$',ylabel='scaled film thickness $H$',title='Coating deposited during a unit total wall stroke')
ax.grid(alpha=.17);ax.legend(fontsize=9)
fig.savefig('2009-blink-film-profile.png',dpi=150,facecolor='white')
