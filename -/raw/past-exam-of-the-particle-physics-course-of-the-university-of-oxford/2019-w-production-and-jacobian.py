"""Original W production diagram and Jacobian spectrum; Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots(1,2,figsize=(10.5,4.1),facecolor='white')
fig.subplots_adjust(left=.04,right=.97,bottom=.18,top=.81,wspace=.25)
a=ax[0];a.set(xlim=(0,1),ylim=(0,1));a.axis('off')
a.set_title(r'$u\bar d\to W^+\to\ell^+\nu_\ell$',fontsize=16)
def ferm(start,end,rev=False):
 a.plot(*zip(start,end),color='#163d5b',lw=1.8)
 p=np.array(start);d=np.array(end)-p
 a.annotate('',xy=p+(.42 if rev else .65)*d,xytext=p+(.65 if rev else .42)*d,arrowprops={'arrowstyle':'-|>','color':'#163d5b','lw':1.2})
l,r=(.32,.5),(.68,.5)
ferm((.03,.83),l);ferm((.03,.17),l,True)
ferm(r,(.97,.83),True);ferm(r,(.97,.17))
x=np.linspace(.32,.68,250);a.plot(x,.5+.025*np.sin(np.linspace(0,8*np.pi,len(x))),color='#a34100',lw=1.6)
for p in [l,r]:a.plot(*p,'o',color='black',ms=3)
for x,y,label in [(.07,.93,r'$u\ (h=-1/2)$'),(.08,.07,r'$\bar d\ (h=+1/2)$'),(.90,.93,r'$\ell^+\ (h=+1/2)$'),(.90,.07,r'$\nu_\ell\ (h=-1/2)$'),(.5,.67,r'$W^+,\ J_z=-1$')]:a.text(x,y,label,ha='center',fontsize=12)
a.text(.5,-.09,'Spin axis: incoming proton-side up quark',ha='center',fontsize=10)
x=np.linspace(0,.999,1200)
f=.75*x*(2-x*x)/np.sqrt(1-x*x)
b=ax[1];b.plot(x,f,color='#126782',lw=2);b.axvline(1,color='#a34100',ls='--',lw=1)
b.set(xlim=(0,1.06),ylim=(0,6),xlabel=r'$x=2p_T/M_W$',ylabel=r'$(1/\Gamma)\,d\Gamma/dx$',title='Fixed mass, zero transverse recoil')
b.text(.56,5.2,'Integrable endpoint\nat $p_T=M_W/2$',ha='center',fontsize=11)
b.grid(alpha=.18)
fig.suptitle('Charged-current spin correlation and transverse momentum',fontsize=17,y=.97)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
