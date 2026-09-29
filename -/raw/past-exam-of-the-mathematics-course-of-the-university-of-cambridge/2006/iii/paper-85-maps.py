"""Original Hénon branches and odd-map local bifurcation sketch."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
fig,axs=plt.subplots(1,2,figsize=(12.3,5.3),layout='constrained')
ax=axs[0]
m=np.linspace(-1,5,900);root=np.sqrt(m+1)
ax.plot(m,-1-root,'k--',lw=1.4)
for mask,style,col in [(m<=3,'-','#2166ac'),(m>=3,'--','black')]:ax.plot(m[mask],(-1+root)[mask],style,color=col,lw=1.8)
p=np.linspace(3,5,500)
for sign in [-1,1]:
 y=1+sign*np.sqrt(p-3)
 for mask,style,col in [(p<=4,'-','#e08214'),(p>=4,'--','black')]:ax.plot(p[mask],y[mask],style,color=col,lw=1.7)
for loc in [-1,3,4]:ax.axvline(loc,color='#999999',ls=':',lw=.8)
ax.plot([-1,3],[-1,1],'ko',ms=4)
ax.set(xlabel=r'$\mu$',ylabel=r'$y$',xlim=(-1.2,5),ylim=(-3.6,3),title=r'Hénon map at $b=1$ (no attracting branches)')
ax.legend(handles=[Line2D([],[],color='#2166ac',label='elliptic fixed point'),Line2D([],[],color='#e08214',label='elliptic 2-cycle values'),Line2D([],[],color='k',ls='--',label='hyperbolic saddle')],fontsize=8,loc='lower right')
ax.text(-.9,-.7,'fold',fontsize=8);ax.text(3.03,.7,'flip',fontsize=8)
ax=axs[1]
ax.axvspan(-2,0,ymin=.6/3.2,ymax=2.6/3.2,facecolor='#d9f0d3')
superc='#0072b2';subc='#cc3366'
for a,segments in [(0,[(-.6,2,superc),(2,2.6,subc)]),(-2,[(-.6,0,superc),(0,2.6,subc)])]:
 for lo,hi,col in segments:ax.plot([a,a],[lo,hi],color=col,lw=2)
for b,segments in [(0,[(-2.8,-2,superc),(-2,-1,subc),(-1,.8,superc)]),(2,[(-2.8,-1,subc),(-1,0,superc),(0,.8,subc)])]:
 for lo,hi,col in segments:ax.plot([lo,hi],[b,b],color=col,lw=2)
ax.text(-1.15,1.1,'stable origin',ha='center',fontsize=10)
# Arrows locate nearby branches along stable-box boundaries.
for start,end in [((0,1),(.45,1)),((-2,1),(-1.6,1)),((-1.6,0),(-1.6,.35)),((-.45,0),(-.45,-.35)),((-1.6,2),(-1.6,1.65)),((-.45,2),(-.45,2.35))]:
 ax.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',color='#444444',lw=1.2))
ax.plot([-1,-1],[0,2],'k*',ms=9)
ax.text(-.96,.14,'generalized flip',fontsize=7)
ax.text(-.96,1.82,'quintic pitchfork',fontsize=7)
ax.set(xlim=(-2.8,.8),ylim=(-.6,2.6),xlabel=r'$a$',ylabel=r'$b$',title='Triangular cubic map: branch sides')
ax.legend(handles=[Line2D([],[],color=superc,lw=2,label='supercritical (centre direction)'),Line2D([],[],color=subc,lw=2,label='subcritical (centre direction)')],fontsize=8,loc='upper left')
fig.savefig('paper-85-maps.png',dpi=150,facecolor='white',transparent=False)
