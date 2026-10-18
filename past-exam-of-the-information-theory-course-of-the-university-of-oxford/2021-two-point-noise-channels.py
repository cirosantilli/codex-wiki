"""Original graphs for Y=X+Z with independent uniform Z in {0,d}.
Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7. Output is relative to CWD.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1,3,figsize=(9.2,3.7),dpi=120,facecolor='white')
for ax,d,capacity in zip(axes,[1,2,3],['1 bit/use',r'$\log_2(1+\sqrt{2})\approx1.272$ bits/use',r'$\log_2 3\approx1.585$ bits/use']):
    ax.set_facecolor('white'); outputs=sorted({x+z for x in range(3) for z in (0,d)})
    yin=np.linspace(.82,.18,3);yout=np.linspace(.92,.08,len(outputs));outpos=dict(zip(outputs,yout))
    for x in range(3):
        for z,color in [(0,'#23816b'),(d,'#bd6b26')]:
            ax.plot([.13,.83],[yin[x],outpos[x+z]],color=color,lw=1.7,zorder=1)
    ax.scatter([.13]*3,yin,s=155,facecolor='#eff5f8',edgecolor='#31546a',zorder=3)
    for x,y in enumerate(yin):ax.text(.13,y,str(x),ha='center',va='center',fontsize=10,zorder=4)
    for y,v in outpos.items():
        collision=sum(y in (x,x+d) for x in range(3))>1
        ax.scatter([.83],[v],s=155,facecolor='#ffe2b9' if collision else 'white',edgecolor='#31546a',zorder=3)
        ax.text(.83,v,str(y),ha='center',va='center',fontsize=10,zorder=4)
    ax.text(.13,1.03,'input',ha='center',fontsize=10);ax.text(.83,1.03,'output',ha='center',fontsize=10)
    ax.set_title(f'Noise {{0, {d}}}: {len(outputs)} outputs',fontsize=11,pad=24)
    ax.text(.5,-.05,capacity,ha='center',fontsize=10)
    ax.set_xlim(-.03,1);ax.set_ylim(-.1,1.1);ax.axis('off')
fig.text(.5,.025,'Each edge has probability ½. Shaded outputs can arise from two different inputs.',ha='center',fontsize=10)
fig.subplots_adjust(left=.02,right=.99,bottom=.15,top=.77,wspace=.22)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
plt.close(fig)
