import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
r=np.linspace(0,5,500);u=(r*r-9)/2
fig,ax=plt.subplots(figsize=(7.2,3.4),dpi=100)
ax.plot(r,u,lw=2,color='tab:blue',label=r'$U_2/a^2=((b/a)^2-9)/2$')
ax.axhline(0,color='black',lw=.7);ax.axvline(3,color='gray',ls=':',alpha=.7);ax.scatter([3],[0],color='black',s=24,zorder=3)
ax.annotate('Leading cancellation',xy=(3,0),xytext=(1.1,4.7),arrowprops={'arrowstyle':'->','color':'black'})
ax.text(.3,-3.8,'Longitudinal mode dominates\nLaboratory swimming along +x',fontsize=9)
ax.text(3.5,3.3,'Transverse mode dominates\nLaboratory swimming along -x',fontsize=9)
ax.set(xlabel=r'Amplitude ratio $b/a$',ylabel=r'Mean far-field coefficient $U_2/a^2$',xlim=(0,5),title='Opposing contributions at different wavenumbers')
ax.grid(alpha=.15);fig.tight_layout();fig.savefig('paper-334-sheet-cancellation.png',facecolor='white',transparent=False)
