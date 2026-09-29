"""Original diagram; tested with Python 3.14, NumPy and Matplotlib.
Write the matching PNG basename to the caller's working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6.8,5.7),dpi=145,facecolor='white')
roots=[((1,0),r'$\alpha$'),((-1,1),r'$\beta$'),((0,1),r'$\alpha+\beta$'),((1,1),r'$2\alpha+\beta$')]
for v,label in roots:
 for sign in [1,-1]:
  p=np.array(v)*sign;color='#b03933' if sign==1 and v in [(1,0),(-1,1)] else ('#245f9a' if sign==1 else '#888888')
  ax.annotate('',xy=p,xytext=(0,0),arrowprops=dict(arrowstyle='-|>',lw=1.8,color=color,mutation_scale=16))
  text=label if sign==1 else '$-('+label[1:-1]+')$'
  dx=.12 if p[0]>0 else (-.12 if p[0]<0 else 0);dy=.12 if p[1]>0 else (-.12 if p[1]<0 else 0)
  ax.text(p[0]+dx,p[1]+dy,text,ha='left' if p[0]>0 else ('right' if p[0]<0 else 'center'),va='bottom' if p[1]>0 else ('top' if p[1]<0 else 'center'),fontsize=13,color=color)
ax.scatter(0,0,s=16,color='#222222');ax.axhline(0,color='#dddddd',lw=.7,zorder=-1);ax.axvline(0,color='#dddddd',lw=.7,zorder=-1)
ax.set_aspect('equal');ax.set_xlim(-2,2);ax.set_ylim(-1.6,1.6);ax.axis('off')
ax.set_title('B2: all eight roots; red arrows are simple roots',fontsize=14,pad=15)
fig.tight_layout();fig.savefig('paper-1-b2-roots.png',facecolor='white',transparent=False);plt.close(fig)
