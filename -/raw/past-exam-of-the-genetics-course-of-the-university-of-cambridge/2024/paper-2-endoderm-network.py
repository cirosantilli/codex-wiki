"""Original explanatory network; Python 3.14, matplotlib. Output basename goes to cwd."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig,ax=plt.subplots(figsize=(12,7),facecolor='white');ax.set(xlim=(0,12),ylim=(0,7));ax.axis('off')
def box(x,y,w,h,text,color='#e7f0fb',edge='#245d8e'):
 ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.10',fc=color,ec=edge,lw=1.3));ax.text(x,y,text,ha='center',va='center')
def arrow(a,b,color='#245d8e',rad=0,style='-'):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=13,lw=1.5,color=color,connectionstyle=f'arc3,rad={rad}',linestyle=style))
ax.text(6,6.75,'An intestinal fate requires converging inputs and later differentiation',ha='center',fontsize=15,weight='bold')
box(1.65,5.5,2.7,.8,'P2 contact\nMOM-2 / Wnt',color='#fff1df',edge='#a86b24')
box(5.2,5.5,3.3,.95,'E: high SYS-1 / POP-1\nratio supports activation',color='#fff1df',edge='#a86b24')
arrow((3.1,5.5),(3.45,5.5),'#a86b24')
box(1.65,3.5,2.7,.8,'Maternal SKN-1')
box(5.2,3.5,2.65,.8,'MED-1 and MED-2')
arrow((3.1,3.5),(3.75,3.5))
box(8.9,3.5,2.6,1.05,'END-3 and END-1\n(endoderm specification)')
arrow((6.65,3.5),(7.45,3.5));arrow((6.1,4.93),(8.25,4.13),'#a86b24')
arrow((2.4,3.98),(7.5,4.02),rad=-.24)
ax.text(5.0,4.47,'parallel input',ha='center',fontsize=10,color='#245d8e')
box(5.2,1.6,2.65,.8,'ELT-7 and ELT-2',color='#edf6e7',edge='#4a7832')
box(9.0,1.6,2.6,.8,'Intestinal targets\nand differentiation',color='#edf6e7',edge='#4a7832')
arrow((8.8,2.86),(6.3,2.08),'#4a7832');arrow((6.65,1.6),(7.6,1.6),'#4a7832')
arrow((4.5,1.14),(5.8,1.14),'#4a7832',rad=.65);ax.text(5.2,.58,'stabilizing feedback',ha='center',fontsize=10,color='#4a7832')
box(1.65,1.6,2.7,.8,'PAL-1 / other inputs',color='#f3eef8',edge='#7a5b92')
arrow((2.85,2.05),(7.6,3.05),'#7a5b92',style='--')
ax.text(1.65,4.68,'Induction changes the\nEMS daughter-cell decision',ha='center',fontsize=10,color='#80521b')
ax.text(9.1,5.7,'MS instead has\nrepressive POP-1 activity',ha='center',fontsize=11,color='#7c3d36')
ax.text(6,.07,'Arrows summarize functional inputs; they do not assert direct binding for every connection.\nThe gut-1 requirement is unknown: test signal production, response, specification and differentiation separately.',ha='center',va='bottom',fontsize=10)
fig.tight_layout();fig.savefig('paper-2-endoderm-network.png',dpi=165,facecolor='white',bbox_inches='tight');plt.close(fig)
