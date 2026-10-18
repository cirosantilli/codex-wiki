"""Original idealised product-model illustration, not empirical test scores.

Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes a same-basename PNG to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,(ax,bx)=plt.subplots(1,2,figsize=(11,5.2),dpi=120,facecolor='white',gridspec_kw={'width_ratios':[1.04,1]})
t=np.linspace(0,1,201);d,c=np.meshgrid(t,t)
im=ax.pcolormesh(d,c,d*c,shading='auto',cmap='Blues',vmin=0,vmax=1,rasterized=True)
ax.contour(d,c,d*c,levels=[.27],colors=['#555555'],linestyles='--',linewidths=1.2)
for x,y,label,color in [(.3,.9,'A','#c75335'),(.9,.3,'B','#8b3f9d')]:
 ax.scatter([x],[y],s=70,color=color,edgecolor='white',linewidth=1.0,zorder=4)
 ax.annotate(label,(x,y),xytext=(8,6),textcoords='offset points',color=color,weight='bold',fontsize=13)
ax.set(xlim=(0,1),ylim=(0,1),xlabel='Decoding D',ylabel='Linguistic comprehension C',title='Idealised comprehension: R = D × C')
ax.set_aspect('equal')
fig.colorbar(im,ax=ax,fraction=.044,pad=.03,label='Product R')
ys=np.arange(3);w=.34
bx.bar(ys-w/2,[.3,.9,.27],w,color='#c75335',label='Profile A')
bx.bar(ys+w/2,[.9,.3,.27],w,color='#8b3f9d',label='Profile B')
for xpos,vals in [(ys-w/2,[.3,.9,.27]),(ys+w/2,[.9,.3,.27])]:
 for x,y in zip(xpos,vals):bx.text(x,y+.025,f'{y:.2f}',ha='center',va='bottom',fontsize=10)
bx.set(xticks=ys,xticklabels=['Decoding\nD','Language\nC','Product\nR'],ylim=(0,1.05),ylabel='Illustrative model value',title='Same product, different profiles')
bx.spines[['top','right']].set_visible(False)
bx.legend(loc='upper center',bbox_to_anchor=(.5,-.2),ncol=2,frameon=False)
fig.suptitle('A comprehension score can conceal different component constraints',fontsize=15,weight='bold',y=.98)
fig.text(.5,.025,'Hypothetical normalised values only: no diagnostic cutoffs, test norms or treatment effects are represented.',ha='center',fontsize=10,color='#444444')
fig.subplots_adjust(left=.065,right=.98,top=.82,bottom=.23,wspace=.38)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
