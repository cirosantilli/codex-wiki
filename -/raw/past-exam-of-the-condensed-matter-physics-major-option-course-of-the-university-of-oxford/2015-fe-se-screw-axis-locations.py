from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,ax=plt.subplots(figsize=(8.7,7.3),layout="constrained")
for value in [.25,.75]:
 ax.axhline(value,color="#174c75",lw=2,label='[100] screws' if value==.25 else None)
 ax.axvline(value,color="#44834b",lw=2,label='[010] screws' if value==.25 else None)
x=np.linspace(0,1,500)
for offset in [-.5,.5]:
 y=x-offset;mask=(y>=0)&(y<=1);ax.plot(x[mask],y[mask],'--',color='#b35b15',lw=1.8,label='[110] translated screws' if offset==-.5 else None)
for offset in [.5,1.5]:
 y=offset-x;mask=(y>=0)&(y<=1);ax.plot(x[mask],y[mask],':',color='#7b4280',lw=2,label='[1 -1 0] translated screws' if offset==.5 else None)
ax.add_patch(Rectangle((0,0),1,1,fill=False,lw=1.5));ax.scatter([0,.5,1,0,1],[0,.5,1,1,0],color='black',s=28,zorder=4)
ax.set(xlim=(-.06,1.06),ylim=(-.06,1.06),xlabel='Fractional x',ylabel='Fractional y',title='All shown lines repeat at z = 0 and z = 1/2')
ax.set_aspect('equal');ax.set_xticks([0,.25,.5,.75,1]);ax.set_yticks([0,.25,.5,.75,1]);ax.legend(loc='upper center',bbox_to_anchor=(.5,-.1),ncol=2,fontsize=9,frameon=False)
fig.suptitle('FeSe screw-axis lines: principal and translated diagonal families',fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,transparent=False)
