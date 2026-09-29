"""Original diagrams; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Write a PNG basename to the caller CWD. Preserve caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon
pi=np.pi
fig,axs=plt.subplots(1,2,figsize=(11.8,6.6),gridspec_kw={'width_ratios':[1.8,1]},facecolor='white')
fig.subplots_adjust(left=.075,right=.975,bottom=.19,top=.87,wspace=.38)
blue='#1764a0';future='#8d399f';past='#c46a13';null='#3b806a'
ax=axs[0];eta=np.linspace(-pi/2+.001,pi/2-.001,700)
ax.add_patch(Polygon([[0,-.5],[.5,0],[0,.5],[-.5,0]],facecolor='#e7eef5',edgecolor='none',zorder=0))
for sign in [-1,1]:
    ax.plot(sign*(pi/2-eta)/pi,eta/pi,color=future,lw=1.8)
    ax.plot(sign*(eta+pi/2)/pi,eta/pi,color=past,lw=1.8)
ax.plot(np.zeros_like(eta),eta/pi,color=blue,lw=2.3)
ax.plot((.95+np.arcsin(.6*np.sin(eta)))/pi,eta/pi,color=blue,lw=1.6)
ray=np.linspace(-.32,.28,100);ax.plot(ray,ray-.08,color=null,ls='--',lw=1.5)
ax.axhline(.5,color='black',lw=2);ax.axhline(-.5,color='black',lw=2)
for x in [-1,1]:ax.axvline(x,color='0.45',ls=':',lw=1.5)
ax.text(0,.56,'future infinity (spacelike)',ha='center',fontsize=10)
ax.text(-.91,-.465,'past infinity (spacelike)',ha='left',fontsize=9,bbox={'facecolor':'white','edgecolor':'none','alpha':.9,'pad':1})
ax.text(-1.04,0,'identified sides',rotation=90,ha='right',va='center',fontsize=9,color='0.35')
ax.text(-.20,.08,'static\npatch',ha='center',va='bottom',fontsize=9,color='0.35')
ax.set(xlim=(-1,1),ylim=(-.5,.5),xlabel=r'$\chi/\pi$',ylabel=r'$\eta/\pi$')
ax.set_xticks([-1,-.5,0,.5,1]);ax.set_yticks([-.5,0,.5]);ax.set_aspect('equal')
ax.set_title('de Sitter: conformal cylinder',fontsize=12,pad=38)
ax=axs[1];tau=np.linspace(-pi,pi,1001)
for E,sign in [(1.,1),(1.6,1),(2.4,-1)]:
    psi=np.arctan(sign*np.sqrt(E*E-1)*np.sin(tau))
    t=np.unwrap(np.arctan2(E*np.sin(tau),np.cos(tau)))
    ax.plot(psi/pi,t/pi,color=blue,lw=2 if E==1 else 1.6)
psi=np.linspace(-pi/2+.001,pi/2-.001,500)
for offset in [-.65,0,.65]:ax.plot(psi/pi,psi/pi+offset,color=null,ls='--',lw=1.3)
for x in [-.5,.5]:ax.axvline(x,color='black',lw=2)
ax.text(-.55,0,'timelike boundary',ha='right',va='center',rotation=90,fontsize=9)
ax.text(.55,0,'timelike boundary',ha='left',va='center',rotation=90,fontsize=9)
for y,direction in [(1.,1),(-1.,-1)]:
    ax.annotate('',xy=(.4,y+.12*direction),xytext=(.4,y-.02*direction),arrowprops={'arrowstyle':'->','lw':1.1},annotation_clip=False)
ax.text(0,1.15,'time continues',ha='center',fontsize=9)

ax.set(xlim=(-.5,.5),ylim=(-1,1),xlabel=r'$\psi/\pi$',ylabel=r'$t/\pi$')
ax.set_xticks([-.5,0,.5]);ax.set_yticks([-1,-.5,0,.5,1]);ax.set_aspect('equal')
ax.set_title('AdS universal cover: conformal strip',fontsize=12,pad=48)
for ax in axs:
    ax.set_facecolor('white');ax.grid(alpha=.12)
    ax.spines['top'].set_visible(False);ax.spines['right'].set_visible(False)
legend=[Line2D([],[],color=blue,lw=2,label='timelike geodesic'),Line2D([],[],color=null,ls='--',lw=1.5,label='null geodesic'),Line2D([],[],color=future,lw=1.8,label='future observer horizon'),Line2D([],[],color=past,lw=1.8,label='past observer horizon')]
fig.legend(handles=legend,loc='lower center',bbox_to_anchor=(.5,.06),ncol=2,frameon=False,fontsize=10)
fig.savefig('paper-55-conformal-structure.png',dpi=125,facecolor='white',transparent=False)
plt.close(fig)
