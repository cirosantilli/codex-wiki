"""Original javelin/shed diagrams; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
PNG basename is written to caller CWD; caller MPLCONFIGDIR is honored.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig, axes=plt.subplots(1,2,figsize=(10.6,5.6),layout='constrained',facecolor='white')
colors={'rear':'#be661f','front':'#175c98','entrance':'#151515','back':'#777777','slice':'#21855b'}
T=np.linspace(-1.6,1.2,500)
a=axes[0]
a.plot(np.zeros_like(T),T,color=colors['entrance'],label='Shed entrance')
a.plot(np.full_like(T,1.5),T,color=colors['back'],label='Shed back')
for name,x in [('rear',.8*T),('front',.8*T+1.2)]:
    prior=T<=.375
    a.plot(x[prior],T[prior],color=colors[name],lw=2,label='Javelin '+('trailing end' if name=='rear' else 'leading end'))
    a.plot(x[~prior],T[~prior],color=colors[name],lw=1.5,ls='--')
x=np.linspace(.8*.18,.8*.18+1.2,100)
a.plot(x,np.full_like(x,.18),color=colors['slice'],lw=3,label='One simultaneous S slice')
a.scatter([0,1.5],[0,.375],color='#b21f35',zorder=5,s=28)
a.annotate('A',(0,0),xytext=(-16,-16),textcoords='offset points',color='#b21f35',weight='bold')
a.annotate('B',(1.5,.375),xytext=(9,10),textcoords='offset points',color='#b21f35',weight='bold')
a.set(xlim=(-1.0,2.8),ylim=(-1.6,1.2),xlabel='x (m)',ylabel='ct (m)',title='S: shed at rest')
a.legend(fontsize=8,loc='lower right',framealpha=.95)
Tp=np.linspace(-2,1.0,500);a=axes[1]
a.plot(-.8*Tp,Tp,color=colors['entrance'],label='Shed entrance')
a.plot(.9-.8*Tp,Tp,color=colors['back'],label='Shed back')
for name,xp,cut in [('rear',0.,.225),('front',2.,-1.375)]:
    prior=Tp<=cut
    a.plot(np.full(np.sum(prior),xp),Tp[prior],color=colors[name],lw=2)
    a.plot(np.full(np.sum(~prior),xp),Tp[~prior],color=colors[name],lw=1.5,ls='--')
xp=np.linspace(0,2,100)
a.plot(xp,.108-.8*xp,color=colors['slice'],lw=3)
a.annotate('Same S slice:\nnot simultaneous in S\N{PRIME}',(.9,-.612),xytext=(-12,14),textcoords='offset points',fontsize=9,color=colors['slice'])
a.scatter([0,2],[0,-1.375],color='#b21f35',zorder=5,s=28)
a.annotate('A',(0,0),xytext=(-18,6),textcoords='offset points',color='#b21f35',weight='bold')
a.annotate('B',(2,-1.375),xytext=(10,-4),textcoords='offset points',color='#b21f35',weight='bold')
a.set(xlim=(-1.2,3.0),ylim=(-2,1.0),xlabel='x\N{PRIME} (m)',ylabel='ct\N{PRIME} (m)',title='S\N{PRIME}: javelin initially at rest')
a.text(.04,.04,'Dashed: initial-motion extrapolation\nafter first impact in S',transform=a.transAxes,fontsize=9,bbox={'facecolor':'white','alpha':.9,'edgecolor':'none'})
for a in axes:
    a.set_facecolor('white');a.grid(alpha=.15)
fig.savefig(Path('paper-4-javelin-spacetime.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
