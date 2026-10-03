"""Three quartic one-loop 1PI channels; Python 3.14, matplotlib 3.10.7.
Run in the mirrored media directory; writes only the basename PNG to cwd.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
fig,axs=plt.subplots(1,3,figsize=(8,2.5),dpi=120,facecolor='white')
for ax,(title,left,right) in zip(axs,[('s channel',(1,2),(3,4)),('t channel',(1,3),(2,4)),('u channel',(1,4),(2,3))]):
 ax.set(xlim=(-.1,1.1),ylim=(-.05,1.05));ax.axis('off')
 color='#214c76';A=(.32,.48);B=(.68,.48)
 for x,labels,direction in [(A[0],left,-1),(B[0],right,1)]:
  for y,label in zip([.79,.17],labels):
   endpoint=x+direction*.28;ax.plot([x,endpoint],[.48,y],color=color,lw=1.7)
   ax.text(endpoint+direction*.015,y,fr'$p_{label}$',ha='right' if direction<0 else 'left',va='center',fontsize=12)
 for angle in [(0,180),(180,360)]:
  ax.add_patch(Arc((.5,.48),.36,.44,theta1=angle[0],theta2=angle[1],color=color,lw=1.7))
 ax.scatter([A[0],B[0]],[.48,.48],s=28,color=color,zorder=4)
 ax.text(.5,.98,title,ha='center',fontsize=12)
 ax.text(.5,-.02,'symmetry factor 1/2',ha='center',fontsize=10)
fig.subplots_adjust(left=.015,right=.985,top=.88,bottom=.09,wspace=.16)
fig.suptitle('All one-loop 1PI four-point graphs in quartic scalar theory',fontsize=12,y=.98)
fig.savefig('paper-304-quartic-bubbles.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
