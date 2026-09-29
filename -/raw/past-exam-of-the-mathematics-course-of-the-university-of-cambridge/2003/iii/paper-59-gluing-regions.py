"""Original return-map region diagram and topological orbit sketches.
Interior equilibria are not specified by the question and are not invented.
Python 3.14/numpy/matplotlib; PNG basename output in caller CWD.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle

blue='#0068a3'
def saddle(ax):
    ax.plot(0,0,'kx',ms=6,mew=1.3)
    for s in [-1,1]:
        ax.annotate('',xy=(s*.38,0),xytext=(s*.08,0),arrowprops={'arrowstyle':'->','lw':.9,'color':'#777777'})
        ax.annotate('',xy=(0,s*.08),xytext=(0,s*.38),arrowprops={'arrowstyle':'->','lw':.9,'color':'#777777'})

def cycles(ax,right=False,left=False,outer=False):
    saddle(ax)
    for s,present in [(1,right),(-1,left)]:
        if present:
            ax.add_patch(Circle((s*.83,s*.83),.52,fill=False,color=blue,lw=1.7))
            ax.annotate('',xy=(s*.83+.49,s*.83+.17),xytext=(s*.83+.49,s*.83-.12),arrowprops={'arrowstyle':'->','color':blue,'lw':1.3})
    if outer:
        ax.add_patch(Ellipse((0,0),5.,2.25,angle=45,fill=False,color=blue,lw=1.7))
        t1,t2=-.9,-.78
        p1=((2.5*np.cos(t1)-1.125*np.sin(t1))/np.sqrt(2),(2.5*np.cos(t1)+1.125*np.sin(t1))/np.sqrt(2))
        p2=((2.5*np.cos(t2)-1.125*np.sin(t2))/np.sqrt(2),(2.5*np.cos(t2)+1.125*np.sin(t2))/np.sqrt(2))
        ax.annotate('',xy=p2,xytext=p1,arrowprops={'arrowstyle':'->','color':blue,'lw':1.3})
    ax.set(xlim=(-2.05,2.05),ylim=(-2.05,2.05),aspect='equal')
    ax.axis('off')

fig=plt.figure(figsize=(10,11),constrained_layout=True)
grid=fig.add_gridspec(4,3,height_ratios=[1.45,.15,1,1])
ax=fig.add_subplot(grid[0,:])
mu=np.linspace(-.32,.32,450);nu=np.linspace(-.32,.32,450)
M,N=np.meshgrid(mu,nu);A=.9;B=1.1;delta=1.7
region=np.zeros_like(M)
region[(M<0)&(N<0)]=0
region[(M<0)&(N>0)&(M < -A*np.maximum(N,0)**delta)]=1
region[(M<0)&(N>0)&(M >= -A*np.maximum(N,0)**delta)]=2
region[(M>0)&(N<0)&(N < -B*np.maximum(M,0)**delta)]=3
region[(M>0)&(N<0)&(N >= -B*np.maximum(M,0)**delta)]=4
region[(M>0)&(N>0)]=5
ax.contourf(M,N,region,levels=np.arange(7)-.5,colors=['#e2edf5','#dae8d6','#e9dce9','#f3e2cf','#f8dfdb','#e2e0ef'])
z=np.linspace(0,.32,300)
ax.plot(-A*z**delta,z,color='#873c86',lw=1.6)
ax.plot(z,-B*z**delta,color='#bd553b',lw=1.6)
ax.axhline(0,color='black',lw=1);ax.axvline(0,color='black',lw=1)
ax.text(-.25,-.23,'I: R + L',fontsize=10)
ax.text(-.24,.20,'II: R',fontsize=10)
ax.text(-.026,.18,'III: R + G',fontsize=8,rotation=90,ha='center')
ax.text(.18,-.25,'IV: L',fontsize=10)
ax.text(.23,-.037,'V: L + G',fontsize=8,rotation=-15,ha='center')
ax.text(.13,.20,'VI: G',fontsize=10)
ax.annotate(r'$C_R:\ \mu=-A\nu^\delta$',(-A*.3**delta,.3),(-.3,.31),fontsize=8)
ax.annotate(r'$C_L:\ \nu=-B\mu^\delta$',(.30,-B*.30**delta),(.08,-.18),fontsize=8,arrowprops={'arrowstyle':'->'})
ax.set(xlabel=r'$\mu$',ylabel=r'$\nu$',title=r'Asymmetric gluing: local regions ($A=0.9$, $B=1.1$, $\delta=1.7$)')
ax.spines[['top','right']].set_visible(False)
label=fig.add_subplot(grid[1,:]);label.axis('off')
label.text(.5,.5,'Blue curves: attracting cycles. ×: the given saddle. Sketches show recurrent-orbit topology only.',ha='center',va='center',fontsize=9)
settings=[('I: two single-lobe cycles',True,True,False),('II: right cycle',True,False,False),('III: right + two-lobe cycles',True,False,True),('IV: left cycle',False,True,False),('V: left + two-lobe cycles',False,True,True),('VI: one two-lobe cycle',False,False,True)]
for j,(title,r,l,g) in enumerate(settings):
    ax=fig.add_subplot(grid[2+j//3,j%3]);cycles(ax,r,l,g);ax.set_title(title,fontsize=9)
fig.savefig('paper-59-gluing-regions.png',dpi=120,facecolor='white')
plt.close(fig)
