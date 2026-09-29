"""Original connected and annihilation phi-decay topologies; Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
fig,axes=plt.subplots(1,3,figsize=(12,4.1),facecolor='white')
fig.subplots_adjust(left=.025,right=.98,bottom=.14,top=.80,wspace=.20)
for a in axes:a.set(xlim=(0,1),ylim=(0,1));a.axis('off')
def line(a,p,q,label=None,rev=False):
 a.plot(*zip(p,q),color='#163d5b',lw=1.6)
 p=np.array(p);d=np.array(q)-p
 a.annotate('',xy=p+(.38 if rev else .62)*d,xytext=p+(.62 if rev else .38)*d,arrowprops={'arrowstyle':'-|>','color':'#163d5b','lw':1})
 if label:a.text(*(p+.5*d+np.array([0,.06])),label,ha='center',fontsize=12)
def wave(a,p,q,label=None):
 p=np.array(p);d=np.array(q)-p;t=np.linspace(0,1,180);normal=np.array([-d[1],d[0]])/np.linalg.norm(d)
 z=p[:,None]+d[:,None]*t+normal[:,None]*.018*np.sin(12*np.pi*t)
 a.plot(z[0],z[1],color='#a34100',lw=1.2)
 if label:a.text(*((p+q)/2+np.array([0,.08])),label,ha='center',fontsize=11)
a=axes[0];a.set_title('Connected strange-line survival',fontsize=12)
line(a,(.03,.85),(.94,.85),r'$s$');line(a,(.03,.15),(.94,.15),r'$\bar s$',True)
wave(a,(.33,.85),(.53,.50),'$g$')
line(a,(.53,.50),(.94,.70),r'$\bar u$',True);line(a,(.53,.50),(.94,.30),r'$u$')
a.text(.97,.78,r'$K^-$',ha='left',fontsize=12);a.text(.97,.22,r'$K^+$',ha='left',fontsize=12)
a.text(.5,-.06,'Original strange flavours survive',ha='center',fontsize=10)
a=axes[1];a.set_title('Annihilation into pions',fontsize=12)
line(a,(.02,.85),(.25,.75),r'$s$');line(a,(.02,.15),(.25,.25),r'$\bar s$',True)
line(a,(.25,.75),(.25,.25))
for y in [.3,.5,.7]:wave(a,(.25,y),(.65,y))
a.text(.46,.87,'3 gluons',ha='center',fontsize=11)
a.add_patch(Circle((.74,.5),.23,facecolor='#e1e8ed',edgecolor='#526777'))
for y,lab in [(.82,r'$\pi$'),(.50,r'$\pi$'),(.18,r'$\pi$')]:
 a.plot([.85,.99],[.5,y],color='#526777',lw=1.2);a.text(.99,y,lab,ha='left',fontsize=12)
a.text(.5,-.06,'Disconnected flavour topology: OZI suppressed',ha='center',fontsize=10)
a=axes[2];a.set_title('Electromagnetic annihilation',fontsize=12)
line(a,(.02,.85),(.30,.5),r'$s$');line(a,(.02,.15),(.30,.5),r'$\bar s$',True)
wave(a,(.30,.5),(.67,.5),r'$\gamma^*$')
line(a,(.67,.5),(.98,.85),r'$\ell^-$');line(a,(.67,.5),(.98,.15),r'$\ell^+$',True)
a.text(.5,-.06,r'Width proportional to $\alpha^2$',ha='center',fontsize=10)
fig.suptitle(r'Decay topologies of a predominantly $s\bar s$ vector meson',fontsize=17,y=.97)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
