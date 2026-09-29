"""Original cylinder/plane image-charge construction; write PNG to cwd."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.size':10})
a,H=1.,2.;s=np.sqrt(H*H-a*a)
x,z=np.meshgrid(np.linspace(-3.6,3.6,401),np.linspace(.015,4.4,301))
rp=np.hypot(x,z-s);rm=np.hypot(x,z+s)
V=np.log(rm/rp);V=np.ma.masked_where(x*x+(z-H)**2<=a*a,V)
fig,ax=plt.subplots(figsize=(6.4,5.1),layout='constrained')
cs=ax.contour(x,z,V,levels=[.15,.3,.5,.75,1.,1.2],colors='#226b9c',linewidths=1)
ax.clabel(cs,fmt='%.2f',fontsize=8)
ax.add_patch(Circle((0,H),a,facecolor='#dde2e6',edgecolor='black',lw=1.7,zorder=3))
ax.text(.05,H+.22,'Metal',ha='center',zorder=5)
ax.scatter([0],[s],c='crimson',s=44,zorder=6);ax.text(.12,s-.1,r'$+\lambda$',color='crimson',zorder=6)
ax.scatter([0],[-s],c='royalblue',s=44,zorder=6);ax.text(.12,-s-.1,r'$-\lambda$ (fictitious)',color='royalblue')
ax.axhline(0,c='black',lw=2);ax.fill_between([-3.6,3.6],[-2.1,-2.1],[0,0],color='#f0f0f0')
ax.text(-3.25,.1,'Grounded plane: V = 0',fontsize=9)
ax.plot([0,0],[-s,s],ls='--',c='.6',lw=.8)
ax.annotate('',(0,H),(-a,H),arrowprops={'arrowstyle':'<->','color':'black'},zorder=5)
ax.text(-.58,H+.08,r'$a$',zorder=5)
ax.set(xlim=(-3.6,3.6),ylim=(-2.1,4.3),xlabel=r'$x/a$',ylabel=r'$z/a$',title=r'Cylinder centre at $H=2a$; image height $s=\sqrt{3}a$')
ax.set_aspect('equal');ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-1-cylinder-images.png',dpi=170,facecolor='white');plt.close(fig)
