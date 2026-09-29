"""Original spectral domains; Python 3.14 / Matplotlib 3.10.7 / NumPy 2.3.5.

Write the opaque PNG basename to caller CWD; preserve caller MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
fig,axes=plt.subplots(1,2,figsize=(11.2,4.8),dpi=100)
fig.patch.set_facecolor('white')
ax=axes[0];u=np.linspace(-1.9,1.9,800);v=np.sqrt(1+3*u*u)
ax.fill_between(u,0,v,color='#dbeafa');ax.plot(u,v,color='#345b92',lw=2);ax.axhline(0,color='#6b3782',lw=2);ax.axvline(0,color='#888888',lw=.7)
ax.annotate('',xy=(.95,0),xytext=(.1,0),arrowprops=dict(arrowstyle='->',color='#6b3782',lw=2))
u1,u2=.95,.45;ax.annotate('',xy=(u2,np.sqrt(1+3*u2*u2)),xytext=(u1,np.sqrt(1+3*u1*u1)),arrowprops=dict(arrowstyle='->',color='#345b92',lw=2))
ax.text(-.05,.4,r'$D_+:\ \mathrm{Re}\,w<0$',ha='center',fontsize=12);ax.text(-.05,2.7,r'$\mathrm{Re}\,w>0$',ha='center',fontsize=12)
ax.text(.03,1.05,r'$i$',fontsize=12);ax.text(1.22,2.85,r'$C$',fontsize=13)
ax.set_xlim(-1.9,1.9);ax.set_ylim(-.15,3.45);ax.set_aspect('equal');ax.set_xlabel(r'$\mathrm{Re}\,k$');ax.set_ylabel(r'$\mathrm{Im}\,k$')
ax.set_title(r'Linear contour: $w=i(k+k^3)$',fontsize=13)
ax.text(0,-.19,r'Full boundary = real axis plus upper curve',transform=ax.transAxes,fontsize=10)
ax=axes[1];labels=['D_1','D_2','D_1','D_4','D_3','D_4'];colours=['#dbeafa','#faebcb','#dbeafa','#e9ddf5','#dff0df','#e9ddf5']
for j,(lab,col) in enumerate(zip(labels,colours)):
 ax.add_patch(Wedge((0,0),1.65,60*j,60*(j+1),facecolor=col,edgecolor='white'))
 angle=(j+.5)*np.pi/3;ax.text(1.04*np.cos(angle),1.04*np.sin(angle),'$'+lab+'$',ha='center',va='center',fontsize=13)
 angle=j*np.pi/3;ax.plot([0,1.75*np.cos(angle)],[0,1.75*np.sin(angle)],color='#333333',lw=1.2)
ax.set_xlim(-1.9,1.9);ax.set_ylim(-1.85,1.85);ax.set_aspect('equal');ax.set_xlabel(r'$\mathrm{Re}\,k$');ax.set_ylabel(r'$\mathrm{Im}\,k$');ax.set_title(r'mKdV: signs of $(\mathrm{Im}\,k,\mathrm{Im}\,k^3)$',fontsize=13)
ax.text(.04,-.19,r'$D_1:(+,+)\quad D_2:(+,-)\quad D_3:(-,+)\quad D_4:(-,-)$',transform=ax.transAxes,fontsize=10)
fig.subplots_adjust(left=.075,right=.98,bottom=.21,top=.89,wspace=.3)
fig.savefig(Path('paper-61-spectral-domains.png'),facecolor='white',transparent=False)
plt.close(fig)
