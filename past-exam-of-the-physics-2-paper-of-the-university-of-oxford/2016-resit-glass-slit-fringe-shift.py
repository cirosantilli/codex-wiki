"""Original illustration for the 2016 Oxford Physics 2 resit solutions.
Writes only the matching PNG to the current working directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

s=1e-4;D=.85;lam=s*.05/np.sqrt(D*D+.05*.05)/10;delay=.5e-4;Y0=D*np.tan(np.arcsin(delay/s))
fig,axs=plt.subplots(1,2,figsize=(10,4.5),layout='constrained')
for level,delta,col,label in [(1,0,'#266da6','no plate'),(0,delay,'#b65b26','glass plate')]:
 m=np.arange(-500,501);sn=(delta-m*lam)/s;sn=sn[abs(sn)<1];pos=D*sn/np.sqrt(1-sn*sn);pos=pos[(pos>-.04)&(pos<.55)];axs[0].vlines(pos,level-.12,level+.12,color=col,lw=1)
 center=0 if delta==0 else Y0;axs[0].scatter([center],[level],color=col,s=52,zorder=4);axs[0].annotate('$m=0$',(center,level),xytext=(-10,25),textcoords='offset points',fontsize=11,color=col)
axs[0].set(xlim=(-.045,.56),ylim=(-.3,1.6),yticks=[0,1],yticklabels=['glass plate','no plate'],xlabel='screen position $Y$ (m)',title='Bright fringes; highlighted order-zero maxima');axs[0].grid(axis='x',alpha=.2);axs[0].text(.29,.48,rf'$Y_0={Y0:.3f}$ m'+'\n'+r'$\theta_0=30^\circ$',ha='center')
Y=np.linspace(-.0075,.0075,2000);sn=Y/np.sqrt(D*D+Y*Y)
for delta,col,label in [(0,'#266da6','no plate'),(delay,'#b65b26','glass plate')]:axs[1].plot(Y*1000,np.cos(np.pi*(delta-s*sn)/lam)**2,color=col,label=label,lw=1.7)
axs[1].set(xlabel='screen position $Y$ (mm)',ylabel='intensity / maximum',ylim=(0,1.08),title='Local fringes remain near the original centre');axs[1].grid(alpha=.2);axs[1].legend(fontsize=9)
fig.suptitle('Far-field geometry allows a large observation angle; a small-angle screen shift is inaccurate',fontsize=12)
fig.savefig(Path.cwd()/'2016-resit-glass-slit-fringe-shift.png',dpi=140,transparent=False);plt.close(fig)
