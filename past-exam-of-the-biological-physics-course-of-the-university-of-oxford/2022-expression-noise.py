"""Seeded burst model and schematic clouds; Python 3.14, numpy 2.3.5, matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
rng=np.random.default_rng(2022)
def trajectory(mean,b,end=7):
    t=0.;n=0;ts=[t];ns=[n]
    arrivals=mean/b
    while t<end:
        total=arrivals+n
        t+=rng.exponential(1/total)
        if t>end: break
        if rng.random()<arrivals/total:n+=rng.geometric(1/(1+b))-1
        else:n-=1
        ts.append(t);ns.append(n)
    return np.array(ts),np.array(ns)/mean
fig=plt.figure(figsize=(11,7),layout='constrained')
grid=fig.add_gridspec(2,6)
for i,(mean,b) in enumerate([(10000,3),(10000,400),(100,3)]):
    a=fig.add_subplot(grid[0,2*i:2*i+2]);t,n=trajectory(mean,b)
    a.step(t,n,where='post',lw=.8,label='one sample path')
    s=np.linspace(0,7,300);a.plot(s,1-np.exp(-s),'k--',lw=1.5,label='ensemble mean')
    a.set(title=f'mean count {mean:,}; b = {b}',xlabel=r'time $\alpha_Pt$',ylabel='protein / stationary mean',ylim=(0,1.9),xlim=(0,7))
    cv=np.sqrt((1+b)/mean);a.text(.04,.93,f'stationary CV ≈ {cv:.2f}',transform=a.transAxes,va='top')
    if i==0:a.legend(fontsize=8,loc='lower right')
for j,(intrinsic,title) in enumerate([(.025,'Extrinsic noise dominates'),(.16,'Comparable intrinsic and extrinsic noise')]):
    a=fig.add_subplot(grid[1,3*j:3*j+3]);e=rng.normal(0,.16,350)
    x=1+e+rng.normal(0,intrinsic,350);y=1+e+rng.normal(0,intrinsic,350)
    a.scatter(x,y,s=7,alpha=.45)
    a.plot([.3,1.7],[.3,1.7],'k--',lw=1)
    a.set(xlabel='normalized cyan intensity',ylabel='normalized yellow intensity',title=title,xlim=(.3,1.7),ylim=(.3,1.7),aspect='equal')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
