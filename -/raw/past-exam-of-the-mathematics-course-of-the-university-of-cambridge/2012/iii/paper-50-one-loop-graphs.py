"""Render the requested scalar one-loop diagrams to the caller's current directory.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Only root pyproject dependencies are used. The caller's MPLCONFIGDIR is respected.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,axes=plt.subplots(1,4,figsize=(11,3.6),dpi=100,facecolor='white')
style={'color':'#202020','linewidth':1.9}
for ax in axes:
    ax.set_facecolor('white')
    ax.set_aspect('equal')
    ax.set_xlim(-1.55,1.55)
    ax.set_ylim(-1.25,1.45)
    ax.axis('off')
ax=axes[0]
theta=np.linspace(0,2*np.pi,401)
ax.plot(.43*np.sin(theta),.43+.43*np.cos(theta),**style)
ax.plot([-1.05,1.05],[0,0],**style)
ax.scatter([0],[0],s=27,c='#202020',zorder=3)
ax.text(-1.08,-.18,r'$p$',ha='center',fontsize=12)
ax.text(1.08,-.18,r'$-p$',ha='center',fontsize=12)
ax.text(0,1.12,'Two-point tadpole',ha='center',fontsize=12,weight='bold')
ax.text(0,-.92,'Symmetry factor 1/2',ha='center',fontsize=11)
for ax,channel,left,right in zip(axes[1:],['s','t','u'],[(1,2),(1,3),(1,4)],[(3,4),(2,4),(2,3)]):
    t=np.linspace(0,np.pi,201)
    ax.plot(.45*np.cos(t),.38*np.sin(t),**style)
    ax.plot(.45*np.cos(t),-.38*np.sin(t),**style)
    for x,indices,sign in [(-.45,left,-1),(.45,right,1)]:
        for y,index in zip([.58,-.58],indices):
            endx=sign*1.08
            ax.plot([x,endx],[0,y],**style)
            ax.text(endx+sign*.1,y,r'$p_'+str(index)+'$',ha='center',va='center',fontsize=12)
    ax.scatter([-.45,.45],[0,0],s=27,c='#202020',zorder=3)
    ax.text(0,1.12,channel+'-channel bubble',ha='center',fontsize=12,weight='bold')
    pair='1'+str(left[1])
    ax.text(0,-.92,r'$P_'+channel+'=p_1+p_'+str(left[1])+'$',ha='center',fontsize=12)
fig.subplots_adjust(left=.025,right=.975,bottom=.08,top=.95,wspace=.18)
fig.savefig('paper-50-one-loop-graphs.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
