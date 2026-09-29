"""Original linear-mode snapshots, equal masses; output only into cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(1,2,figsize=(9,5.7),dpi=150,facecolor='white')
A=.2
for ax,sign,name in zip(axes,[1,-1],['Slower mode','Faster mode']):
 ratio=1+sign*np.sqrt(2)
 xs=[0,A,A*ratio];ys=[0,-1,-2]
 ax.plot([0,0],[.1,-2.18],ls=':',color='#999999')
 ax.plot(xs,ys,color='#30343b',lw=2)
 ax.scatter(xs[1:],ys[1:],s=190,color=['#19678b','#ba4938'],edgecolor='white',zorder=5)
 ax.scatter([0],[0],marker='s',s=50,color='black')
 for yy,xx in zip(ys[1:],xs[1:]):
  ax.annotate('',xy=(xx,yy+.18),xytext=(0,yy+.18),arrowprops=dict(arrowstyle='->',lw=1.7,color='#007c83'))
 ax.text(A+.06,-1,'$m$',fontsize=13,va='center')
 ax.text(A*ratio+.06,-2,'$m$',fontsize=13,va='center')
 ax.text(-.65,-2.52,r'$x_1=A$'+'\n'+r'$x_2=(1'+('+' if sign==1 else '-')+r'\sqrt{2})A$',fontsize=13,va='center')
 ax.set_title(name+'\n'+r'$\omega=\sqrt{(2'+('-' if sign==1 else '+')+r'\sqrt{2})g/l}$',fontsize=13,pad=14)
 ax.set(xlim=(-.72,.78),ylim=(-2.8,.2))
 ax.set_aspect('equal');ax.axis('off')
fig.suptitle('Equal-mass double-pendulum modes',fontsize=16,y=.98)
fig.text(.5,.025,'Horizontal offsets enlarged; arrows show displacement signs and relative amplitudes.',ha='center',fontsize=11)
fig.subplots_adjust(top=.78,bottom=.12,wspace=.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white')
