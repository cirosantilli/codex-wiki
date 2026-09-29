"""Draw labelled D-type diagrams. Python 3.14, Matplotlib 3.10."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2, figsize=(10, 5.2), facecolor='white')
def draw(ax, title, points, edges):
 ax.set_title(title, fontsize=14, pad=15)
 for a,b in edges:
  x,y=points[a],points[b]
  if a=='dots':x=(x[0]+.17,x[1])
  if b=='dots':y=(y[0]-.17,y[1])
  ax.plot([x[0],y[0]],[x[1],y[1]],color='#374151',lw=2,zorder=1)
 for text,(x,y) in points.items():
  if text=='dots':ax.text(x,y,r'$\cdots$',ha='center',va='center',fontsize=22)
  else:
   ax.scatter(x,y,s=125,color='#166534',zorder=2)
   ax.annotate(text,(x,y),xytext=(0,-22),textcoords='offset points',ha='center',fontsize=14)
 ax.set_xlim(-.5,5.1);ax.set_ylim(-1.15,1.45);ax.axis('off')
p={r'$\alpha_1$':(0,0),r'$\alpha_2$':(1,0),'dots':(2,0),r'$\alpha_{n-2}$':(3,0),r'$\alpha_{n-1}$':(4.5,.8),r'$\alpha_n$':(4.5,-.8)}
draw(axs[0,0],r'$D_n$ ($n\geq5$)',p,[(r'$\alpha_1$',r'$\alpha_2$'),(r'$\alpha_2$','dots'),('dots',r'$\alpha_{n-2}$'),(r'$\alpha_{n-2}$',r'$\alpha_{n-1}$'),(r'$\alpha_{n-2}$',r'$\alpha_n$')])
p={r'$\alpha_1$':(.7,0),r'$\alpha_2$':(2.2,0),r'$\alpha_3$':(3.7,.85),r'$\alpha_4$':(3.7,-.85)}
draw(axs[0,1],r'$D_4$',p,[(r'$\alpha_1$',r'$\alpha_2$'),(r'$\alpha_2$',r'$\alpha_3$'),(r'$\alpha_2$',r'$\alpha_4$')])
p={r'$\alpha_2$':(.5,0),r'$\alpha_1$':(2.3,0),r'$\alpha_3$':(4.1,0)}
draw(axs[1,0],r'$D_3\cong A_3$',p,[(r'$\alpha_2$',r'$\alpha_1$'),(r'$\alpha_1$',r'$\alpha_3$')])
p={r'$\alpha_1$':(1.1,0),r'$\alpha_2$':(3.5,0)}
draw(axs[1,1],r'$D_2\cong A_1\times A_1$',p,[])
fig.tight_layout(pad=2)
fig.savefig(Path.cwd()/f'{Path(__file__).stem}.png',dpi=160,facecolor='white',transparent=False)
plt.close(fig)
