"""Original spacetime construction and enlarged meeting region."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
beta=35/37;tc=25/12;td=1813/864;xd=beta*td
fig,(ax,detail)=plt.subplots(1,2,figsize=(9,5.2),layout='constrained',facecolor='white',gridspec_kw={'width_ratios':[1.2,1]})
for a in [ax,detail]:
 t=np.linspace(0,2.16,500);a.plot(beta*t,t,color='#245c9f',lw=2,label='Lander')
 a.plot([2,2],[0,2.17],color='.2',lw=1.8,label='Earth')
 a.plot([0,2],[0,2],color='#b45309',ls='--',lw=2,label='Outgoing radio')
 a.plot([2,xd],[tc,td],color='#21633d',ls='-.',lw=2,label='Reply radio')
 for x,y,mark in [(0,0,'o'),(2,2,'o'),(2,tc,'s'),(xd,td,'D')]:a.scatter([x],[y],marker=mark,color='black',s=26,zorder=6)
 a.set(xlabel='Position toward Earth (ly)',ylabel='Earth-frame time (yr)');a.spines[['top','right']].set_visible(False)
ax.set(xlim=(-.05,2.2),ylim=(-.05,2.22),aspect='equal',title='Full exchange (equal axis units)')
ax.annotate('A: launch',(0,0),(.2,.12));ax.legend(fontsize=8,loc='upper left')
detail.set(xlim=(1.965,2.005),ylim=(1.98,2.12),title='Near Earth (unequal axis scales)')
for label,x,y,dx,dy in [('B',2,2,-.013,-.007),('C',2,tc,-.013,-.004),('D',xd,td,-.009,.009)]:detail.annotate(label,(x,y),(x+dx,y+dy),arrowprops={'arrowstyle':'-','color':'.4'},fontsize=12)
fig.savefig(Path('paper-1-spacetime.png'),dpi=130,facecolor='white');plt.close(fig)
