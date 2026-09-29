"""Original teleportation and Bell-readout plots; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

fig, axs=plt.subplots(1,2,figsize=(13.5,5.0),layout='constrained',facecolor='white',gridspec_kw={'width_ratios':[1.4,1]})
a=axs[0]
for y in [0,-1,-2]:a.plot([.7,7],[y,y],color='#334155')
for y,t in [(0,r'$|\psi\rangle_1$'),(-1,r'$2$'),(-2,r'$3$')]:a.text(.5,y,t,ha='right',va='center',fontsize=12)
a.add_patch(Rectangle((.72,-2.2),.9,1.4,facecolor='#eff6ff',edgecolor='#2563eb',zorder=3));a.text(1.17,-1.5,r'$\Phi^+$',ha='center',va='center',fontsize=13)
a.text(1.3,-2.65,'Distribute photon 3\nbefore input arrives',ha='center',fontsize=10)
a.plot([2.5,2.5],[0,-1],color='#2563eb',lw=2);a.plot(2.5,0,'o',color='#2563eb',ms=7);a.add_patch(Circle((2.5,-1),.15,facecolor='white',edgecolor='#2563eb',lw=2,zorder=3));a.text(2.5,-1,'+',ha='center',va='center',fontsize=16,zorder=4)
def box(x,y,t,col='#2563eb'):
    a.add_patch(Rectangle((x-.28,y-.22),.56,.44,facecolor='white',edgecolor=col,zorder=3));a.text(x,y,t,ha='center',va='center',fontsize=12,zorder=4)
box(3.3,0,'H');box(4.2,0,'M');box(4.2,-1,'M');box(5.35,-2,r'$X^n$');box(6.35,-2,r'$Z^m$')
a.plot([4.2,6.35,6.35],[.25,.5,-1.76],ls='--',color='#dc2626',lw=1.5);a.text(5,.58,'m',color='#dc2626')
a.plot([4.2,5.35,5.35],[-1.25,-1.5,-1.76],ls='--',color='#dc2626',lw=1.5);a.text(4.65,-1.65,'n',color='#dc2626')
a.text(7.1,-2,r'$|\psi\rangle$',ha='left',va='center',fontsize=12);a.set_title('Teleportation with two correction bits',fontsize=13);a.set(xlim=(-.1,8),ylim=(-2.95,.95));a.axis('off')
b=axs[1];data=np.array([[0,.5,.5,0],[0,.5,.5,0],[.5,0,0,.5],[.5,0,0,.5]])
b.imshow(data,vmin=0,vmax=.5,cmap='Blues',aspect='equal')
b.set(xticks=range(4),xticklabels=['00','01','10','11'],yticks=range(4),yticklabels=[r'$\Psi^+$',r'$\Psi^-$',r'$\Phi^+$',r'$\Phi^-$'],xlabel='Direct computational outcome',title='Restricted Bell-state readout')
for i in range(4):
 for j in range(4):b.text(j,i,'1/2' if data[i,j] else '0',ha='center',va='center',color='white' if data[i,j] else '#334155',fontsize=12)
b.text(1.5,4.1,'Pair parity is read; the sign is hidden.\nUniform-message mutual information: 1 bit.',ha='center',va='top',fontsize=10)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
