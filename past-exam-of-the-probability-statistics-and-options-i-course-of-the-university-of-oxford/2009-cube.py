"""Python 3.14, root NumPy/Matplotlib versions. One original image, output CWD."""
import matplotlib.pyplot as plt
pos={'000':(-2,-2),'001':(2,-2),'011':(2,2),'010':(-2,2),'100':(-.9,-.9),'101':(.9,-.9),'111':(.9,.9),'110':(-.9,.9)}
colors=['#2c875d','#cf6c23','#327eb1']
fig,ax=plt.subplots(figsize=(5.5,5.2),layout='constrained',facecolor='white')
for a in pos:
 for b in pos:
  diff=[i for i in range(3)if a[i]!=b[i]]
  if a<b and len(diff)==1:ax.plot([pos[a][0],pos[b][0]],[pos[a][1],pos[b][1]],color=colors[diff[0]],lw=2.3,zorder=1)
for a,(x,y)in pos.items():
 ax.scatter([x],[y],s=80,color='white',edgecolor='black',zorder=2)
 factor=1.11 if abs(x)>1 else .76
 ax.text(x*factor,y*factor,a,ha='center',va='center',fontsize=11)
ax.set_aspect('equal');ax.set(xlim=(-2.5,2.5),ylim=(-2.5,2.5),title='Planar Q₃: one edge colour per coordinate');ax.axis('off')
fig.savefig('2009-cube.png',dpi=155,facecolor='white')
