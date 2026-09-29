"""Original augmentation diagrams.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7+dfsg1.
Writes only paper-40-augmenting-paths.png to the caller's working directory.
Matplotlib uses the caller's MPLCONFIGDIR unchanged.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

pos={'s':(0,0),'1':(1,.72),'2':(1,-.72),'t':(2,0)}
edges=[('s','1'),('1','t'),('s','2'),('2','t'),('1','2')]
fig,axes=plt.subplots(1,3,figsize=(15,4),dpi=100,facecolor='white')
for ax in axes:
 ax.set_facecolor('white');ax.set_xlim(-.3,2.3);ax.set_ylim(-1.08,1.18);ax.set_aspect('equal');ax.axis('off')
 for u,v in edges:
  x,y=zip(pos[u],pos[v]);ax.plot(x,y,color='#aeb7bf',lw=1.5,zorder=1)
 for name,(x,y) in pos.items():
  ax.add_patch(Circle((x,y),.105,facecolor='white',edgecolor='#38434d',lw=1.3,zorder=5));ax.text(x,y,name,ha='center',va='center',fontsize=13,zorder=6)

def arrow(ax,u,v,color):
 ax.add_patch(FancyArrowPatch(pos[u],pos[v],arrowstyle='-|>',mutation_scale=14,shrinkA=11,shrinkB=11,lw=2.8,color=color,zorder=3))
def label(ax,u,v,text):
 x=(pos[u][0]+pos[v][0])/2;y=(pos[u][1]+pos[v][1])/2
 if u=='1' and v=='2':x+=.17
 else:y+=.13 if y>0 else -.13
 ax.text(x,y,text,ha='center',va='center',fontsize=12,bbox=dict(facecolor='white',edgecolor='none',pad=1),zorder=4)
blue='#1675a9';orange='#c56519'
for u,v in [('s','1'),('1','t')]:arrow(axes[0],u,v,blue)
for u,v in [('s','2'),('2','t')]:arrow(axes[0],u,v,orange)
for u,v in edges:label(axes[0],u,v,'1' if (u,v)==('1','2') else r'$M$')
axes[0].set_title('Two direct augmentations',fontsize=13,pad=7)
axes[0].text(1,-1.03,r'Total increase: $M+M=2M$',ha='center',fontsize=11)
for u,v in [('s','1'),('1','2'),('2','t')]:arrow(axes[1],u,v,orange)
for u,v in edges:label(axes[1],u,v,'1' if (u,v)==('1','2') else r'$M$')
axes[1].set_title('First crossing augmentation',fontsize=13,pad=7)
axes[1].text(1,-1.03,'Increase: 1; middle net flow: 1',ha='center',fontsize=11)
for u,v in [('s','2'),('2','1'),('1','t')]:arrow(axes[2],u,v,blue)
for u,v in edges:
 label(axes[2],u,v,'2' if (u,v)==('1','2') else r'$M-1$' if (u,v) in [('s','1'),('2','t')] else r'$M$')
axes[2].set_title('Opposite crossing in the residual network',fontsize=13,pad=7)
axes[2].text(1,-1.03,r'Reverse middle capacity: $1-(-1)=2$',ha='center',fontsize=11)
fig.tight_layout(pad=1.5,w_pad=2)
fig.savefig('paper-40-augmenting-paths.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
