"""Original schematic; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7; CWD output."""
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7.4,5.4),facecolor='white')
for z in np.linspace(.05,1.12,9):ax.axhline(z,color='#d5e1ec',lw=1)
z=np.linspace(0,.95,160);b=.035+.24*z;ax.fill_betweenx(z,-b,b,color='#eead77',alpha=.8);ax.plot(-b,z,color='#9c5220');ax.plot(b,z,color='#9c5220')
ax.axhline(.66,ls='--',color='#4b75a0');ax.text(.52,.59,'neutral-buoyancy level',fontsize=10);ax.text(.51,.95,'maximum rise / turning cap',fontsize=10);ax.text(-.13,.08,'source',fontsize=10);ax.scatter([0],[0],color='#9c5220',s=35)
for zz in [.2,.4,.6]:
 ax.annotate('',xy=(0,zz+.12),xytext=(0,zz),arrowprops={'arrowstyle':'->','color':'#9c5220','lw':2})
 for sign in [-1,1]:ax.annotate('',xy=(sign*(.035+.24*zz),zz),xytext=(sign*(.35+.24*zz),zz),arrowprops={'arrowstyle':'->','color':'#4b75a0'})
ax.annotate('',xy=(.22,.68),xytext=(.05,.95),arrowprops={'arrowstyle':'->','connectionstyle':'arc3,rad=-.5','color':'#9c5220','lw':2});ax.annotate('',xy=(-.22,.68),xytext=(-.05,.95),arrowprops={'arrowstyle':'->','connectionstyle':'arc3,rad=.5','color':'#9c5220','lw':2})
for sign in [-1,1]:ax.annotate('',xy=(sign*.95,.66),xytext=(sign*.24,.66),arrowprops={'arrowstyle':'->','color':'#9c5220','lw':2})
ax.text(-1.04,.42,'ambient\nentrainment',fontsize=10);ax.text(.52,.45,'lighter ambient upward',fontsize=10);ax.text(-.23,.42,'B > 0',fontsize=10);ax.text(-.23,.82,'B < 0',fontsize=10);ax.text(.55,.72,'lateral intrusion',fontsize=10)
ax.set(xlim=(-1.1,1.65),ylim=(-.05,1.17),ylabel='height (schematic)',title='A plume rises beyond its neutral level before turning');ax.set_xticks([]);fig.tight_layout();fig.savefig('paper-43-stratified-plume.png',dpi=120,facecolor='white');plt.close(fig)
