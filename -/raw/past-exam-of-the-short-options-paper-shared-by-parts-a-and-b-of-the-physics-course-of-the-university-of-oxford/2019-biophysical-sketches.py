"""Original qualitative biophysical schematics; Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle
import numpy as np
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
fig,axs=plt.subplots(1,3,figsize=(13.8,4.6),layout='constrained')
a,b,c=axs
for ax in (a,b):ax.set_aspect('equal');ax.axis('off');ax.set_xlim(-2,2);ax.set_ylim(-2,2)
a.set_title('Ratchet: both baths at the same T')
angles=(np.repeat(np.arange(12),2)+np.tile([0,.15],12))*2*np.pi/12
r=np.where(np.arange(24)%2==0,1,.78)
a.add_patch(Polygon(np.c_[r*np.cos(angles),r*np.sin(angles)],fc='#dddddd',ec='black'))
a.plot([-.45,.45],[0,0],color='black',lw=3);a.plot([0,0],[-.45,.45],color='black',lw=3)
a.annotate('axle to paddles\nin thermal bath',(0,0),(-1.8,-1.5),arrowprops={'arrowstyle':'->'})
a.plot([.5,1.3],[.88,1.3],lw=4,color='#aa3377');a.plot(1.3,1.3,'ko')
a.annotate('pawl + spring\nalso fluctuate',(.8,1.03),(-1.85,1.4),arrowprops={'arrowstyle':'->'})
a.plot([1.02,1.02,1.5],[.0,-.7,-.7],color='black');a.add_patch(Rectangle((1.3,-1.1),.4,.4,fc='#4477aa'))
a.text(1.5,-1.35,'load',ha='center');a.text(0,-1.95,'No net work at equilibrium',ha='center')
b.set_title('ATP synthase: rotor, stator, catalytic head')
b.add_patch(Rectangle((-1.6,-1.1),3.2,.45,fc='#ddeedd',ec='0.4'))
b.add_patch(Rectangle((-.8,-1.28),1.1,.8,fc='#4477aa',ec='black'))
b.text(-.25,-.9,r'$F_o$: c-ring',ha='center',color='white')
b.add_patch(Rectangle((.4,-1.1),.4,.65,fc='#c96d24'));b.text(.9,-.8,'a',ha='center')
b.annotate(r'$H^+$',(.63,-.4),(1.4,-.1),arrowprops={'arrowstyle':'->'})
b.plot([-.25,-.25],[-.45,.5],color='#aa3377',lw=7)
b.text(-.5,.1,r'$\gamma$ shaft',ha='right')
b.plot([1,1,.5],[-.7,1.15,1.15],color='0.3',lw=4);b.text(1.1,.45,'stator',rotation=90)
for x,y,t in [(-.8,.8,r'$\beta$'),(-.25,1.35,r'$\alpha$'),(.3,.8,r'$\beta$')]:
 b.add_patch(Circle((x,y),.43,fc='#ffeeaa',ec='black'));b.text(x,y,t,ha='center',va='center')
b.text(-.25,1.91,r'$F_1$: $\alpha_3\beta_3$ head',ha='center')
b.text(0,-1.65,'Proton flow → rotation → ATP release',ha='center',fontsize=10)
b.text(0,-1.9,'ATP hydrolysis can reverse rotation',ha='center',fontsize=9)
c.set_title('Point image: Airy intensity profile')
x=np.linspace(-2,2,1601);q=2*np.pi*x
# Bessel J1 from its convergent series; no SciPy dependency.
j=np.zeros_like(q);term=q/2
for m in range(60):
 if m:term*=-(q/2)**2/(m*(m+1))
 j+=term
profile=np.ones_like(q);mask=q!=0;profile[mask]=(2*j[mask]/q[mask])**2
c.plot(x,profile,color='#4477aa',lw=2);c.axvline(.609835,ls=':',color='0.4');c.axvline(-.609835,ls=':',color='0.4')
c.annotate('first zero',(.609835,0),(.9,.45),arrowprops={'arrowstyle':'->'})
c.set_xlabel(r'Image position $x/(M\lambda/\mathrm{NA})$');c.set_ylabel('Normalized intensity');c.set_ylim(0,1.1);c.set_xlim(-2,2)
c.text(0,.75,'M = 100\nNA = 1.3',ha='center')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
