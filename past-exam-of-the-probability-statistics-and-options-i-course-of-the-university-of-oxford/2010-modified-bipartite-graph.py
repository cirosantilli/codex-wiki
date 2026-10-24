"""Original planar embedding. Python 3.14; dependencies in root pyproject.toml.
Writes PNG into the current working directory.
"""
import matplotlib.pyplot as plt
pos={'x1':(-2,0),'x2':(2,0),'y2':(0,-2),'y1':(0,-1),'y5':(0,0),'y3':(0,1),'y4':(0,2)}
col={'x1':'#3b8ac4','x2':'#3b8ac4','y1':'#f4a340','y3':'#f4a340','y4':'#f4a340','y2':'#67ba78','y5':'#67ba78'}
fig,ax=plt.subplots(figsize=(5.8,5.1),layout='constrained',facecolor='white')
for x in ['x1','x2']:
 for y in ['y1','y2','y3','y4','y5']:
  ax.plot([pos[x][0],pos[y][0]],[pos[x][1],pos[y][1]],color='#555555',lw=1.6,zorder=1)
for v in ['y2','y5']:
 ax.plot([0,0],[pos['y1'][1],pos[v][1]],color='#ad3946',lw=3,zorder=2)
for v,(x,y) in pos.items():
 ax.scatter([x],[y],s=550,color=col[v],edgecolor='black',linewidth=1,zorder=3)
 ax.text(x,y,v[0]+'$_'+v[1]+'$',ha='center',va='center',fontsize=12,zorder=4)
ax.set(xlim=(-2.5,2.5),ylim=(-2.4,2.4),title='A planar embedding with three vertex colours')
ax.set_aspect('equal');ax.axis('off');fig.savefig('2010-modified-bipartite-graph.png',dpi=155,facecolor='white')
