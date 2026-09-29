"""Original explanatory diagram; Python 3.14, matplotlib and numpy.
Run from the desired output directory; the PNG is written to that directory.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
from tools.chemistry_diagram import bond, atom, ring, wedge, curly, flow, finish, save, BLUE, ORANGE
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig,axs=plt.subplots(1,3,figsize=(10.2,4.0),layout='constrained')
for ax,(name,low,high,mu) in zip(axs,[('Mn(II), d⁵',[1,1,1],[1,1],'5.92'),('Fe(II), d⁶',[2,1,1],[1,1],'4.90'),('Cu(II), d⁹',[2,2,2],[2,1],'1.73')]):
    for y,occ in [(0,low),(1.5,high)]:
        for j,n in enumerate(occ):
            x=j-(len(occ)-1)/2
            ax.plot([x-.32,x+.32],[y,y],color='0.2',lw=1.6)
            for k in range(n):
                xx=x+(k-.5 if n==2 else 0)*.25
                ax.annotate('',(xx,y+.75 if k==0 else y+.13),(xx,y+.13 if k==0 else y+.75),arrowprops={'arrowstyle':'->','lw':1.6,'color':BLUE})
    ax.text(-1.7,.12,r'$t_{2g}$');ax.text(-1.2,1.6,r'$e_g$')
    ax.text(0,-.55,'μ = '+mu+' μB',ha='center')
    finish(ax,(-2,1.65),(-.9,2.6),name)
fig.suptitle('Increasing energy upward; one arrow represents one electron',fontsize=12)
save(fig,'paper-2-crystal-field.png')
