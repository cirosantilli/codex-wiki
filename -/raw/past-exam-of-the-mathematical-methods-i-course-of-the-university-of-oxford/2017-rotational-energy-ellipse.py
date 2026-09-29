"""Exact original inertia ellipse. Python 3.14; NumPy 2.3; Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'figure.facecolor':'white','savefig.facecolor':'white'})
fig,ax=plt.subplots(figsize=(6.2,5.5),layout='constrained');t=np.linspace(0,2*np.pi,1001);q=np.array([[1,-1],[1,1]])/np.sqrt(2);xy=q@np.array([np.sqrt(2)*np.cos(t),np.sqrt(2/3)*np.sin(t)])
ax.plot(*xy,lw=2,label=r'$T=1,\ I_0=1$');ax.fill(*xy,alpha=.07)
for index,name,color in [(0,r"$\omega'_x$: major",'tab:red'),(1,r"$\omega'_y$: minor",'tab:green')]:
 v=q[:,index];ax.annotate('',xy=1.72*v,xytext=-1.72*v,arrowprops={'arrowstyle':'->','color':color,'lw':1.5});ax.text(*(1.82*v),name,color=color,ha='left',va='bottom',fontsize=11)
ax.axhline(0,color='.6',lw=.8);ax.axvline(0,color='.6',lw=.8);ax.plot([0,1],[0,1],':',color='tab:red',lw=1);ax.text(.35,.12,'45°',color='tab:red')
ax.set(xlim=(-1.9,2),ylim=(-1.8,1.85),xlabel=r'$\omega_x$',ylabel=r'$\omega_y$',title='Principal axes of rotational energy');ax.set_aspect('equal');ax.grid(alpha=.18);ax.legend(loc='lower right')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False);plt.close(fig)
