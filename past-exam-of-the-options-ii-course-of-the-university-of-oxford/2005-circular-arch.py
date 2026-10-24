"""Original arch diagram. Python3.14.4, NumPy2.3.5, Matplotlib3.10.7; output CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
radius=1.4
x=np.linspace(0,2,600);y=np.sqrt(radius**2-(x-1)**2)-np.sqrt(radius**2-1)
fig,ax=plt.subplots(figsize=(7,3.7),facecolor='white',layout='constrained')
ax.set_facecolor('white');ax.fill_between(x,0,y,color='#dbeafe')
ax.plot(x,y,color='#2563eb',lw=2.5);ax.plot([0,2],[0,0],color='#374151',lw=1.3)
ax.scatter([0,2],[0,0],c='#111827',zorder=4)
ax.text(0,-.085,'0',ha='center');ax.text(2,-.085,r'$2a$',ha='center')
ax.annotate(r'$y=\sqrt{\lambda^2-(x-a)^2}-\sqrt{\lambda^2-a^2}$',(.98,.40),xytext=(1,.78),ha='center',arrowprops={'arrowstyle':'->','color':'#475569'})
ax.text(1,-.27,r'$l=2\lambda\arcsin(a/\lambda),\quad 2a<l<\pi a$',ha='center')
ax.set(xlim=(-.15,2.15),ylim=(-.35,.95),xlabel=r'$x$',ylabel=r'$y$')
ax.set_title('A smooth graph arc with fixed length and endpoints')
ax.spines[['top','right']].set_visible(False);ax.set_xticks([]);ax.set_yticks([])
fig.savefig(Path.cwd()/'2005-circular-arch.png',dpi=150,facecolor='white')
