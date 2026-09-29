"""Original comparison plot; emit PNG basename in cwd. Python3.14.4, NumPy2.3.5, Matplotlib3.10.7."""
import math
import os
from pathlib import Path
if not os.environ.get('MPLCONFIGDIR'):
 raise RuntimeError('Supply MPLCONFIGDIR, normally through the root Makefile.')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def survival(eps,n=None):
 if eps==0:return 0.0
 lo,hi=0.0,1.0-1e-14
 for _ in range(80):
  r=(lo+hi)/2
  val=-math.log1p(-r)/r-(1+eps) if n is None else (-math.log1p(-r)+n*math.log1p(-(1+eps)*r/n))/r
  if val>0:hi=r
  else:lo=r
 return (lo+hi)/2

def main():
 x=np.linspace(0,0.35,351)
 fig,axes=plt.subplots(1,2,figsize=(1120/100+1e-9,460/100+1e-9),dpi=100,facecolor='white')
 ax=axes[0]
 ax.plot(x,[survival(float(e),2) for e in x],label='Binomial offspring: n = 2',color='#c2410c',lw=2.1)
 ax.plot(x,[survival(float(e)) for e in x],label='Poisson offspring',color='#1565c0',lw=2.1)
 ax.plot(x,2*x,'--',label='Printed upper bound: 2ε',color='#555555')
 ax.plot(x,2*x/(1+2*x),':',label='Poisson lower bound',color='#00897b',lw=2)
 e=.05;r=4*e/(1+e)**2
 ax.scatter([e],[r],c='#c2410c',s=28,zorder=5)
 ax.annotate('ε = 0.05: ρ = 80/441 > 0.10',xy=(e,r),xytext=(.015,.43),fontsize=9,arrowprops={'arrowstyle':'->','color':'#444444'})
 ax.set(xlabel='Excess offspring mean ε',ylabel='Survival probability ρ',title='Finite-binomial correction',xlim=(0,.35),ylim=(0,.85))
 ax.legend(loc='upper left',fontsize=8.8,framealpha=.95)
 ax.grid(alpha=.18)
 ax=axes[1];t=np.linspace(0,2.6,350);drift=t-t*t/2
 ax.plot(t,drift,color='#1565c0',lw=2.1,label='Leading drift: s − s²/2')
 ax.fill_between(t,0,drift,where=drift>=0,color='#1565c0',alpha=.13)
 ax.axhline(0,color='#777777',lw=.8)
 for u in [0,2]:ax.axvline(u,color='#777777',lw=.8,ls=':')
 ax.annotate('Positive drift sustains one component',xy=(1,.5),xytext=(.15,.66),fontsize=9)
 ax.set(xlabel='Explored vertices / (ε n)',ylabel='Leading active-count drift / (ε² n)',title='Barely-supercritical exploration',xlim=(0,2.6),ylim=(-.9,.85))
 ax.legend(loc='lower left',fontsize=9);ax.grid(alpha=.18)
 fig.tight_layout(pad=1.3)
 fig.savefig(Path.cwd()/'paper-9-branching-survival.png',dpi=100,facecolor='white',transparent=False)
 plt.close(fig)
if __name__=='__main__':main()
