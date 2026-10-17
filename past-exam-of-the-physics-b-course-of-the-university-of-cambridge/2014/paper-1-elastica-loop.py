"""Original explanatory calculation. Python 3.14, numpy and matplotlib.
Writes one literal PNG basename to cwd; no source-image pixels or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,(a,b)=plt.subplots(1,2,figsize=(9,4),layout='constrained');u=np.linspace(-6,6,1400);X=u-2*np.tanh(u);Y=2/np.cosh(u);theta=4*np.arctan(np.exp(u));curv=2/np.cosh(u)
a.plot(X,Y,lw=2);a.scatter([0],[2],color='#c33c29');a.annotate('height 2/α',(0,2),(.9,2.25),arrowprops=dict(arrowstyle='->'),fontsize=9);a.axhline(0,color='gray',lw=.8);a.set(xlabel=r'$\alpha x$',ylabel=r'$\alpha y$',ylim=(-.15,2.6),title='Analytic ideal loop; thickness/contact ignored');a.set_aspect('equal')
b.plot(u,theta/np.pi,label=r'$\theta/\pi$');b.plot(u,curv,label=r'$\theta\prime/\alpha$');b.set(xlabel=r'$\alpha s$',ylabel='Scaled angle or curvature',title=r'$\alpha=\sqrt{T/(EI)}$');b.axvline(0,color='gray',ls=':');b.legend(frameon=False)
fig.savefig('paper-1-elastica-loop.png',dpi=150);plt.close(fig)
