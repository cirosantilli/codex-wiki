"""Original spectrograph and geometric slit profile; Python 3.14,
matplotlib 3.10.7, numpy 2.3.5. Save opaque PNG in the working directory.
"""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/2018-paper-338-mpl-cache')
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(11,6),dpi=100,facecolor='white')
ax=fig.add_axes([.04,.41,.92,.53]);ax.set_xlim(-.5,10);ax.set_ylim(-1.1,4.2);ax.axis('off')
blue='#1764a0';orange='#cf7000';red='#ba2434'
ax.plot([-.4,8],[0,0],'--',color='#aaa');ax.plot([8,8],[0,3.4],'--',color='#aaa')
def lens(x,y,vertical=True):
    a=(x,y-.8) if vertical else (x-.8,y)
    b=(x,y+.8) if vertical else (x+.8,y)
    ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'<->','color':blue,'lw':2.2})
def ray(points):
    a=np.asarray(points);ax.plot(a[:,0],a[:,1],color=orange,lw=1.7)
    u=a[-2]+.45*(a[-1]-a[-2]);v=a[-2]+.65*(a[-1]-a[-2])
    ax.annotate('',xy=v,xytext=u,arrowprops={'arrowstyle':'->','color':orange})
lens(.5,0);lens(4,0);lens(8,2.1,False)
for s in [-1,1]:
    ray([[-.4,s*.65],[.5,s*.65],[2.1,0],[4,s*.36],[8+s*.36,s*.36],[8+s*.36,2.1],[8,3.4]])
ax.plot([2.1,2.1],[-.75,-.10],color=blue,lw=4);ax.plot([2.1,2.1],[.10,.75],color=blue,lw=4)
ax.plot([7.4,8.6],[-.6,.6],color=blue,lw=4)
ax.plot([7.55,8.45],[3.4,3.4],color=red,lw=3)
for x,t in [(.5,'telescope'),(2.1,'slit'),(4,'collimator')]:ax.text(x,-1,t,ha='center',fontsize=11)
ax.text(5.9,.5,'collimated beam',ha='center',fontsize=10)
ax.text(8.55,-.55,'reflection grating',fontsize=10)
ax.text(8.9,2.05,'camera',fontsize=11)
ax.text(8,3.65,'detector / slit image',ha='center',fontsize=11)
ax.text(.1,1.2,'Geometric layout (schematic)',fontsize=12)
bx=fig.add_axes([.25,.105,.5,.23])
bx.plot([-2,-.5,-.5,.5,.5,2],[0,0,1,1,0,0],color=orange,lw=2.5)
bx.set_xlim(-2,2);bx.set_ylim(-.18,1.3);bx.set_yticks([0,1],['0',r'$I_0$'])
bx.set_xticks([-.5,0,.5],[r'$x_0-p/2$',r'$x_0$',r'$x_0+p/2$'])
bx.set_ylabel('Intensity');bx.set_xlabel('Detector coordinate in dispersion direction')
bx.annotate('',xy=(.5,.45),xytext=(-.5,.45),arrowprops={'arrowstyle':'<->','color':'#444'})
bx.text(0,.55,r'$p=q\,\Delta\lambda$',ha='center',fontsize=12)
bx.set_title('Uniform monochromatic slit: ideal top-hat profile',fontsize=11)
bx.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=100,facecolor='white',transparent=False)
