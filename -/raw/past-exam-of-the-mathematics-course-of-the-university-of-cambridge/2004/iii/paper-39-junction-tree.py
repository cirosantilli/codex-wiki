"""Render original nine-clique junction tree; output PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

cliques=[('A','C','U','V'),('A','C','M'),('A','F','M'),('A','B','F'),('C','D','M'),('F','M','X'),('F','M','Y'),('B','P','Q'),('D','R','S')]
edges=[(0,1),(1,2),(2,3),(1,4),(2,5),(2,6),(3,7),(4,8)]
pos={0:(3,3),1:(3,2),2:(2,1),3:(.6,0),4:(5,1),5:(2,0),6:(3.4,0),7:(.6,-1),8:(5,0)}
fig,ax=plt.subplots(figsize=(9,6),dpi=120,facecolor='white')
for i,j in edges:
    x,y=pos[i];xx,yy=pos[j];ax.plot([x,xx],[y,yy],color='#365d72',lw=1.8,zorder=1)
    sep=', '.join(sorted(set(cliques[i])&set(cliques[j])))
    ax.text((x+xx)/2,(y+yy)/2,'{'+sep+'}',fontsize=10,ha='center',va='center',bbox={'facecolor':'white','edgecolor':'none','pad':1.5},zorder=2)
for i,(x,y) in pos.items():
    ax.text(x,y,f'$K_{i}$\n'+', '.join(cliques[i]),fontsize=11,ha='center',va='center',bbox={'boxstyle':'round,pad=.5','facecolor':'#edf5f8','edgecolor':'#18394b','linewidth':1.5},zorder=3)
ax.set(xlim=(-.2,5.8),ylim=(-1.55,3.65));ax.axis('off')
ax.set_title('Cousin-marriage pedigree: junction tree of maximal cliques',fontsize=13,pad=12)
ax.text(2.8,-1.45,'Edge labels are separators. Every genotype occurs in a connected subtree.',ha='center',fontsize=10)
fig.subplots_adjust(left=.025,right=.98,top=.9,bottom=.07)
fig.savefig(Path.cwd()/'paper-39-junction-tree.png',facecolor='white',transparent=False)
plt.close(fig)
