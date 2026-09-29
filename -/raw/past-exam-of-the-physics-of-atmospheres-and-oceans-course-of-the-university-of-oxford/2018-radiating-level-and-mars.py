"""Original effective emission level and diagnostic Mars mixed-layer calculation."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(11,4.6),layout='constrained',facecolor='white')
D=np.geomspace(.001,100,800);pressure=(1-D/np.expm1(D))/D;a=axes[0];a.plot(D,pressure,color='#355a9b',lw=2,label='exact linear-source mean');a.axhline(.5,color='#bd7820',ls='--',label='thin limit: 1/2');mask=D>1.8;a.plot(D[mask],1/D[mask],color='#269572',ls=':',lw=2,label='thick limit: 1 / D');a.set(xscale='log',xlabel='total effective optical depth D',ylabel='emission pressure / surface pressure',ylim=(0,.6),title='A  Two-stream emission weighting');a.legend(frameon=False,fontsize=9)
sigma=5.670374419e-8;F=.8*584/4;top=(F/(2*sigma))**.25;ground=top*3.25**.25
z=np.linspace(0,25,600);trad=top*(1+1.25*np.exp(-z/10))**.25;tad=ground-4.4*z;lo,hi=0,25
for _ in range(70):
 mid=(lo+hi)/2
 if ground-4.4*mid>top*(1+1.25*np.exp(-mid/10))**.25:lo=mid
 else:hi=mid
zm=(lo+hi)/2;a=axes[1];a.axhspan(0,zm,color='#e7eddb',label='diagnostic parcel layer');a.plot(trad,z,color='#355a9b',lw=2,label='unadjusted radiative air');a.plot(tad,z,color='#bd7820',lw=2,label='surface-launched adiabat');a.scatter([ground,trad[0]],[0,0],color=['#a43838','#355a9b'],zorder=4);a.plot([trad[0],ground],[0,0],color='#a43838',lw=3);a.scatter([ground-4.4*zm],[zm],color='#333',zorder=5);a.annotate(f'intersection ≈ {zm:.1f} km',(ground-4.4*zm,zm),(205,13),arrowprops={'arrowstyle':'->'});a.set(xlabel='temperature (K)',ylabel='height (km)',xlim=(160,250),ylim=(-.4,25),title='B  Mars: ground–air jump drives the estimate');a.legend(frameon=False,fontsize=8.5,loc='upper right')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
