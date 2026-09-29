"""Original Hox organization schematic; Python 3.14, matplotlib. Output basename to cwd."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig,ax=plt.subplots(figsize=(12,7.5),facecolor='white');ax.set(xlim=(0,12),ylim=(0,7.5));ax.axis('off')
colors=['#2d77a8','#4ca38b','#dfad45','#c26a59']
def cluster(x,y,labels=('anterior','central','posterior'),scale=1):
 ax.plot([x-.2,x+3.0*scale],[y,y],color='0.4',lw=1.5)
 for i,(label,col) in enumerate(zip(labels,[colors[0],colors[1],colors[3]])):
  xx=x+i*1.05*scale;ax.add_patch(Rectangle((xx-.12,y-.13),.7*scale,.26,fc=col,ec='white'));ax.text(xx+.23*scale,y+.28,label,ha='center',fontsize=9)
ax.text(6,7.23,'Hox linkage, duplication and developmental regulation',ha='center',fontsize=15,weight='bold')
cluster(.8,5.95);ax.text(2.15,5.36,'Inherited cluster\n(local duplication and divergence)',ha='center',fontsize=10)
ax.add_patch(FancyArrowPatch((4.1,5.96),(5.1,5.96),arrowstyle='-|>',mutation_scale=14,lw=1.4));ax.text(4.6,6.38,'duplication',ha='center',fontsize=10)
for y in [6.47,5.45]:cluster(5.55,y,labels=('1','2','3'),scale=.75)
ax.text(9.85,6.03,'Further duplication,\nretention, loss and divergence',ha='center',fontsize=10)
ax.plot([.4,11.6],[4.78,4.78],color='0.82')
cluster(.85,3.9);ax.text(2.2,3.35,'Sequential activation / shared enhancers\ncan constrain order and proximity.',ha='center',fontsize=10)
for i in range(3):
 x=5.85+i*1.95;ax.plot([x-.38,x+.65],[3.9,3.9],color='0.45');ax.add_patch(Rectangle((x-.12,3.77),.6,.26,fc=[colors[0],colors[1],colors[3]][i],ec='white'))
ax.text(8.25,3.35,'Dispersed genes can retain local\npositional expression control.',ha='center',fontsize=10)
ax.text(2.2,4.47,'Linked regulatory system',ha='center',fontsize=12,weight='bold');ax.text(8.25,4.47,'Derived dispersed system',ha='center',fontsize=12,weight='bold')
ax.plot([.4,11.6],[2.76,2.76],color='0.82')
ax.text(2.55,2.31,'Different questions',ha='center',fontsize=12,weight='bold')
for y,left,right in [(1.85,'Spatial collinearity','Where are the anterior expression limits?'),(1.36,'Temporal collinearity','In what order do genes turn on?'),(.87,'Regulatory architecture','Which enhancers can contact each gene?')]:
 ax.text(.7,y,left,va='center',fontsize=11);ax.text(5.55,y,right,va='center',fontsize=11)
ax.text(6,.18,'Schematic representatives only: coloured boxes are not a complete gene inventory or a species phylogeny.\nA cluster rearrangement can affect timing, enhancer access and spatial expression differently.',ha='center',fontsize=10)
fig.tight_layout();fig.savefig('paper-2-hox-organization.png',dpi=165,facecolor='white',bbox_inches='tight');plt.close(fig)
