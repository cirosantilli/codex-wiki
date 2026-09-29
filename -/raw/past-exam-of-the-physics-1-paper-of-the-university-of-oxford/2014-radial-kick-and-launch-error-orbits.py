"""Original conic/effective-potential calculations. Python 3.14,
NumPy 2.3, Matplotlib 3.10. Writes only the basename PNG in CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,3,figsize=(13.3,4.6),facecolor='white');phi=np.linspace(0,2*np.pi,1801)
a=axs[0];r=1/(1-.5*np.sin(phi));a.plot(r*np.cos(phi),r*np.sin(phi),c='#b14c29',label='After radial kick');a.plot(np.cos(phi),np.sin(phi),c='#236b8e',ls='--',label='Original circle');a.scatter([0,1],[0,0],c=['#263849','black'],s=[28,18]);a.annotate('',xy=(1,.7),xytext=(1,0),arrowprops={'arrowstyle':'->','color':'#236b8e','lw':2});a.annotate('',xy=(1.55,0),xytext=(1,0),arrowprops={'arrowstyle':'->','color':'#b14c29','lw':2});a.text(1.04,.52,r'$v_c$',color='#236b8e');a.text(1.12,-.20,r'$\Delta v_r$',color='#b14c29');a.scatter([0,0],[-2/3,2],c='black',s=15);a.text(.07,2.04,r'$r_{\max}=2r_0$',fontsize=9);a.text(.09,-.83,r'$r_{\min}=2r_0/3$',fontsize=9);a.set(xlim=(-1.6,1.9),ylim=(-1.1,2.5),title=r'Radial kick, $\beta=1.25$',xlabel=r'$x/r_0$',ylabel=r'$y/r_0$');a.set_aspect('equal');a.legend(fontsize=8,loc='upper left')
a=axs[1];rr=np.linspace(.35,4,1000);a.plot(rr,.5/rr**2-1/rr,c='#263849',label=r'$V_{\rm eff}/(GMm/r_0)$')
for E,label,col in [(-.375,r'$\beta=1.25$: bound','#b14c29'),(0,r'$\beta=2$: parabolic','#236b8e'),(.25,r'$\beta=2.5$: escaping','#4b7b43')]:a.axhline(E,color=col,label=label,lw=1.5)
a.scatter([2/3,2],[-.375,-.375],c='#b14c29',s=18);a.set(xlim=(.35,4),ylim=(-.6,.65),xlabel=r'$r/r_0$',ylabel='Dimensionless energy',title='Turning radii at intersections');a.legend(fontsize=8,loc='upper right')
a=axs[2];alpha=np.pi/6;e=np.sin(alpha);orient=-np.pi/2-alpha;r=(1-e*e)/(1+e*np.cos(phi-orient));a.plot(np.cos(phi),np.sin(phi),c='#236b8e',ls='--',label='Intended circle');a.plot(r*np.cos(phi),r*np.sin(phi),c='#b14c29',label='Actual ellipse');a.scatter([0,1],[0,0],c=['#263849','black'],s=[28,18]);a.annotate('',xy=(1+.35*np.sin(alpha),.35*np.cos(alpha)),xytext=(1,0),arrowprops={'arrowstyle':'->','lw':2});a.text(.55,-1.12,r'$a=R,\ e=0.5$',fontsize=10);a.set(xlim=(-1.35,1.65),ylim=(-1.35,1.65),xlabel=r'$x/R$',ylabel=r'$y/R$',title='Correct speed, direction error 30°');a.set_aspect('equal');a.legend(loc='upper left',fontsize=8)
for a in axs:a.grid(alpha=.15);a.spines[['top','right']].set_visible(False)
fig.tight_layout();fig.savefig(Path('2014-radial-kick-and-launch-error-orbits.png'),dpi=140,facecolor='white')
