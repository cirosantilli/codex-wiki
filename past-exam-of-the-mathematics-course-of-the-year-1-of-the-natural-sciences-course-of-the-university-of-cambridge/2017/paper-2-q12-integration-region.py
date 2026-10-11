"""Plot the original parabola/semicircle integration region; save PNG to cwd.

Tested with Python 3.14; dependencies are in the root pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

alpha = np.sqrt((np.sqrt(5)-1)/2)
x = np.linspace(-1,1,600)
z = np.linspace(-alpha,alpha,500)
fig, ax = plt.subplots(figsize=(6,4.6), layout='constrained')
ax.plot(x,np.sqrt(np.maximum(1-x*x,0)),color='#2465a6',linewidth=2,label=r'$y=\sqrt{1-x^2}$')
ax.plot(x,x*x,color='#b55821',linewidth=2,label=r'$y=x^2$')
ax.fill_between(z,z*z,np.sqrt(1-z*z),color='#6da9d8',alpha=.3)
ax.vlines([-alpha,alpha],0,alpha*alpha,colors='gray',linestyles=':',linewidth=1)
ax.scatter([-alpha,alpha],[alpha*alpha]*2,color='black',s=22,zorder=4)
ax.axhline(0,color='black',linewidth=.6)
ax.axvline(0,color='black',linewidth=.6)
ax.set(xlim=(-1.07,1.07),ylim=(-.08,1.12),xlabel='$x$',ylabel='$y$',title='Region between the parabola and semicircle')
ax.set_xticks([-1,-alpha,0,alpha,1],['−1','$-a$','0','$a$','1'])
ax.set_yticks([0,alpha*alpha,1],['0','$a^2$','1'])
ax.text(.12,.67,'integration\nregion',ha='center',va='center',fontsize=11,color='#17476c')
ax.set_aspect('equal',adjustable='box')
ax.spines[['top','right']].set_visible(False)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.15),ncol=2,frameon=False)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=170,facecolor='white')
