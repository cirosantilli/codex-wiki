"""Original general-m exact phase-estimation circuit, Python 3.14/Matplotlib 3.10.7.
Writes only its PNG basename in cwd; preserves caller MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig,ax=plt.subplots(figsize=(9.4,4.2),dpi=100,facecolor='white')
rows=[(3.1,r'$j=0$',r'$x_0$'),(2.3,r'$j=1$',r'$x_1$'),(.8,r'$j=m-1$',r'$x_{m-1}$')]
for y,label,out in rows:
    ax.plot([.6,8.9],[y,y],color='black',lw=1.2,zorder=1)
    ax.text(.06,y,r'$|0\rangle$',va='center',fontsize=12)
    ax.text(.7,y+.21,label,fontsize=10)
    ax.add_patch(Rectangle((1.15,y-.20),.48,.4,facecolor='#e4f0f5',edgecolor='black',zorder=3))
    ax.text(1.39,y,'H',ha='center',va='center',fontsize=12,zorder=4)
    ax.add_patch(Rectangle((8.05,y-.20),.48,.4,facecolor='white',edgecolor='black',zorder=3))
    ax.text(8.29,y,r'$M_Z$',ha='center',va='center',fontsize=11,zorder=4)
    ax.text(8.7,y+.11,out,fontsize=11)
ax.text(1.4,1.5,r'$\vdots$',ha='center',fontsize=18)
ax.text(7.1,1.5,r'$\vdots$',ha='center',fontsize=18)
target=-.1
ax.plot([.6,8.9],[target,target],color='black',lw=1.2)
ax.text(.05,target,r'$|\psi\rangle$',va='center',fontsize=12)
ax.text(8.6,target+.16,r'$|\psi\rangle$',fontsize=12)
for x,y,label,width in [(2.35,3.1,r'$U$',.56),(3.9,2.3,r'$U^2$',.68),(5.65,.8,r'$U^{2^{m-1}}$',1.05)]:
    ax.plot([x,x],[target,y],color='black',lw=1.2,zorder=1)
    ax.scatter(x,y,s=33,color='black',zorder=3)
    ax.add_patch(Rectangle((x-width/2,target-.22),width,.44,facecolor='#f5edda',edgecolor='black',zorder=3))
    ax.text(x,target,label,ha='center',va='center',fontsize=11,zorder=4)
ax.text(4.8,1.5,r'$\cdots$',fontsize=17)
ax.add_patch(Rectangle((6.55,.44),1.06,3.03,facecolor='#e4efe5',edgecolor='black',zorder=3))
ax.text(7.08,2,r'$\mathrm{QFT}^{-1}_{2^m}$',ha='center',va='center',rotation=90,fontsize=14,zorder=4)
ax.set(xlim=(-.1,9.3),ylim=(-.65,3.8));ax.axis('off')
fig.suptitle('Exact phase estimation: one control per binary digit',fontsize=14)
fig.text(.5,.06,r'Bit convention: $k=\sum_{j=0}^{m-1}2^j k_j$,  $x=\sum_{j=0}^{m-1}2^j x_j$; omitted wires follow the same pattern.',ha='center',fontsize=11)
fig.subplots_adjust(left=.03,right=.99,bottom=.17,top=.88)
fig.savefig(Path('paper-67-phase-estimation-circuit.png'),facecolor='white',transparent=False)
plt.close(fig)
