"""One-loop cubic scalar two-point insertion. PNG basename written only to cwd.
Python 3.14; dependencies in the root pyproject.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch,Circle
fig,ax=plt.subplots(figsize=(7.6,3.5),dpi=100,facecolor='white')
blue='#194b7b';ax.set_xlim(-2.5,2.5);ax.set_ylim(-1,1.1);ax.axis('off')
for h in [-1,1]:
    ax.add_patch(PathPatch(Path([(-.8,0),(-.5,h),(.5,h),(.8,0)],[Path.MOVETO,Path.CURVE4,Path.CURVE4,Path.CURVE4]),fill=False,color=blue,lw=2.4))
ax.plot([-2,-.8],[0,0],color=blue,lw=2);ax.plot([.8,2],[0,0],color=blue,lw=2)
for x in [-.8,.8]:ax.add_patch(Circle((x,0),.065,color=blue))
ax.text(0,.8,r'$p+k$',ha='center',fontsize=16);ax.text(0,-.86,r'$p$',ha='center',fontsize=16)
ax.text(-1.55,.17,r'$k$',ha='center',fontsize=16);ax.text(1.55,.17,r'$k$',ha='center',fontsize=16)
ax.text(-.8,-.29,r'$-g\mu^{(6-d)/2}$',ha='right',fontsize=12);ax.text(.8,-.29,r'$-g\mu^{(6-d)/2}$',ha='left',fontsize=12)
ax.set_title('Cubic scalar two-point insertion: symmetry factor 1/2',fontsize=14,pad=8)
fig.text(.5,.04,'The displayed integral amputates the two external propagators.',ha='center',fontsize=11)
fig.subplots_adjust(left=.025,right=.975,bottom=.12,top=.85)
fig.savefig('paper-46-cubic-self-energy.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
