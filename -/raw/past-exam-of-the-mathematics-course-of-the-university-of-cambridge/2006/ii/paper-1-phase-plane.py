"""Original phase portrait; Python 3.14, root NumPy/Matplotlib dependencies."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(-0.6,3.6,500);X,Y=np.meshgrid(x,x);H=X*Y*(X+Y-3)
fig,ax=plt.subplots(figsize=(6.5,6.1),facecolor='white')
cs=ax.contour(X,Y,H,levels=[-0.9,-0.65,-0.3,0.5,1.5,4],colors='#4682a9',linewidths=1)
ax.clabel(cs,fontsize=8,fmt='%g');ax.contour(X,Y,H,levels=[0],colors='#333333',linewidths=1.8)
q=np.linspace(-0.45,3.45,19);Q,R=np.meshgrid(q,q);U=Q*(Q+2*R-3);V=R*(3-2*Q-R)
length=np.hypot(U,V);length=np.where(length>1e-9,length,1)
ax.quiver(Q,R,U/length,V/length,color='#888888',alpha=.6,scale=38,width=.0025)
for px,py,label in [(0,0,'saddle'),(3,0,'saddle'),(0,3,'saddle'),(1,1,'centre')]:
 ax.plot(px,py,'o',color='#b13f32',ms=5);ax.annotate(label,(px,py),xytext=(6,7),textcoords='offset points',fontsize=9)
ax.set(xlim=(-.6,3.6),ylim=(-.6,3.6),xlabel='$x$',ylabel='$y$',title='$H=xy(x+y-3)$: level curves and flow')
ax.set_aspect('equal');fig.tight_layout();fig.savefig('paper-1-phase-plane.png',dpi=150,facecolor='white')
