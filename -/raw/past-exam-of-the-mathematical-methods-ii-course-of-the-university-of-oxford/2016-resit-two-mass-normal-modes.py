"""Normal modes and an initial-value solution for a string with two point masses."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(2,2,figsize=(9.6,7.2),layout='constrained')
for ax,values,title in [(axes[0,0],[0,1,1,0],r'Lower mode: $(y_1,y_2)\propto(1,1)$'),(axes[0,1],[0,2,-1,0],r'Upper mode: $(y_1,y_2)\propto(2,-1)$')]:
 ax.plot([0,2,3,4],values,color='#176ca6',lw=2);ax.scatter([2,3],values[1:3],s=[55,110],color=['#176ca6','#d57420'],zorder=5)
 ax.scatter([0,4],[0,0],marker='s',color='black',s=35);ax.axhline(0,color='.5',ls=':',lw=.8)
 for xx,yy,label in [(2,values[1],'m'),(3,values[2],'2m')]:ax.text(xx+.08,yy+.16,label,fontsize=11)
 ax.set(title=title,xlabel=r'$x/a$',ylabel='Relative displacement',ylim=(-1.5,2.6));ax.grid(alpha=.15)
t=np.linspace(0,2*np.pi,700);y1=(np.cos(t)+2*np.cos(2*t))/3;y2=(np.cos(t)-np.cos(2*t))/3
for ax,y,title,color in [(axes[1,0],y1,'Light mass released from displacement d','#176ca6'),(axes[1,1],y2,'Heavy mass initially at zero displacement','#d57420')]:
 ax.plot(t,y,color=color,lw=2);ax.axhline(0,color='.5',lw=.6);ax.set(title=title,xlabel=r'$\omega_- t$',ylabel=r'$y/d$',ylim=(-1.1,1.1),xlim=(0,2*np.pi));ax.set_xticks([0,np.pi,2*np.pi],['0',r'$\pi$',r'$2\pi$']);ax.grid(alpha=.15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
