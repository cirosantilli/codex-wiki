"""Python 3.14; matplotlib 3.10.7, numpy 2.3.5 (root pyproject).
Generate an opaque 840x600 PNG in the caller's working directory.
The caller controls MPLCONFIGDIR; this script does not override it.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
names=['Clift','Ford','Gomez','Mannoni','Oza','Petersen','Schiffer','Strauss','Sutton','Winston']
y=np.array([-1.52,.24,-1.27,-1.68,-.30,.03,-1.57,.58,-.17,0.])
se=np.array([1.07,.82,.74,1.03,.82,.33,1.03,.46,.35,.22])
w=1/se**2;mean=float(np.dot(w,y)/sum(w))
fig,ax=plt.subplots(figsize=(8.4,6),dpi=100,facecolor='white')
ax.set_facecolor('white')
s=np.linspace(0,1.2,200)
ax.fill_betweenx(s,mean-2*s,mean+2*s,color='#dbe7ee',alpha=1)
ax.plot(mean-2*s,s,'--',color='#657b89',lw=1.2)
ax.plot(mean+2*s,s,'--',color='#657b89',lw=1.2,label='Approximate 95% limits: pooled log RR ± 2 SE')
ax.axvline(mean,color='#25617a',lw=1.2,label=f'Fixed-effect pooled log RR = {mean:.3f}')
ax.axvline(0,color='#909090',lw=.9,linestyle=':')
ax.scatter(y,se,s=46,color='#173e57',edgecolors='white',linewidths=.7,zorder=3)
offsets=[(7,7),(7,-8),(7,5),(-70,0),(7,5),(7,10),(-66,-10),(7,4),(-54,-13),(7,-5)]
for name,x,s0,offset in zip(names,y,se,offsets):
 ax.annotate(name,(x,s0),xytext=offset,textcoords='offset points',fontsize=9,color='#173e57')
ax.set_xlim(-2.7,2.5);ax.set_ylim(1.2,0)
ax.set_xlabel('Log risk ratio (transfusion / control)')
ax.set_ylabel('Standard error (greater precision at the top)')
ax.set_title('Funnel plot of the ten trial estimates',pad=12)
ax.grid(axis='y',color='#eeeeee',lw=.7)
ax.legend(loc='lower right',fontsize=8,framealpha=1,facecolor='white')
fig.subplots_adjust(left=.12,right=.97,bottom=.13,top=.89)
fig.savefig('paper-32-funnel.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
