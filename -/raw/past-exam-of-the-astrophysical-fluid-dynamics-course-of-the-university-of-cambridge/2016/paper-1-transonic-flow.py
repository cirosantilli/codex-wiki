"""Original explanatory plot. Tested with Python 3.14, numpy and matplotlib; PNG output goes to the current directory."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
# Example gamma=7/5. Values are computed from the area–Mach relation, not traced from a source figure.
gamma=7/5
x=np.linspace(-.5,.5,701);area=4*(1-.5*np.exp(-16*x*x))**2
def area_mach(m):return (2/(gamma+1)*(1+(gamma-1)*m*m/2))**((gamma+1)/(2*(gamma-1)))/m
def invert(target,supersonic):
 if abs(target-1)<1e-13:return 1.
 lo,hi=(1.,10.) if supersonic else (1e-8,1.)
 for _ in range(70):
  m=(lo+hi)/2
  if (area_mach(m)>target)==supersonic:hi=m
  else:lo=m
 return (lo+hi)/2
mach=np.array([invert(a,z>0) for a,z in zip(area,x)]);temp=(gamma+1)/(2+(gamma-1)*mach*mach)
fig,axs=plt.subplots(3,1,figsize=(7.9,6.4),sharex=True,layout='constrained')
for a,y,label,col in zip(axs,[area,mach,temp],[r'$A/A_s$',r'Mach number $M$',r'$T/T_s$'],['#357ba0','#b66a36','#498755']):
 a.plot(x,y,color=col,lw=2);a.axvline(0,color='#999',lw=.9,ls='--');a.set(ylabel=label);a.grid(alpha=.17);a.plot(0,1,'ko',ms=4)
axs[0].set_title(r'Computed smooth transonic branch, example $\gamma=7/5$');axs[1].axhline(1,ls=':',color='#888');axs[1].text(-.46,.6,'subsonic');axs[1].text(.22,2,'supersonic');axs[2].set_xlabel(r'Position $x/L$');axs[0].text(.02,1.15,'sonic throat',fontsize=9)
fig.savefig('paper-1-transonic-flow.png',dpi=160);plt.close(fig)
