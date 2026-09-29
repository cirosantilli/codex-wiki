"""Original diagram; tested with Python 3.14, NumPy and Matplotlib.
Write the matching PNG basename to the caller's working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7.1,6.4),dpi=145,facecolor='white')
E=[np.array([1.,0]),np.array([-.5,np.sqrt(3)/2]),np.array([-.5,-np.sqrt(3)/2])]
angles=np.deg2rad(np.linspace(120,180,60));arc=2.45*np.column_stack((np.cos(angles),np.sin(angles)))
ax.fill(np.r_[0,arc[:,0],0],np.r_[0,arc[:,1],0],color='#dcebe2',zorder=0)
for ang in [120,180]:
 v=2.45*np.array([np.cos(np.deg2rad(ang)),np.sin(np.deg2rad(ang))]);ax.plot([0,v[0]],[0,v[1]],'--',color='#298459',lw=1.5)
for vec,label in [(E[1]-E[2],r'$\alpha_1=\epsilon_2-\epsilon_3$'),(E[2]-E[0],r'$\alpha_2=\epsilon_3-\epsilon_1$'),(E[1]-E[0],r'$\alpha_1+\alpha_2$')]:
 for sign in [1,-1]:
  v=sign*vec;color='#a34238' if sign==1 else '#888888'
  ax.annotate('',xy=v,xytext=(0,0),arrowprops=dict(arrowstyle='-|>',color=color,lw=1.8,mutation_scale=14))
  text=label if sign==1 else {r'$\alpha_1=\epsilon_2-\epsilon_3$':r'$-\alpha_1$',r'$\alpha_2=\epsilon_3-\epsilon_1$':r'$-\alpha_2$',r'$\alpha_1+\alpha_2$':r'$-\alpha_1-\alpha_2$'}[label]
  delta=np.array([0,.13 if v[1]>=0 else -.13])
  ax.text(*(v+delta),text,ha='center',va='bottom' if v[1]>=0 else 'top',fontsize=11,color=color)
H=-np.sqrt(2)*E[0]+E[1]+(np.sqrt(2)-1)*E[2];H=H/np.linalg.norm(H)*1.15
ax.annotate('',xy=H,xytext=(0,0),arrowprops=dict(arrowstyle='-|>',color='#263f70',lw=2.1))
ax.text(H[0]-.04,H[1]+.1,r'$H_0$',color='#263f70',fontsize=13,ha='right')
ax.text(-1.1,1.36,r'$\omega_1=\epsilon_2$',color='#298459',fontsize=12,rotation=-60)
ax.text(-2.27,-.16,r'$\omega_2=-\epsilon_1$',color='#298459',fontsize=12,ha='center')
ax.text(-2.02,1.25,'Dominant chamber',color='#236444',fontsize=10,ha='center')
ax.scatter(0,0,color='#333333',s=15)
ax.set_aspect('equal');ax.axis('off');ax.set_xlim(-3.05,2.1);ax.set_ylim(-2.15,2.65)
ax.set_title('A2 chamber for the specified nonstandard ordering',fontsize=14,pad=14)
fig.tight_layout();fig.savefig('paper-1-weyl-chamber.png',facecolor='white',transparent=False);plt.close(fig)
