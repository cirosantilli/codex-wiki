"""Original gate decomposition diagrams; Python 3.14/matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.size':12})
fig,axs=plt.subplots(3,1,figsize=(10.5,8.4),layout='constrained',facecolor='white')
def setup(ax,n,title):
 for i in range(n):
  y=-i;ax.plot([.2,7.4],[y,y],color='#126782',lw=1.8);ax.text(-.05,y,f'q{i+1}',ha='right',va='center')
 ax.set(xlim=(-.6,8.2),ylim=(-n+.25,.8));ax.axis('off');ax.set_title(title,loc='left')
def gate(ax,x,controls,target):
 ys=[-q for q in controls]+[-target];ax.plot([x,x],[min(ys),max(ys)],color='black',lw=1.6)
 for c in controls:ax.plot(x,-c,'ko',ms=7)
 ax.add_patch(Circle((x,-target),.13,facecolor='white',edgecolor='black',lw=1.7,zorder=3));ax.plot([x-.10,x+.10],[-target,-target],color='black',lw=1.5,zorder=4);ax.plot([x,x],[-target-.10,-target+.10],color='black',lw=1.5,zorder=4)
setup(axs[0],2,'SWAP from three CNOTs')
for x,c,t in [(1.4,[0],1),(3.7,[1],0),(6,[0],1)]:gate(axs[0],x,c,t)
axs[0].text(7.65,-.5,'SWAP',va='center',fontsize=11)
setup(axs[1],3,'Fredkin: control all three gates of the SWAP decomposition')
for x,c,t in [(1.4,[0,1],2),(3.7,[0,2],1),(6,[0,1],2)]:gate(axs[1],x,c,t)
setup(axs[2],3,'Fredkin with one Toffoli and two CNOTs')
for x,c,t in [(1.4,[2],1),(3.7,[0,1],2),(6,[2],1)]:gate(axs[2],x,c,t)
axs[2].text(3.7,-2.6,'Time runs left to right; filled dots require control = 1.',ha='center',fontsize=11)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
