"""Original explanatory figure; Python 3.14, numpy and matplotlib.
Writes a literal PNG basename to cwd. No source-image pixels or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,3,figsize=(12,4),layout='constrained');a,b,c=axs
alpha=np.linspace(.002,2.5,700);s=np.exp(-2*alpha**2)
for phi,lab,col in [(0,'0 (even)','#1766a5'),(np.pi/2,'π/2','#e47a13'),(3*np.pi/4,'3π/4','#709944'),(np.pi,'π (odd)','#c33c29')]:
 D=1+s*np.cos(phi);mean=-alpha*s*np.sin(phi)/D;var=.25-alpha**2*s*(np.cos(phi)+s)/D**2;a.plot(alpha,var,label='φ = '+lab,color=col);b.plot(alpha,mean,color=col)
a.axhline(.25,color='black',ls=':',label='Vacuum variance');a.set(xlabel=r'Input amplitude $|\alpha|$',ylabel=r'$\mathrm{Var}(X_2)$',ylim=(.08,.8),title='True variance about the mean');a.legend(frameon=False,fontsize=8)
b.axhline(0,color='gray',ls=':');b.set(xlabel=r'Input amplitude $\alpha>0$',ylabel=r'$\langle X_2\rangle$',title='Mean generally differs from zero')
phmax=np.arccos(-s);c.fill_between(alpha,-phmax,phmax,color='#1766a5',alpha=.2,label='True squeezing');c.plot(alpha,phmax,color='#1766a5');c.plot(alpha,-phmax,color='#1766a5');c.axhline(np.pi/2,color='gray',ls='--',label='Printed-moment criterion');c.axhline(-np.pi/2,color='gray',ls='--');c.set(xlabel=r'Input amplitude $|\alpha|>0$',ylabel=r'Phase $\phi$',ylim=(-np.pi,np.pi),title='Squeezing range depends on amplitude');c.set_yticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],['−π','−π/2','0','π/2','π']);c.legend(frameon=False,fontsize=8,loc='center right')
fig.savefig('paper-1-cat-variance.png',dpi=150);plt.close(fig)
