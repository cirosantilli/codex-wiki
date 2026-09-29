import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

fig=plt.figure(figsize=(11,7),layout='constrained');gs=fig.add_gridspec(2,2,height_ratios=[1,1.05]);a=fig.add_subplot(gs[0,0]);h=fig.add_subplot(gs[0,1]);r=fig.add_subplot(gs[1,:])
y=np.linspace(-1.05,1.05,700);u=3.5*y**10
a.plot(y,u,'k--',label=r'$U(y)$')
for n in range(3):a.plot(y,u+n+.5,label=fr'$n={n}$')
a.axhline(2.8,color='crimson',ls=':',label=r'$E_F$');a.set(xlim=(-1.05,1.05),ylim=(-.05,4),xlabel='Across strip, y / half-width',ylabel='Energy (chosen units)',title='Confinement and spin-resolved levels');a.legend(ncol=2,fontsize=9,loc='upper center')
h.add_patch(Rectangle((0,0),6,2,facecolor='#edf5fa',edgecolor='k'))
for yy,xx in [(1.75,[.5,2.6,4.7]),(.25,[5.5,3.4,1.3])]:
 for x in xx:h.annotate('',xy=(x+.65*(1 if yy>1 else -1),yy),xytext=(x,yy),arrowprops={'arrowstyle':'->','color':'#17639b','lw':2})
for x,yy,label in [(0,1,'1'),(2,2,'2'),(4,2,'3'),(6,1,'4'),(4,0,'5'),(2,0,'6')]:
 h.plot(x,yy,'ko');h.text(x,yy+(.24 if yy>=1 else -.37),label,ha='center')
# An electron cyclotron orbit at positive B is counterclockwise.
th=np.linspace(0,2*np.pi,100);h.plot(3+.38*np.cos(th),1+.38*np.sin(th),color='gray');h.annotate('',xy=(3,1.38),xytext=(3.12,1.36),arrowprops={'arrowstyle':'->','color':'gray'})
h.text(.25,.85,r'$B=+B_z$ out of page',fontsize=10);h.text(3,2.65,'Arrows: electron motion; probes 2,3,5,6',ha='center',fontsize=10)
h.text(3,-.8,r'$R_H=(V_2-V_6)/I,\quad R_{xx}=(V_2-V_3)/I$',ha='center');h.set(xlim=(-.4,6.4),ylim=(-1.05,2.95),title='Chiral contacts and closed bulk orbit');h.axis('off')
b=np.linspace(.15,.9,1800);nu=1/b;k=np.ones_like(b);s=np.zeros_like(b)
for j in range(1,6):
 z=(nu-j-.5)/.055;k+=.5*(1+np.tanh(z));s+=.085/(np.cosh(np.clip(z,-350,350))**2)
r.plot(b,k/(k*k+s*s),label=r'$|R_H|/R_K$');r.plot(b,s/(k*k+s*s),label=r'$R_{xx}/R_K$',color='crimson')
for n in [2,3,4,5]:
 x=1/n;r.text(x,1/n+.035,fr'$N={n}$',ha='center')
r.set(xlabel=r'$B/(n_sh/e)$',ylabel=r'Resistance / $R_K$',title='Illustrative integer Hall staircase and transition peaks',ylim=(-.02,1.08));r.legend(loc='upper left');r.grid(alpha=.15)
fig.savefig('paper-1-hall-states.png',dpi=155)
