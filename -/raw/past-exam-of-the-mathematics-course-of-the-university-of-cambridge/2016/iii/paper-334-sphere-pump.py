import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
fig,axes=plt.subplots(1,2,figsize=(8,3.6),dpi=100)
q=np.linspace(0,2*np.pi,700);phase=np.pi/3;x=np.cos(q);y=np.cos(q+phase)
axes[0].plot(x,y,lw=2,color='tab:blue')
for t in [.2,2.3,4.5]:
 a=np.array([np.cos(t),np.cos(t+phase)]);b=np.array([np.cos(t+.16),np.cos(t+.16+phase)])
 axes[0].annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':'tab:blue','lw':1.5})
axes[0].set(xlabel=r'$(x_1-\overline{x_1})/\delta$',ylabel=r'$(x_2-\overline{x_2})/\delta$',title=r'Joint stroke: $\phi=\pi/3$');axes[0].set_aspect('equal');axes[0].grid(alpha=.15)
ph=np.linspace(0,2*np.pi,400);axes[1].plot(ph/np.pi,np.sin(ph),lw=2,color='tab:orange');axes[1].axhline(0,color='gray',lw=.7)
axes[1].scatter([0,1,2],[0,0,0],color='black',s=17)
axes[1].set(xlabel=r'Phase lag $\phi/\pi$',ylabel='Leading mean total force / amplitude',title=r'Force changes sign with phase',xlim=(0,2));axes[1].grid(alpha=.15)
fig.tight_layout();fig.savefig('paper-334-sphere-pump.png',facecolor='white',transparent=False)
