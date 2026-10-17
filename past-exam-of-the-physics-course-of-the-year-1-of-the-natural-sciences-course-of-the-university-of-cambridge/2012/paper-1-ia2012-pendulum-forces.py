import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
fig,ax=plt.subplots(figsize=(6.4,5.2),layout='constrained')
th=np.deg2rad(30);bob=np.array([np.sin(th),-np.cos(th)])
ax.plot([0,bob[0]],[0,bob[1]],color='#555',lw=3)
ax.plot([0,0],[0,-1.12],color='#aaa',ls='--')
ax.scatter([0,bob[0]],[0,bob[1]],s=[50,190],color=['black','#555'],zorder=5)
ax.add_patch(Arc((0,0),.55,.55,theta1=270,theta2=300,color='black'))
ax.text(.08,-.37,r'$\theta$',fontsize=14)
ax.text(.31,-.37,r'$L$',fontsize=14)
def arrow(vec,color,label,offset):
 tip=bob+vec
 ax.annotate('',xy=tip,xytext=bob,arrowprops=dict(arrowstyle='->',color=color,lw=2.4))
 ax.text(*(tip+np.array(offset)),label,color=color,fontsize=12)
arrow(-.6*bob,'#c94a39',r'rod force $F_r$',(-.23,.06))
arrow(np.array([0,-.55]),'#2475aa',r'$Mg$',(.04,-.02))
tan=np.array([np.cos(th),np.sin(th)])
arrow(-.48*tan,'#468b50',r'$-Mg\sin\theta$ (tangential)',(-.34,-.16))
ax.text(-.56,.05,'pivot',fontsize=11)
ax.text(-.65,-1.58,'Rod force is radial; only gravity supplies restoring torque.',fontsize=10)
ax.set(xlim=(-.72,1.04),ylim=(-1.72,.15),aspect='equal');ax.axis('off')
fig.savefig('paper-1-ia2012-pendulum-forces.png',dpi=160,facecolor='white')
