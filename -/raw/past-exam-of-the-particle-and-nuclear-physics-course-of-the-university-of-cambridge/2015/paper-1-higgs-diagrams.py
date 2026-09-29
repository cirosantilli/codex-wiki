from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,axs=plt.subplots(2,3,figsize=(11,6.8))
def line(ax,p,q,kind='fermion',arrow=True,label=None):
 p=np.array(p,float);q=np.array(q,float);d=q-p;norm=np.array([-d[1],d[0]])/np.linalg.norm(d)
 if kind=='higgs':ax.plot(*np.array([p,q]).T,ls='--',lw=1.7,color='black')
 elif kind in ['photon','gluon','W']:
  t=np.linspace(0,1,240);freq=7 if kind!='gluon' else 9;amp=.045 if kind!='gluon' else .065
  z=p[:,None]+d[:,None]*t+norm[:,None]*amp*np.sin(2*np.pi*freq*t)
  if kind=='gluon':z+=d[:,None]/np.linalg.norm(d)*.025*(np.cos(2*np.pi*freq*t)-1)
  ax.plot(*z,lw=1.2,color='tab:blue' if kind!='gluon' else 'tab:green')
 else:
  ax.plot(*np.array([p,q]).T,color='black',lw=1.5)
  if arrow:ax.annotate('',xy=p+.6*d,xytext=p+.43*d,arrowprops={'arrowstyle':'->','color':'black','lw':1.4})
 if label:ax.text(*(p+.5*d+norm*.12),label,ha='center',fontsize=10)
def setup(ax,title):ax.set(xlim=(-1.6,1.7),ylim=(-1.15,1.35),title=title);ax.axis('off')
a=axs[0,0];setup(a,r'$\mu^+\mu^-\to H\to b\bar b$')
line(a,(-1.4,.8),(-.5,0));line(a,(-.5,0),(-1.4,-.8));line(a,(-.5,0),(.5,0),'higgs',label='$H$');line(a,(.5,0),(1.4,.8));line(a,(1.4,-.8),(.5,0))
for xy,lab in [((-1.5,.95),r'$\mu^-$'),((-1.5,-1),r'$\mu^+$'),((1.35,.95),'$b$'),((1.35,-1),r'$\bar b$')]:a.text(*xy,lab)
a=axs[0,1];setup(a,r'Tree $H\to b\bar b$');line(a,(-1.3,0),(0,0),'higgs',label='$H$');line(a,(0,0),(1.3,.8));line(a,(1.3,-.8),(0,0));a.text(1.3,.9,'$b$');a.text(1.3,-1,r'$\bar b$')
def triangle(ax,out,inside,title):
 setup(ax,title);A=(-.65,0);B=(.4,.6);C=(.4,-.6);line(ax,(-1.4,0),A,'higgs',label='$H$')
 for p,q in [(A,B),(B,C),(C,A)]:line(ax,p,q,'fermion' if inside=='t' else 'W',arrow=inside=='t')
 line(ax,B,(1.4,.9),out);line(ax,C,(1.4,-.9),out)
 ax.text(-.02,-.02,'$t$' if inside=='t' else r'$W^\pm$',ha='center')
 lab='$g$' if out=='gluon' else r'$\gamma$';ax.text(1.4,1,lab);ax.text(1.4,-1.1,lab)
triangle(axs[0,2],'gluon','t',r'Quark loop: $H\to gg$')
triangle(axs[1,0],'photon','t',r'Charged-fermion loop: $H\to\gamma\gamma$')
triangle(axs[1,1],'photon','W',r'Charged-W triangle: $H\to\gamma\gamma$')
a=axs[1,2];setup(a,r'W contact topology: $H\to\gamma\gamma$');line(a,(-1.4,0),(-.5,0),'higgs',label='$H$')
t=np.linspace(0,np.pi,260)
for sign in [-1,1]:
 x=.05-.55*np.cos(t);y=sign*.45*np.sin(t);dy=.02*np.sin(18*t);a.plot(x,y+dy,color='tab:blue',lw=1.2)
a.text(0,.62,r'$W^\pm$');line(a,(.6,0),(1.45,.85),'photon');line(a,(.6,0),(1.45,-.85),'photon');a.text(1.45,.95,r'$\gamma$');a.text(1.45,-1.05,r'$\gamma$');a.scatter([-.5,.6],[0,0],s=12,color='black')
fig.suptitle('Representative lowest-order topologies; include loop orientations and photon permutations',fontsize=11,y=1.02)

fig.tight_layout()
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white',bbox_inches='tight')
plt.close(fig)
