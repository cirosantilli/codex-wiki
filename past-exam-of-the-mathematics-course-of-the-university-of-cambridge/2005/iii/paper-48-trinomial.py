"""One-step log-price tree. Python 3.12, root numpy/matplotlib dependencies.
Writes paper-48-trinomial.png to caller CWD; respects caller MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,ax=plt.subplots(figsize=(8.6,4.2),dpi=140)
fig.patch.set_facecolor('white');ax.set_facecolor('white')
origin=(0,0)
labels=[(1.6,1.05,r'$x_i+h$',r'$p_u=ka/h^2+kb/(2h)$'),(1.6,0,r'$x_i$',r'$p_m=1-2ka/h^2$'),(1.6,-1.05,r'$x_i-h$',r'$p_d=ka/h^2-kb/(2h)$')]
for x,y,state,weight in labels:
 ax.annotate('',xy=(x-.08,y),xytext=(.10,0),arrowprops=dict(arrowstyle='->',lw=1.8,color='#365f91'))
 ax.scatter([x],[y],s=65,color='#365f91',zorder=3)
 ax.text(x+.11,y,state,va='center',fontsize=13)
 ax.text(.55,y*.57+.12 if y else -.17,weight,fontsize=11,ha='left',va='center',bbox=dict(facecolor='white',edgecolor='none',pad=1.5))
ax.scatter([0],[0],s=80,color='#202d40',zorder=3)
ax.text(-.10,.15,r'$x_i$',ha='right',fontsize=13)
ax.text(0,1.42,r'Time $t_{j-1}$',ha='center',fontsize=12)
ax.text(1.6,1.42,r'Time $t_j$',ha='center',fontsize=12)
ax.text(.75,-1.48,r'$u_i^{j-1}=p_d u_{i-1}^{j}+p_m u_i^{j}+p_u u_{i+1}^{j}$',ha='center',fontsize=13)
ax.set_title('Log-price trinomial tree: backward pricing is a weighted average',fontsize=13,pad=16)
ax.set_xlim(-.45,2.35);ax.set_ylim(-1.7,1.62);ax.axis('off')
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-48-trinomial.png',facecolor='white',transparent=False)
plt.close(fig)
