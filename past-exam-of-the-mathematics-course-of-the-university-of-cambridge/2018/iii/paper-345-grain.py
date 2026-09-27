"""Original force diagrams; save an opaque PNG to CWD."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Arc
fig,axs=plt.subplots(1,2,figsize=(9.6,4.2),dpi=100,facecolor='white')
for ax,a,title in zip(axs,[0,np.deg2rad(22)],['Horizontal bed','Upslope bed; tangent drag']):
 T=np.array([np.cos(a),np.sin(a)]);N=np.array([-np.sin(a),np.cos(a)]);C=.45*N
 ax.plot([-2*T[0],2*T[0]],[-2*T[1],2*T[1]],color='#333333',lw=3)
 ax.add_patch(Circle(C,.45,facecolor='#e8e0ce',edgecolor='#555555',lw=1.4))
 for vec,label,col,start in [(1.35*T,'drag $F_D$','#b84e3b',C),(.95*N,'normal $R$','#2b7794',C),(-.95*T,'friction $\\mu_sR$','#35724b',C),([0,-1.25],'weight $G$','#444444',C)]:
  end=C+vec;ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','lw':2,'color':col});ax.text(*(end+np.array([.08,.06])),label,fontsize=10,color=col,ha='left' if end[0]>=0 else 'right')
 if a:
  ax.plot([0,1.6],[0,0],ls=':',color='#999999');ax.add_patch(Arc((0,0),2.3,2.3,theta1=0,theta2=22,color='#777777'));ax.text(1.2,.13,'$\\alpha$',fontsize=12)
 ax.set(xlim=(-2.3,2.5),ylim=(-1.3,2.1),title=title);ax.set_aspect('equal');ax.axis('off')
fig.tight_layout();fig.savefig('paper-345-grain.png',facecolor='white',transparent=False)
