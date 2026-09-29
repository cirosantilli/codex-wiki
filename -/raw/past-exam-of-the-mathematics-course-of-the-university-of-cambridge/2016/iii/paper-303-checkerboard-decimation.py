"""Checkerboard bond counting; Python 3.14, root Matplotlib dependency.
Produces one opaque basename PNG in cwd. Source and _media locations are Make's concern.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
fig,(left,right)=plt.subplots(1,2,figsize=(10,4.4),dpi=100,facecolor='white')
for ax in (left,right):
 ax.set_aspect('equal');ax.set_facecolor('white');ax.spines[['top','right']].set_visible(False);ax.tick_params(labelsize=9)
for x in range(-1,4):
 for y in range(-1,3):
  if (x+y)%2==0:left.scatter(x,y,c='#263238',s=55,zorder=4)
  else:left.scatter(x,y,c='#a7a7a7',s=60,marker='x',linewidths=1.8,zorder=5)
for x in range(-1,4):left.plot([x,x],[-1,2],c='#ececec',lw=.8,zorder=0)
for y in range(-1,3):left.plot([-1,3],[y,y],c='#ececec',lw=.8,zorder=0)
for points in [[(0,0),(0,1),(1,1)],[(0,0),(1,0),(1,1)]]:left.plot(*zip(*points),c='#d67917',lw=3,zorder=2)
left.plot([0,1,2],[-.06,-.06,-.06],c='#2467af',lw=2.6,zorder=3)
left.plot([0,1],[0,1],c='#26875f',ls='--',lw=2,zorder=2)
for point,color,label,offset in [((0,0),'#263238','retained origin',(-.88,-.49)),((1,1),'#d67917','two shared centres',(.13,.17)),((2,0),'#2467af','one shared centre',(.08,.12))]:
 left.scatter(*point,s=100,c=color,zorder=6)
 left.annotate(label,point,xytext=(point[0]+offset[0],point[1]+offset[1]),fontsize=9,color=color,bbox=dict(facecolor='white',edgecolor='none',pad=1.5))
left.set(xlim=(-1.1,3.15),ylim=(-1.1,2.15),xlabel='original x / a',ylabel='original y / a');left.set_xticks(range(-1,4));left.set_yticks(range(-1,3));left.set_title('Retain even x + y; sum over the crosses',fontsize=11)
left.legend(handles=[Line2D([],[],marker='o',ls='',c='#263238',label='retained spin'),Line2D([],[],marker='x',ls='',c='#a7a7a7',label='eliminated spin'),Line2D([],[],ls='--',c='#26875f',label='original diagonal coupling L')],fontsize=8,loc='lower right',framealpha=1)
for u in range(-1,3):
 for v in range(-1,3):right.scatter(u,v,s=55,c='#263238',zorder=4)
for u in range(-1,3):right.plot([u,u],[-1,2],c='#ececec',lw=.8)
for v in range(-1,3):right.plot([-1,2],[v,v],c='#ececec',lw=.8)
right.plot([0,1],[0,0],c='#d67917',lw=3,zorder=3);right.plot([0,1],[0,1],c='#2467af',lw=3,zorder=3)
right.scatter([0,1,1],[0,0,1],c=['#263238','#d67917','#2467af'],s=100,zorder=5)
right.text(.5,-.33,r"$K'=L+2K^2$",ha='center',fontsize=12,color='#b46110',bbox=dict(facecolor='white',edgecolor='none',pad=2));right.text(.28,.62,r"$L'=K^2$",rotation=45,fontsize=12,color='#2467af',bbox=dict(facecolor='white',edgecolor='none',pad=2))
right.text(.5,1.68,r'$u=(x+y)/2,\quad v=(x-y)/2$',ha='center',fontsize=10)
right.set(xlim=(-1.12,2.12),ylim=(-1.1,2.15),xlabel='rescaled u (spacing a)',ylabel='rescaled v (spacing a)');right.set_xticks(range(-1,3));right.set_yticks(range(-1,3));right.set_title(r'Retained lattice: rotate and rescale by $1/\sqrt{2}$',fontsize=11)
fig.subplots_adjust(left=.07,right=.97,bottom=.14,top=.89,wspace=.3)
fig.savefig('paper-303-checkerboard-decimation.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
