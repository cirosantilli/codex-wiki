"""Original schematic; run in its directory. Python/deps pinned in pyproject.toml."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/2018-paper-333-mpl-cache')
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(10,4.8),dpi=100,facecolor='white',layout='constrained')
x=np.linspace(-3,3,181); y=np.linspace(-2.2,2.2,151); X,Y=np.meshgrid(x,y)
I=np.array([math.sqrt(math.pi)/2*math.erfc(v) for v in x])
psi=np.exp(-Y*Y)*I[np.newaxis,:]; u=2*Y*psi; v=-np.exp(-X*X-Y*Y)
axs[0].contour(X,Y,psi,levels=[.04,.12,.3,.6,1,1.5],colors='#3d6b98',linewidths=.85)
axs[0].streamplot(x,y,u,v,density=.8,color='#183c5b',linewidth=.85,arrowsize=1.1)
axs[0].plot(0,0,'o',color='#c96c23',markersize=5)
axs[0].set(title='Surface flow: open western streamlines',xlabel=r'$x/L$',ylabel=r'$y/L$',xlim=(-3,3),ylim=(-2.2,2.2))
ys=np.linspace(-2.3,2.3,19); zs=np.linspace(-4,0,17); YY,ZZ=np.meshgrid(ys,zs)
vs=-(1+ZZ)*np.exp(ZZ-YY*YY); ws=-ZZ*np.exp(ZZ-YY*YY)
# Components separately nondimensionalized by their analytical scales; arrows show directions.
axs[1].quiver(YY,ZZ,vs,ws,color='#183c5b',angles='xy',scale_units='xy',scale=2.7,width=.0045)
axs[1].axhline(-1,color='#888888',linestyle='--',linewidth=.8)
axs[1].axhline(0,color='#333333',linewidth=1)
axs[1].text(1.1,-.62,'southward',fontsize=9); axs[1].text(1.1,-2.5,'northward',fontsize=9)
axs[1].text(-2.2,-3.8,'Upwelling; projected 3D flow',fontsize=9)
axs[1].set(title=r'Meridional/vertical directions at $x=0$',xlabel=r'$y/L$',ylabel=r'$z/H$',xlim=(-2.4,2.4),ylim=(-4.1,.12))
fig.savefig(Path.cwd()/'paper-333-heating-circulation.png',facecolor='white',transparent=False,dpi=100)
plt.close(fig)
