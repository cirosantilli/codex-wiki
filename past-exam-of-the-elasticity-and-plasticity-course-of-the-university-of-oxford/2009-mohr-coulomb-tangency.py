"""Original normalized Mohr diagram. Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7.
Run from output directory; dependencies in wiki pyproject.toml.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
fig,ax=plt.subplots(figsize=(7.6,5.1),constrained_layout=True)
phi=np.pi/6;C=-2.;R=abs(C)*np.sin(phi);t=np.linspace(0,2*np.pi,600)
ax.plot(C+R*np.cos(t),R*np.sin(t),color='#286c9c',lw=2,label='Mohr circle at first yield')
n=np.linspace(-3.7,0,200)
for sign in [-1,1]:ax.plot(n,sign*(-n)*np.tan(phi),color='#b14d37',lw=1.8,label=r'$|F|=-N\tan\phi$' if sign==1 else None)
N=C*np.cos(phi)**2;F=abs(C)*np.sin(phi)*np.cos(phi)
for sign in [-1,1]:
    ax.plot([C,N],[0,sign*F],':',color='#555555');ax.scatter([N],[sign*F],color='#b14d37',s=25)
ax.scatter([C],[0],color='black',s=18);ax.annotate('$C<0$',(C,0),xytext=(-2.3,-.22))
ax.add_patch(Arc((0,0),1.2,1.2,theta1=150,theta2=180,color='#555555',lw=1))
ax.text(-.8,.13,r'$\phi$',fontsize=12)
ax.axhline(0,color='black',lw=.8);ax.axvline(0,color='black',lw=.8)
ax.set(xlim=(-3.7,.35),ylim=(-2.2,2.2),xlabel=r'$N$ (tension positive)',ylabel='$F$',title='Cohesionless frictional yield: circle tangent to both lines',aspect='equal')
ax.grid(alpha=.13);ax.legend(loc='lower left',fontsize=9)
fig.savefig('2009-mohr-coulomb-tangency.png',dpi=150,facecolor='white')
