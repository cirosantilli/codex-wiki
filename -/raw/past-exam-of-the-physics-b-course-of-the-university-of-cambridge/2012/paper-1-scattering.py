"""Original repulsive Kepler hyperbola with asymptote and turning radius."""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10})
b,s=1.,.55;e=np.sqrt(1+(b/s)**2);qmax=np.arccos(1/e)
q=np.linspace(qmax-.012,-qmax+.012,1800)
n=np.array([-s,b])/np.hypot(s,b);t=np.array([-n[1],n[0]])
r=(b*b/s)/(e*np.cos(q)-1);P=r[:,None]*(np.cos(q)[:,None]*n+np.sin(q)[:,None]*t)
d=s+np.hypot(s,b);D=d*n
fig,ax=plt.subplots(figsize=(7.1,4.5),layout='constrained')
ax.plot(P[:,0],P[:,1],c='#1e75a6',lw=2,label='Repulsive trajectory')
for j in [100,900,1600]:
 if -5.7<P[j,0]<4.2 and -.5<P[j,1]<4.2:ax.annotate('',P[j+12],P[j],arrowprops={'arrowstyle':'->','color':'#1e75a6','lw':2})
ax.plot([-5.7,1],[b,b],'--',c='.55',label='Incoming asymptote')
ax.axhline(0,c='.6',lw=.7);ax.scatter([0],[0],s=65,c='crimson',zorder=6);ax.text(.13,-.27,'Fixed nucleus',color='crimson')
ax.annotate('',(-4.6,b),(-4.6,0),arrowprops={'arrowstyle':'<->','color':'black'})
ax.text(-4.45,.45,r'$b$',fontsize=13)
ax.annotate('',D,(0,0),arrowprops={'arrowstyle':'<->','color':'black'})
ax.text(D[0]*.55-.25,D[1]*.55,r'$d$',fontsize=13)
ax.scatter([D[0]],[D[1]],c='#1e75a6',s=22,zorder=5)
ax.set(xlim=(-5.7,4.2),ylim=(-.5,4.2),xlabel='Horizontal distance / b',ylabel='Vertical distance / b',title=r'Illustrative orbit: $\kappa/(mv^2)=0.55b$')
ax.set_aspect('equal');ax.legend(loc='upper left',fontsize=9);ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-1-scattering.png',dpi=170,facecolor='white');plt.close(fig)
