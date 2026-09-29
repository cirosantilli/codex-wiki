"""Original explanatory schematic. Python 3.14; NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

def velocity(z):return np.where(z<=1,1+z,np.where(z<=1.2,3-z,.6+z))
def segments(p):return [(0,1/p-1,1,1)] if p>.5 else [(0,1,1,1),(1,1.2,2,-1),(1.2,1/p-.6,1.8,1)]
def quantities(p):
 x=T=0.
 for za,zb,va,g in segments(p):
  vb=va+g*(zb-za);sa=np.sqrt(max(0,1-(p*va)**2));sb=np.sqrt(max(0,1-(p*vb)**2));x+=2*(sa-sb)/(p*g);T+=2*(np.arctanh(sa)-np.arctanh(sb))/g
 return x,T,T-p*x
fig,aa=plt.subplots(2,3,figsize=(12,7.3),layout='constrained');a=aa.ravel();z=np.linspace(0,5,800)
a[0].plot(velocity(z),z,c='k');a[0].axhspan(1,1.2,color='#f3c7ac');a[0].set(xlabel='speed',ylabel='depth',title='Specified illustrative profile',ylim=(4.5,0),xlim=(.8,5.2))
for p in [.97,.85,.7,.55,.499,.47,.4,.32,.24,.19]:
 xx=[];zz=[];offset=0
 for za,zb,va,g in segments(p):
  zs=np.linspace(za,zb,140);vs=va+g*(zs-za);sa=np.sqrt(max(0,1-(p*va)**2));xs=offset+(sa-np.sqrt(np.maximum(0,1-(p*vs)**2)))/(p*g);xx.extend(xs);zz.extend(zs);offset=xs[-1]
 xx=np.array(xx);zz=np.array(zz);col='#2871a1' if p>.5 else '#b34f28';a[1].plot(np.r_[xx,2*offset-xx[::-1]],np.r_[zz,zz[::-1]],c=col,lw=.8)
a[1].axhspan(1,1.2,color='#f3c7ac',zorder=-2);a[1].set(xlabel='range',ylabel='depth',ylim=(4.7,0),xlim=(0,13),title='Turning rays; no turns in the reversal')
for ps,col,label in [(np.linspace(.50000001,.99999,1400),'#2871a1','shallow branch'),(np.linspace(.15,.49999999,2000),'#b34f28','deep branch')]:
 vals=np.array([quantities(p) for p in ps]);x,T,tau=vals.T;a[2].plot(x,T,c=col,label=label);a[3].plot(ps,x,c=col);a[4].plot(ps,tau,c=col)
a[2].set(xlabel='range x',ylabel='travel time T',title='All travel-time branches',xlim=(0,14),ylim=(0,8));a[2].legend(fontsize=8)
a[3].set(xlabel='ray parameter p',ylabel='range x(p)',title='Range–slowness curve',xlim=(.1,1),ylim=(0,14));a[4].set(xlabel='ray parameter p',ylabel='intercept time τ(p)',title='Separate intercept-time branches',xlim=(.1,1))
for ax in a[3:5]:ax.axvline(.5,c='gray',ls=':',lw=1)
a[5].axis('off');a[5].text(.03,.9,'Dimensionless illustrative model\n\nv = 1 + z,       0 ≤ z ≤ 1\nv = 3 − z,       1 ≤ z ≤ 1.2\nv = 0.6 + z,    z ≥ 1.2\n\nBlue: turn above the reversal\nOrange: penetrate and turn below\n\nBranches are not joined across p = 0.5.\nDeep-branch folding permits multiple\narrivals outside the shadow range.',va='top',fontsize=10)
for ax in a[:5]:ax.grid(alpha=.18)
fig.suptitle('Original ray tracing through a thin low-velocity zone')

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
