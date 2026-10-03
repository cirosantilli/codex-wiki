"""Original distributional-support schematic; output is only in the caller's cwd.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,(ax,bx)=plt.subplots(1,2,figsize=(9.6,3.6),dpi=100,gridspec_kw={'width_ratios':[1,1.65]})
theta=np.linspace(0,2*np.pi,361)
ax.plot(np.cos(theta),np.sin(theta),color='#237c82',lw=3)
ax.scatter([0],[0],s=70,color='#a83b72',zorder=3)
ax.annotate(r'$-\pi\cos m\,\delta_0$',xy=(0,0),xytext=(.10,-.34),color='#a83b72')
ax.text(.62,.82,r'$\delta_{S^1}$',color='#237c82',fontsize=13)
ax.set_aspect('equal');ax.set_xlim(-1.30,1.30);ax.set_ylim(-1.30,1.30)
ax.set_xlabel(r'$x_1$');ax.set_ylabel(r'$x_2$');ax.grid(alpha=.14)
ax.set_title('Singular contributions')
m=np.arange(1,41);c=-np.pi*np.cos(m)
bx.axhline(0,color='.6',lw=.7)
bx.plot(m,c,color='#a83b72',lw=1,alpha=.7)
bx.scatter(m,c,color='#a83b72',s=14,zorder=3)
bx.set_xlim(0,41);bx.set_ylim(-3.5,3.5);bx.set_yticks([-np.pi,0,np.pi],[r'$-\pi$','0',r'$\pi$'])
bx.set_xlabel('Integer index m');bx.set_ylabel('Coefficient of the point mass at the origin')
bx.set_title('The origin coefficient does not converge');bx.grid(alpha=.14)
fig.text(.5,.015,'Away from the origin only the stable unit-circle arclength measure remains.',ha='center',fontsize=9)
fig.subplots_adjust(left=.07,right=.985,bottom=.19,top=.86,wspace=.34)
fig.savefig(Path.cwd()/'paper-327-circle-and-point-defect.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
