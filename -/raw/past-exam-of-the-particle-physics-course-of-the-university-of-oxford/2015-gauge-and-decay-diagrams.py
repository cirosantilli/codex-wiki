"""Original diagrams. Python 3.14, matplotlib 3.10, numpy 2.3.
Writes only the basename PNG in the CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white'})
fig,axs=plt.subplots(3,3,figsize=(13,11))
def ferm(ax,a,b,label,reverse=False,offset=(0,.055)):
    a,b=np.array(a),np.array(b);v=b-a
    ax.plot([a[0],b[0]],[a[1],b[1]],color='#263849',lw=1.7)
    p,q=a+.43*v,a+.62*v
    if reverse:p,q=q,p
    ax.annotate('',xy=q,xytext=p,arrowprops={'arrowstyle':'-|>','color':'#263849','lw':1.4})
    ax.text(*((a+b)/2+np.array(offset)),label,ha='center',va='center')
def boson(ax,a,b,label,gluon=False,offset=(0,.075)):
    a,b=np.array(a),np.array(b);v=b-a;n=np.array([-v[1],v[0]])/np.linalg.norm(v);t=np.linspace(0,1,300)
    curve=a[None,:]+t[:,None]*v[None,:]+(.025 if gluon else .018)*np.sin(t*14*np.pi)[:,None]*n[None,:]
    ax.plot(curve[:,0],curve[:,1],color='#b14c29',lw=1.4)
    ax.text(*((a+b)/2+np.array(offset)),label,ha='center',va='center',color='#903818')
def annihilation(ax,initial,final,mediator,gluon=False):
    v,w=(.34,.5),(.65,.5)
    ferm(ax,(.03,.85),v,initial[0]);ferm(ax,(.03,.15),v,initial[1],True,offset=(0,-.06))
    boson(ax,v,w,mediator,gluon)
    ferm(ax,w,(.97,.85),final[0]);ferm(ax,w,(.97,.15),final[1],True,offset=(0,-.06))
a=axs[0,0];boson(a,(.06,.5),(.45,.5),r'$\gamma,Z,g$')
ferm(a,(.45,.5),(.91,.85),r'$f_L$');ferm(a,(.45,.5),(.91,.15),r'$\bar f_R$',True,offset=(0,-.07))
a.text(.5,.03,r'Also $f_R\bar f_L$; $g$ only for quarks',ha='center',fontsize=9)
a=axs[0,1];boson(a,(.06,.5),(.45,.5),r'$W^-$')
ferm(a,(.45,.5),(.91,.85),r'$\ell^-_L$ or $d_L$');ferm(a,(.45,.5),(.91,.15),r'$\bar\nu_R$ or $\bar u_R$',True,offset=(0,-.06))
a.text(.5,.03,r'Quark vertex carries $V_{ij}$',ha='center',fontsize=9)
annihilation(axs[0,2],(r'$e^-_i$',r'$e^+_{\bar i}$'),(r'$\mu^-_j$',r'$\mu^+_{\bar j}$'),r'$\gamma,Z$')
axs[0,2].text(.5,.02,r'$i,j=L,R$; opposite antiparticle helicity',ha='center',fontsize=8.7)
annihilation(axs[1,0],(r'$q$',r'$\bar q$'),(r'$c$',r'$\bar c$'),r'$g^*$',True)
a=axs[1,1];boson(a,(.03,.85),(.34,.5),r'$g$',True,(-.01,.02));boson(a,(.03,.15),(.34,.5),r'$g$',True,(-.01,-.04));boson(a,(.34,.5),(.65,.5),r'$g^*$',True)
ferm(a,(.65,.5),(.97,.85),r'$c$');ferm(a,(.65,.5),(.97,.15),r'$\bar c$',True,offset=(0,-.06))
a=axs[1,2]
for x0,cross in [(0,False),(.53,True)]:
    top,bot=(x0+.23,.75),(x0+.23,.3)
    boson(a,(x0+.01,.85 if not cross else .12),top,r'$g$',True,(-.04,0));boson(a,(x0+.01,.12 if not cross else .85),bot,r'$g$',True,(-.04,0))
    ferm(a,bot,top,'',offset=(0,0));ferm(a,top,(x0+.46,.88),r'$c$',offset=(.02,.03));ferm(a,bot,(x0+.46,.12),r'$\bar c$',True,offset=(.02,-.04))
a.text(.5,.015,'Both heavy-quark exchange diagrams',ha='center',fontsize=9)
a=axs[2,0];annihilation(a,(r'$c$',r'$\bar s$'),(r'$\nu_\tau$',r'$\tau^+$'),r'$W^{+*}$')
a.plot([.015,.015],[.15,.85],ls='--',color='gray');a.text(.16,.99,r'$D_s^+=(c\bar s)$',ha='center');a.text(.5,.015,r'Also $D_s^-\to\tau^-\bar\nu_\tau$',ha='center',fontsize=9)
def decay(ax,leptonic):
    v,w=(.32,.75),(.56,.33)
    ferm(ax,(.02,.75),v,r'$\tau^-$',offset=(0,.08));ferm(ax,v,(.96,.85),r'$\nu_\tau$',offset=(.04,.07));boson(ax,v,w,r'$W^{-*}$',offset=(-.09,-.01))
    ferm(ax,w,(.96,.4),r'$\ell^-$' if leptonic else r'$d,s$',offset=(.02,.07));ferm(ax,w,(.96,.04),r'$\bar\nu_\ell$' if leptonic else r'$\bar u$',True,offset=(.01,-.06))
    ax.text(.32,.025,r'$\ell=e,\mu$' if leptonic else r'quarks $\to$ hadrons',ha='center',fontsize=9)
decay(axs[2,1],True);decay(axs[2,2],False)
titles=['Neutral chiral vertex','Charged chiral vertex','Lepton-pair annihilation','Charm: quark annihilation','Charm: gluon s channel','Charm: gluon t and u channels','Prompt tau-neutrino source','Leptonic tau decay','Hadronic tau decay']
for ax,title in zip(axs.flat,titles):
    ax.set(xlim=(-.06,1.05),ylim=(-.08,1.1));ax.axis('off');ax.set_title(title,pad=9,fontsize=11,fontweight='bold')
fig.tight_layout(h_pad=2,w_pad=1.3)
fig.savefig(Path('2015-gauge-and-decay-diagrams.png'),dpi=125,facecolor='white')
