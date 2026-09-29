"""Original pedagogical mode diagram; write the PNG in the working directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

fig, ax = plt.subplots(figsize=(10.5, 6.1), dpi=120)
fig.patch.set_facecolor('white'); ax.set_facecolor('white')
ax.set(xlim=(-.7, 10.3), ylim=(-2.75, 3.05)); ax.axis('off')
blue='#176a8a'; gold='#ad6818'; ink='#222b35'
def box(x,y,text,w=1.25,h=.58):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=.045',facecolor='#eef2f5',edgecolor=ink,lw=1.4,zorder=3))
    ax.text(x,y,text,ha='center',va='center',fontsize=11,color=ink,zorder=4)
def arrow(start,end,text='',offset=(0,.15),color=blue):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=13,lw=1.7,color=color,zorder=1))
    if text:ax.text((start[0]+end[0])/2+offset[0],(start[1]+end[1])/2+offset[1],text,ha='center',va='center',fontsize=11,color=color)
box(.3,0,'BBO',1.1,.75);box(2.5,1.15,'PBS a');box(2.5,-1.15,'50:50 BS');box(4.7,1.15,r'$\lambda/2$',.9);box(6.6,0,'Final PBS',1.35,.7)
arrow((-.4,0),(-.25,0),color=gold);ax.text(-.35,.45,'UV',ha='center',fontsize=11,color=gold)
arrow((.85,.2),(1.84,1.1),'a');arrow((.85,-.2),(1.84,-1.1),'b',offset=(0,-.15))
arrow((2.5,1.5),(3.1,2.2),r'$H_a$',offset=(-.23,.1));box(3.35,2.45,'T',.55,.4)
arrow((3.16,1.15),(4.2,1.15),r'$c:V$');arrow((5.2,1.1),(5.96,.25),r"$c'$",offset=(.12,.1))
arrow((3.17,-1.1),(5.98,-.2),'d',offset=(0,-.13));arrow((2.5,-1.5),(4.0,-2.05));box(4.4,-2.2,r'$D_3$',.7,.4)
arrow((7.31,.18),(8.8,1.1));box(9.15,1.3,r'$D_1$',.7,.4);arrow((7.31,-.18),(8.8,-1.1));box(9.15,-1.3,r'$D_2$',.7,.4)
ax.text(6.25,2.6,'Fourfold coincidence: T + D₁ + D₂ + D₃',ha='center',fontsize=13,fontweight='bold',color=ink)
ax.text(6.2,1.95,r'$V_c\ \to\ (H_{c\prime}+V_{c\prime})/\sqrt{2}$',ha='center',fontsize=12,color=blue)
ax.text(7.1,-2.15,r'$HH\to H_1H_2$'+'\n'+r'$VV\to V_1V_2$',ha='center',va='center',fontsize=12,color=ink)
fig.suptitle('Photonic GHZ preparation: ideal mode routing',fontsize=16,y=.97,color=ink)
fig.subplots_adjust(left=.035,right=.985,bottom=.05,top=.9)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',metadata={'Software':'codex-wiki original figure'})
plt.close(fig)
