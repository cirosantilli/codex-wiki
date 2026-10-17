"""Original cubic sketch; write the PNG to the current working directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(7,4.4),facecolor='white')
x=np.linspace(-1.8,3.8,700);ax.plot(x,x**3-3*x*x+4,lw=2,color='#247ba0')
for x,y,label,offset in [(-1,0,'Zero (-1, 0)',(-.45,1.1)),(0,4,'Local maximum (0, 4)',(-.6,1.1)),(1,2,'Inflection (1, 2)',(.25,1.1)),(2,0,'Double zero / local minimum (2, 0)',(-.6,-1.5))]:
 ax.scatter([x],[y],color='#ba3434',zorder=4);ax.annotate(label,(x,y),(x+offset[0],y+offset[1]),fontsize=9,arrowprops={'arrowstyle':'-','color':'gray'})
ax.axhline(0,color='gray',lw=.7);ax.axvline(0,color='gray',lw=.7);ax.grid(alpha=.2)
ax.set(xlim=(-1.8,3.8),ylim=(-5,10),xlabel='x',ylabel='y',title=r'$y=x^3-3x^2+4=(x-2)^2(x+1)$')
fig.tight_layout();fig.savefig(Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white');plt.close(fig)
