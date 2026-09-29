"""Original CP1 collision illustration. Python 3.14; numpy 2.3.5; matplotlib 3.10.7.
Writes only the matching opaque PNG in the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
fig,axs=plt.subplots(1,2,figsize=(10,3.8),layout='constrained',facecolor='white')
a=axs[0]
for x,title,v1,v2 in [(0,'Falling',-1,-1),(2,'Floor rebound',-1,1),(4,'After mutual impact',2,0)]:
 a.plot([x-.65,x+.65],[0,0],color='black',lw=1.5)
 a.add_patch(Circle((x,1.55),.21,facecolor='#e29538',edgecolor='black'))
 a.add_patch(Circle((x,.48),.32,facecolor='#5b9bd5',edgecolor='black'))
 for y,v in [(1.55,v1),(.48,v2)]:
  if v:a.annotate('',xy=(x+.43,y+.34*v),xytext=(x+.43,y),arrowprops=dict(arrowstyle='->',color='#383838',lw=1.6))
 a.text(x,-.18,title,ha='center',va='top',fontsize=9)
 a.text(x,2.35,r'$(-u,-u)$' if x==0 else (r'$(-u,+u)$' if x==2 else r'$(2u,0)$'),ha='center')
a.set(xlim=(-.8,4.8),ylim=(-.55,2.8),aspect='equal');a.axis('off');a.set_title(r'Optimal mass ratio $m_1/m_2=1/3$')
r=np.linspace(0,3,601);f=r*(3-r)**2/(1+r)**3
axs[1].plot(r,f,lw=2,color='#317496');axs[1].plot([1/3],[1],'o',color='#bd6022');axs[1].annotate('Complete transfer',xy=(1/3,1),xytext=(.7,.9),arrowprops=dict(arrowstyle='->'))
axs[1].set(xlabel=r'Mass ratio $r=m_1/m_2$',ylabel='Upper-ball energy fraction',xlim=(0,3),ylim=(0,1.08));axs[1].grid(alpha=.25)
fig.savefig('2013-resit-double-ball-bounce.png',dpi=150,facecolor='white',metadata={'Software':'Matplotlib'})
