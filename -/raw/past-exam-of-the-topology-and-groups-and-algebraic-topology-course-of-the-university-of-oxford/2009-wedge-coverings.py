"""Python 3.14, Matplotlib 3.10.7. Write the PNG in the current directory."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse,FancyArrowPatch
from matplotlib.path import Path
blue='#246698';gray='#6d7680'
fig,axs=plt.subplots(1,3,figsize=(13,4.6),gridspec_kw={'width_ratios':[1,1,1.8]},facecolor='white')
def arrow(ax,a,b,rad=0):ax.add_patch(FancyArrowPatch(a,b,connectionstyle=f'arc3,rad={rad}',arrowstyle='-|>',mutation_scale=12,color=blue,lw=1.8))
def dot(ax,x,y,label=None):
 ax.plot(x,y,'o',color='#222222',ms=5,zorder=6)
 if label:ax.text(x-.13,y+.13,label,fontsize=10)
def loop(ax,x,y):
 ax.add_patch(Ellipse((x+.29,y),.58,.42,fill=False,color=blue,lw=1.7))
 arrow(ax,(x+.39,y-.17),(x+.5,y-.1))
 ax.text(x+.62,y-.05,'$x$',fontsize=11,color=blue)
def sphere(ax,x):
 ax.add_patch(Ellipse((x,.1),.85,1.3,facecolor='white',edgecolor=gray,lw=1.5))
 ax.plot([x,x],[-.55,.75],'--',color=gray,lw=1)
 ax.text(x-.36,.12,'$S^2$',fontsize=12,bbox={'facecolor':'white','edgecolor':'none','pad':1})
 dot(ax,x,.75);dot(ax,x,-.55)
ax=axs[0];dot(ax,0,0,'$v_0$');dot(ax,1.7,0,'$v_1$');arrow(ax,(0,.02),(1.7,.02),-.6);arrow(ax,(1.7,-.02),(0,-.02),-.6)
ax.text(.8,.58,'$x$',color=blue,fontsize=12);ax.text(.8,-.6,'$x$',color=blue,fontsize=12)
for x in [0,1.7]:ax.text(x,-1,r'$\mathbb{RP}^2$',ha='center',fontsize=13)
ax.set_title('(i) Two projective planes\nTwo-sheeted cover',fontsize=11);ax.set_xlim(-.55,2.5);ax.set_ylim(-1.5,1.6)
ax=axs[1];sphere(ax,0);loop(ax,0,.75);loop(ax,0,-.55)
ax.text(-.23,-1.2,'$F_2$',fontsize=13);ax.set_title('(ii) Sphere with two loops\nTwo-sheeted cover',fontsize=11);ax.set_xlim(-.65,1.15);ax.set_ylim(-1.5,1.6)
ax=axs[2]
for j,x in enumerate([0,1.9,3.8]):
 sphere(ax,x);loop(ax,x,-.55);ax.text(x+.1,.91,f'$a_{j}$',fontsize=9);ax.text(x-.25,-.92,f'$b_{j}$',fontsize=9)
arrow(ax,(0,.75),(1.9,.75));arrow(ax,(1.9,.75),(3.8,.75))
for x in [.9,2.8]:ax.text(x,.9,'$x$',fontsize=11,color=blue)
path=Path([(3.8,.75),(3.8,1.9),(0,1.9),(0,.75)],[Path.MOVETO,Path.CURVE4,Path.CURVE4,Path.CURVE4]);ax.add_patch(FancyArrowPatch(path=path,arrowstyle='-|>',mutation_scale=12,lw=1.7,color=blue));ax.text(1.8,1.68,'$x$',fontsize=11,color=blue)
ax.text(1.55,-1.3,r'$r=3:\ F_4$',fontsize=12);ax.set_title('(iii) Cyclic family of spheres\nSix-sheeted example',fontsize=11);ax.set_xlim(-.7,4.9);ax.set_ylim(-1.6,2.1)
for ax in axs:ax.set_aspect('equal');ax.axis('off');ax.set_facecolor('white')
fig.suptitle(r'Covering spaces of $S^1\vee\mathbb{RP}^2$',fontsize=15)
fig.tight_layout(rect=(0,.04,1,.91));fig.savefig('2009-wedge-coverings.png',dpi=160,facecolor='white');plt.close(fig)
