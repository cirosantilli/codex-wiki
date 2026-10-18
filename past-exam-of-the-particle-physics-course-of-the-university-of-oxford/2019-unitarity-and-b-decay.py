"""Original CKM geometry and neutral-B mixing/decay diagrams; Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,axes=plt.subplots(2,2,figsize=(10.9,7.8),facecolor='white')
fig.subplots_adjust(left=.06,right=.95,bottom=.07,top=.90,wspace=.34,hspace=.45)
a=axes[0,0];rho,eta=.18,.36
a.plot([0,1,rho,0],[0,0,eta,0],color='#126782',lw=2)
for x,y,t in [(0,0,'0'),(1,0,'1'),(rho,eta,r'$\bar\rho+i\bar\eta$')]:a.plot(x,y,'o',color='#126782');a.text(x,y+.03,t,ha='center',fontsize=12)
a.text(.17,.04,r'$\gamma$',fontsize=14);a.text(.79,.04,r'$\beta$',fontsize=14);a.text(rho+.035,eta-.105,r'$\alpha$',fontsize=14)
a.set(xlim=(-.08,1.08),ylim=(-.10,.50),xlabel='Real part',ylabel='Imaginary part',title='Normalized unitarity triangle')
a.spines[['top','right']].set_visible(False)
def line(a,p,q,label=None,rev=False):
 a.plot(*zip(p,q),color='#163d5b',lw=1.6);p=np.array(p);d=np.array(q)-p
 a.annotate('',xy=p+(.37 if rev else .63)*d,xytext=p+(.63 if rev else .37)*d,arrowprops={'arrowstyle':'-|>','color':'#163d5b','lw':1})
 if label:a.text(*(p+.5*d+np.array([0,.07])),label,ha='center',fontsize=12)
def wave(a,p,q,label=None):
 p=np.array(p);q=np.array(q);d=q-p;t=np.linspace(0,1,180);v=np.array([-d[1],d[0]])/np.linalg.norm(d)
 z=p[:,None]+d[:,None]*t+v[:,None]*.016*np.sin(10*np.pi*t);a.plot(z[0],z[1],color='#a34100',lw=1.2)
 if label:a.text(*((p+q)/2+np.array([.10,0])),label,ha='center',fontsize=12)
def setup(a,title):a.axis('off');a.set(xlim=(0,1),ylim=(0,1));a.set_title(title,fontsize=12)
a=axes[0,1];setup(a,r'$B^0=d\bar b\ \to\ \bar B^0=\bar d b$')
tl,tr,bl,br=(.27,.73),(.73,.73),(.27,.27),(.73,.27)
line(a,(.02,.92),tl,r'$\bar b$',True);line(a,(.02,.08),bl,r'$d$')
line(a,tr,(.98,.92),r'$\bar d$',True);line(a,br,(.98,.08),r'$b$')
line(a,tl,tr,r'$\bar t$',True);line(a,bl,br,r'$t$');wave(a,tl,bl,r'$W^+$');wave(a,tr,br,r'$W^-$')
a.text(.50,-.06,'Top-dominated box; lighter up-type loops also exist',ha='center',fontsize=9)
a=axes[1,0];setup(a,r'Tree path: $B^0\to J/\psi K^0$')
line(a,(.02,.86),(.33,.72),r'$\bar b$',True);line(a,(.33,.72),(.98,.85),r'$\bar c$',True)
wave(a,(.33,.72),(.58,.43),r'$W^+$')
line(a,(.58,.43),(.98,.64),r'$c$');line(a,(.58,.43),(.98,.35),r'$\bar s$',True)
line(a,(.02,.13),(.98,.13),r'$d$')
a.text(.99,.75,r'$J/\psi$',fontsize=11);a.text(.99,.23,r'$K^0$',fontsize=11)
a=axes[1,1];setup(a,'Two coherent paths to one final state')
a.text(.5,.78,r'$B^0\ \longrightarrow\ f$',fontsize=18,ha='center')
a.text(.5,.52,r'$B^0\ \longrightarrow\ \bar B^0\ \longrightarrow\ f$',fontsize=17,ha='center')
a.text(.5,.24,r'$f=J/\psi K_S,\qquad \lambda_f\simeq-e^{-2i\beta}$',fontsize=16,ha='center')
fig.suptitle('CKM phase geometry and interference in neutral-B decays',fontsize=17,y=.97)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
