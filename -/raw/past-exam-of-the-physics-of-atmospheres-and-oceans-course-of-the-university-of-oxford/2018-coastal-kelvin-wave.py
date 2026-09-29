"""Original coastal Kelvin bulge and conserved-flux amplitude curves."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(11,4.8),layout='constrained',facecolor='white')
x=np.linspace(-3,0,220);y=np.linspace(-3,3,260);X,Y=np.meshgrid(x,y);eta=np.exp(X)*np.exp(-Y*Y/(2*.8**2));a=axes[0];a.contourf(X,Y,eta,levels=np.linspace(0,1,14),cmap='Blues');a.axvspan(0,.45,color='#ddd7c8');a.axvline(0,color='#444',lw=2)
xq=np.linspace(-2.7,-.25,6);yq=np.linspace(-2.5,2.5,9);XQ,YQ=np.meshgrid(xq,yq);V=np.exp(XQ)*np.exp(-YQ*YQ/(2*.8**2));a.quiver(XQ,YQ,np.zeros_like(V),V,color='#333',angles='xy',scale_units='xy',scale=1.3,width=.004);a.text(-2.95,1.9,'ahead: convergence',fontsize=10);a.text(-2.95,-2.2,'behind: divergence',fontsize=10);a.annotate('northward\npropagation',xy=(.22,2),xytext=(.22,.2),ha='center',arrowprops={'arrowstyle':'->','lw':1.6},fontsize=9);a.text(.22,-2.7,'land',rotation=90,ha='center');a.set(xlabel='x / Rossby radius (ocean to left)',ylabel='alongshore distance (north ↑)',xlim=(-3,.45),ylim=(-3,3),title='A  Coast on the right of propagation')
h=np.linspace(.25,2,400);a=axes[1]
for f,color in [(.5,'#355a9b'),(1,'#bd7820'),(2,'#269572')]:a.plot(h,np.sqrt(f/h),lw=2,color=color,label=f'|f| / |f₀| = {f:g}')
a.set(xlabel='depth H / H₀',ylabel='coastal amplitude A / A₀',title='B  Conserved integrated flux: A²H / |f|');a.legend(frameon=False)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
