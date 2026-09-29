"""Original complex-locus and triangle-circle sketches; Python 3.14.

Run from the output directory; writes paper-1-complex-loci.png to caller CWD.
Uses only the root-declared NumPy and Matplotlib dependencies.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

fig,axes=plt.subplots(1,2,figsize=(9.8,4.8),facecolor='white')
left,right=axes
for ax in axes:
 ax.set_facecolor('white');ax.set_aspect('equal');ax.axhline(0,color='#aaaaaa',lw=.8);ax.axvline(0,color='#aaaaaa',lw=.8)
 ax.set_xlabel(r'$\operatorname{Re}z$');ax.set_ylabel(r'$\operatorname{Im}z$');ax.grid(alpha=.15)
left.add_patch(Circle((-2,0),np.sqrt(2),fill=False,color='#356f9f',lw=2))
left.scatter([-2],[0],color='#356f9f',s=20)
left.text(-2,.12,r'$-2$',ha='center')
left.text(-3.3,1.48,r'$|z+2|=\sqrt{2}$',color='#356f9f')
left.set_xlim(-3.8,.4);left.set_ylim(-1.9,1.9);left.set_title('Continued-fraction locus',fontsize=12)

q=1/np.sqrt(3);r=(3-np.sqrt(3))/6
verts=np.array([[0,0],[0,1],[q,1]])
right.add_patch(Polygon(verts,closed=True,facecolor='#e7f3eb',edgecolor='none'))
right.axvline(0,color='#444444',lw=1.4)
right.axhline(1,color='#444444',lw=1.4)
rayx=np.array([0,.87]);right.plot(rayx,np.sqrt(3)*rayx,color='#444444',lw=1.4)
right.add_patch(Circle((q/2,.5),q,fill=False,color='#356f9f',lw=1.8,linestyle='--',label='circumcircle'))
right.add_patch(Circle((r,1-r),r,fill=False,color='#b06a16',lw=1.8,label='incircle'))
right.scatter(verts[:,0],verts[:,1],color='#222222',s=18,zorder=5)
right.annotate(r'$O=0$',(0,0),xytext=(-32,-13),textcoords='offset points',fontsize=10)
right.annotate(r'$P=i$',(0,1),xytext=(-30,10),textcoords='offset points',fontsize=10)
right.annotate(r'$Q=1/\sqrt{3}+i$',(q,1),xytext=(7,7),textcoords='offset points',fontsize=10)
right.scatter([q/2,r],[.5,1-r],s=14,color=['#356f9f','#b06a16'])
right.set_xlim(-.42,1.02);right.set_ylim(-.18,1.5);right.set_title('Bounded triangle and its circles',fontsize=12)
right.legend(loc='lower right',fontsize=9,framealpha=1)
fig.tight_layout(pad=1.2,w_pad=2.0)
fig.savefig(Path.cwd()/'paper-1-complex-loci.png',dpi=160,facecolor='white',transparent=False)
plt.close(fig)
