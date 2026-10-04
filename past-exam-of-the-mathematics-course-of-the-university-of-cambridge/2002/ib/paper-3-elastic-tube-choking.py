"""Plot elastic-tube flow branches; write the PNG basename in caller CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def H(s,lam):return 1-s**(-.5)+lam*(1-s*s)/4

def bisect(fn,lo,hi):
 for _ in range(65):
  mid=(lo+hi)/2
  if fn(lo)*fn(mid)<=0:hi=mid
  else:lo=mid
 return (lo+hi)/2

fig,axes=plt.subplots(1,3,figsize=(10.6,3.8),layout='constrained',facecolor='white')
for ax,lam,xmax,title in zip(axes,[.25,1.,4.],[4.4,2.5,1.75],['Lower-speed branch selected','Upstream state is critical','Higher-speed branch selected']):
 sc=lam**(-.4);hc=1+lam/4-1.25*lam**.2
 ss=np.linspace(.035,xmax,1400)
 ax.axhspan(0,max(.21,hc+.18),color='#f4f7fb',zorder=0)
 ax.plot(ss,H(ss,lam),color='#253b57',lw=2)
 ax.axhline(0,color='#777777',lw=.8)
 ax.axvline(sc,color='#b44332',ls=':',lw=1)
 ax.plot(sc,hc,'o',color='#b44332',ms=5)
 ax.plot(1,0,'o',color='#276bad',ms=5)
 ax.annotate('upstream',(1,0),xytext=(7,-20),textcoords='offset points',fontsize=8,color='#276bad')
 ax.annotate(r'$h_c/R$',(sc,hc),xytext=(5,8),textcoords='offset points',fontsize=9,color='#b44332')
 if lam!=1:
  level=hc/2;low=bisect(lambda s:H(s,lam)-level,.035,sc);high=bisect(lambda s:H(s,lam)-level,sc,xmax)
  ax.axhline(level,color='#438159',ls='--',lw=1)
  selected=low if lam<1 else high
  ax.plot([low,high],[level,level],'o',mfc='white',mec='#438159',ms=5)
  ax.plot(selected,level,'o',color='#438159',ms=5)
  ax.annotate('chosen',(selected,level),xytext=(6,-18),textcoords='offset points',fontsize=8,color='#438159')
 ax.set(xlim=(0,xmax),ylim=(-.45,max(.21,hc+.18)),xlabel=r'$s=u/V$',ylabel=r'$h/R$')
 ax.set_title(r'$\lambda='+str(lam)+r'$'+'\n'+title,fontsize=10)
 ax.grid(alpha=.16)
fig.suptitle('Prescribed wall thickness and the two velocity branches',fontsize=13)
fig.savefig(Path('paper-3-elastic-tube-choking.png'),dpi=150,facecolor='white')
plt.close(fig)
