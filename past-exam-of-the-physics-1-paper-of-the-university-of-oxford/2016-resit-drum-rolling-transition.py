"""Original illustration for the 2016 Oxford Physics 1 resit solutions.
Writes only the matching PNG to the current working directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc
import numpy as np
plt.rcParams.update({"font.size": 10.5, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

a=1.;b=.45;h=a*a/b
fig,axs=plt.subplots(1,3,figsize=(10.5,5.1),layout='constrained',gridspec_kw={'width_ratios':[1.15,1.15,1]})
ax=axs[0]
for rad,col in [(a,'#256da5'),(b,'#777777')]:ax.add_patch(Circle((0,0),rad,fill=False,lw=2,color=col))
ax.plot([-1.35,1.35],[-b,-b],color='black',lw=1.2);ax.plot([0,0],[0,h],ls='--',color='.45',lw=1.3)
ax.annotate('',(.95,h),(0,h),arrowprops={'arrowstyle':'->','lw':2,'color':'#b64127'});ax.text(.1,h+.13,'impulse $J$',color='#b64127')
ax.annotate('',(-.28,h),(-.28,0),arrowprops={'arrowstyle':'<->','color':'.3'});ax.text(-.4,h/2,r'$h=a^2/b$',rotation=90,ha='right',va='center')
ax.annotate('$a$',(.7,.7),(1.05,1),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.text(.06,-.2,'$b$',color='.3');ax.text(-1.2,-.75,'rails under axle',fontsize=9)
ax.text(-1.3,2.7,'Cue line lies outside drum\nwhen axle is smaller',fontsize=10)
ax.set(xlim=(-1.5,1.5),ylim=(-1.3,3.05),title='Formal impulse geometry');ax.set_aspect('equal');ax.axis('off')
ax=axs[1];ax.add_patch(Circle((0,1),1,fill=False,lw=2,color='#256da5'));ax.plot([-1.4,1.4],[0,0],color='black',lw=1.3)
ax.annotate('',(1.15,2.3),(-.2,2.3),arrowprops={'arrowstyle':'->','lw':2,'color':'#256da5'});ax.text(-.2,2.5,'centre moves right',fontsize=9)
ax.add_patch(Arc((0,1),1.2,1.2,theta1=20,theta2=260,color='#b64127',lw=1.7));ax.annotate('',(.56,1.21),(.47,1.4),arrowprops={'arrowstyle':'->','color':'#b64127','lw':1.7});ax.text(-.55,.85,'clockwise\nspin',fontsize=10)
ax.annotate('',(-1,-.18),(.15,-.18),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#b64127'});ax.text(-1.25,-.42,'initial slip backwards',color='#b64127',fontsize=9)
ax.annotate('',(1,-.72),(-.15,-.72),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#288148'});ax.text(-.8,-1,'friction forwards',color='#288148',fontsize=9)
ax.set(xlim=(-1.5,1.5),ylim=(-1.3,3.05),title='Overspin on rough ground');ax.set_aspect('equal');ax.axis('off')
ax=axs[2];v0=b;wf=(1+b)/2;vf=wf
ax.bar([0,1],[v0*v0/2,vf*vf/2],color='#256da5',label='translation')
ax.bar([0,1],[.5,wf*wf/2],bottom=[v0*v0/2,vf*vf/2],color='#ce8a32',label='rotation')
ax.set(xticks=[0,1],xticklabels=['initial','rolling'],ylabel=r'$K/(Ma^2\omega_0^2)$',ylim=(0,.76),title='Total energy decreases')
ax.text(.5,.68,r'$b/a=0.45$',ha='center');ax.legend(loc='lower left',fontsize=9);ax.grid(axis='y',alpha=.18)
fig.suptitle('Drum and axle: radii $a=R/2$, $b=r/2$; $I=Ma^2$',fontsize=13)
fig.savefig(Path.cwd()/'2016-resit-drum-rolling-transition.png',dpi=140,transparent=False);plt.close(fig)
