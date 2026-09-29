"""Original schematic stellar composition profiles, not computed models.
Python 3.14, numpy 2.3.5, matplotlib 3.10.7; output to CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
q=np.linspace(0,1,1001)
# H exhaustion: helium core and gradient left by a retreating convective core.
xh=np.interp(q,[0,.08,.25,1],[0,0,.70,.70]);yh=.98-xh
# Helium exhaustion: C/O core, helium mantle and hydrogen-rich envelope.
xe=np.interp(q,[0,.15,.17,.19,.3,1],[0,0,0,.65,.68,.68])
ye=np.interp(q,[0,.15,.155,.17,.19,.3,1],[.02,.02,.98,.98,.33,.30,.30])
# Second dredge-up homogenizes the envelope and moves its H boundary inward.
xd=np.interp(q,[0,.15,.17,.18,1],[0,0,0,.64,.64])
yd=np.interp(q,[0,.15,.155,.17,.18,1],[.02,.02,.98,.98,.34,.34])
assert all(np.all((z>=0)&(z<=1)) for z in [xh,yh,xe,ye,xd,yd])
assert all(np.all(x+y<=1.000001) for x,y in [(xh,yh),(xe,ye),(xd,yd)])
fig,axs=plt.subplots(1,2,figsize=(10,5.2),dpi=100,facecolor='white')
axs[0].plot(q,xh,color='#2866a3',lw=2.2,label='H: central exhaustion')
axs[0].plot(q,yh,color='#c56227',lw=2.2,label='He: central H exhaustion')
axs[0].axhline(.70,color='#2866a3',ls=':',lw=1.2,label='Initial H')
axs[0].axhline(.28,color='#c56227',ls=':',lw=1.2,label='Initial He')
axs[0].set_title('End of core hydrogen burning',fontsize=12)
axs[0].annotate('He core',xy=(.04,.95),xytext=(.22,.86),fontsize=10,arrowprops=dict(arrowstyle='->',color='#777'))
axs[0].annotate('Composition gradient',xy=(.18,.42),xytext=(.43,.48),fontsize=10,arrowprops=dict(arrowstyle='->',color='#777'))
axs[1].plot(q,xe,color='#2866a3',lw=2.2,label='H: He exhaustion')
axs[1].plot(q,ye,color='#c56227',lw=2.2,label='He: He exhaustion')
axs[1].plot(q,xd,color='#2866a3',ls='--',lw=1.6,label='H: after second dredge-up')
axs[1].plot(q,yd,color='#c56227',ls='--',lw=1.6,label='He: after second dredge-up')
axs[1].set_title('He exhaustion and early AGB',fontsize=12)
axs[1].annotate('C/O core:\nH and He depleted',xy=(.07,.025),xytext=(.32,.10),fontsize=10,arrowprops=dict(arrowstyle='->',color='#777'))
axs[1].annotate('He-rich layer',xy=(.16,.93),xytext=(.39,.82),fontsize=10,arrowprops=dict(arrowstyle='->',color='#777'))
for ax in axs:
 ax.set_facecolor('white');ax.set(xlim=(0,1),ylim=(-.025,1.03),xlabel=r'Enclosed mass / current stellar mass, $m/M$',ylabel='Mass fraction')
 ax.grid(alpha=.15);ax.legend(fontsize=9,loc='upper right',bbox_to_anchor=(1,.75))
fig.suptitle('Schematic composition profiles: mass boundaries are illustrative',fontsize=14,y=.97)
fig.subplots_adjust(left=.075,right=.98,bottom=.14,top=.84,wspace=.30)
fig.savefig(Path.cwd()/'paper-317-composition.png',facecolor='white',transparent=False)
plt.close(fig)
