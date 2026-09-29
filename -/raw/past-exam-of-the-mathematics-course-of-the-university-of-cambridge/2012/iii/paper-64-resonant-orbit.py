"""Original Kepler-orbit sketch. Tested Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the desired output directory; respects caller MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

A=3**(-2/3)
Q_PERI=0.002
ECC=1-Q_PERI/A
H=np.sqrt(A*(1-ECC**2))
R_X=np.sqrt(H)

def rotating_position(E):
    E=np.asarray(E)
    t=(E-ECC*np.sin(E))/3
    angle=t+np.pi/3
    X=A*(np.cos(E)-ECC)
    Y=A*np.sqrt(1-ECC**2)*np.sin(E)
    return X*np.cos(angle)+Y*np.sin(angle), -X*np.sin(angle)+Y*np.cos(angle)

fig,ax=plt.subplots(figsize=(8.2001,6.2001),dpi=100,facecolor='white')
fig.subplots_adjust(left=.10,right=.97,bottom=.14,top=.88)
E=np.linspace(0,6*np.pi,24001)
X,Y=rotating_position(E)
ax.plot(X,Y,color='#8a8f98',lw=1.7,label='Three successive orbits')
Ehalf=np.linspace(0,np.pi,8001)
ax.plot(*rotating_position(Ehalf),color='#1669bb',lw=3.0,label='First pericentre to apocentre')
angle=np.linspace(0,2*np.pi,721)
ax.plot(np.cos(angle),np.sin(angle),'--',color='#d4d7dd',lw=1)
ax.plot(R_X*np.cos(angle),R_X*np.sin(angle),':',color='#66a3d0',lw=1)
ax.scatter([0],[0],s=125,marker='*',color='#252b35',zorder=6)
ax.scatter([1],[0],s=80,color='#bf492e',zorder=6)
ax.text(1.03,.025,'Planet',color='#9b351e',fontsize=11)
ax.text(-.055,-.095,'Star',ha='right',fontsize=11)
Ex=np.arccos((1-R_X/A)/ECC)
x,y=rotating_position(Ex)
ax.scatter([x],[y],s=60,color='#1669bb',edgecolor='white',zorder=6)
ax.annotate(r'$r_x$: angular turning point',xy=(x,y),xytext=(.28,.21),fontsize=11,arrowprops={'arrowstyle':'->','color':'#1669bb'},color='#1669bb')
xe,ye=rotating_position(np.pi)
ax.scatter([xe],[ye],s=55,color='#1669bb',zorder=5)
ax.annotate('First apocentre',xy=(xe,ye),xytext=(.51,.77),fontsize=11,arrowprops={'arrowstyle':'->','color':'#1669bb'},color='#1669bb')
p0=rotating_position(0)
ax.annotate('First pericentre',xy=p0,xytext=(-.48,-.26),fontsize=11,arrowprops={'arrowstyle':'->','color':'#1669bb'},color='#1669bb')
for e0,e1 in [(0.65,0.85),(1.9,2.12)]:
    ax.annotate('',xy=rotating_position(e1),xytext=rotating_position(e0),arrowprops={'arrowstyle':'->','color':'#1669bb','lw':1.7})
ax.set_aspect('equal');ax.set_xlim(-1.13,1.24);ax.set_ylim(-1.08,1.08)
ax.set_xlabel(r'$X/a_{\rm pl}$');ax.set_ylabel(r'$Y/a_{\rm pl}$')
ax.set_title(r'High-eccentricity 3:1 resonance: $\phi=\pi$',fontsize=14,pad=12)
ax.grid(alpha=.16);ax.legend(loc='upper left',fontsize=9,framealpha=.97)
fig.text(.5,.035,r'$a/a_{\rm pl}=3^{-2/3}$, $q/a_{\rm pl}=0.002$; one planet period closes the pattern.',ha='center',fontsize=10)
fig.savefig('paper-64-resonant-orbit.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
