"""Original explanatory figure; run under Python 3.14 with numpy and matplotlib.
Writes its PNG basename to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,3,figsize=(10,3.7),layout='constrained');t=np.linspace(0,2*np.pi,500)
for ax,A,B,delta,title in zip(axs,[1,1,1],[.65,1,.55],[0,np.pi/2,np.pi/3],['Linear: phase difference 0',r'Circular: $A=B$, $\delta=\pi/2$',r'Elliptical: $A\ne B$, $\delta=\pi/3$']):
 x=A*np.cos(t);y=B*np.cos(-t+delta);ax.plot(x,y,color='#1766a5',lw=2)
 for st in [.2,2.3,4.3]:
  en=st+.18;p=(A*np.cos(st),B*np.cos(-st+delta));q=(A*np.cos(en),B*np.cos(-en+delta));ax.annotate('',q,p,arrowprops=dict(arrowstyle='->',color='#c33c29',lw=2))
 ax.axhline(0,lw=.5,color='gray');ax.axvline(0,lw=.5,color='gray');ax.set(xlim=(-1.2,1.2),ylim=(-1.2,1.2),xlabel=r'$u_x$',ylabel=r'$u_y$',title=title,aspect='equal');ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
fig.suptitle('At fixed z = 0; arrows show increasing time');fig.savefig('paper-2-polarization.png',dpi=170);plt.close(fig)
