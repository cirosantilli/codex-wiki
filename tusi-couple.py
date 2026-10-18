from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':11,'savefig.facecolor':'white'})
fig,axes=plt.subplots(1,3,figsize=(12,3.8),constrained_layout=True)
t=np.linspace(0,2*np.pi,500)
for ax,degrees in zip(axes,[30,60,120]):
 angle=np.deg2rad(degrees);centre=np.array([np.cos(angle),np.sin(angle)]);point=np.array([2*np.cos(angle),0.])
 ax.plot(2*np.cos(t),2*np.sin(t),color='.6',lw=1.4);ax.plot(centre[0]+np.cos(t),centre[1]+np.sin(t),color='#126d8a',lw=1.5)
 ax.axhline(0,color='.55',lw=.8,ls='--')
 for start,end,color in [(np.zeros(2),centre,'#126d8a'),(centre,point,'#b64d36')]:ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':color,'lw':2})
 ax.scatter([point[0]],[0],color='#b64d36',s=30,zorder=5);ax.scatter([centre[0]],[centre[1]],color='#126d8a',s=18,zorder=5)
 ax.text(point[0],-.28,'P',ha='center',color='#b64d36');ax.text(centre[0]+.1,centre[1]+.08,'C',color='#126d8a');ax.text(.05,.07,'O')
 ax.set(xlim=(-2.3,2.3),ylim=(-2.25,2.25),xlabel='$x/R$',ylabel='$y/R$',title=rf'$\theta={degrees}^\circ$');ax.set_aspect('equal');ax.grid(alpha=.13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110)
