"""Plot the quartic's feasible region and complete minimizer set; output to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig,ax=plt.subplots(figsize=(8.5,6.5),dpi=100,facecolor='white')
x=np.linspace(-3.1,3.1,501);y=np.linspace(-2.25,2.25,401);xx,yy=np.meshgrid(x,y)
z=(xx**2+2*yy)**2-6;z=np.ma.masked_where(xx**2+2*yy**2>9,z)
levels=[-6,-5,0,10,25,45,65,84.25]
c=ax.contourf(xx,yy,z,levels=levels,cmap='YlOrRd',alpha=.8)
fig.colorbar(c,ax=ax,label='h(x,y)',shrink=.82,pad=.035)
t=np.linspace(0,2*np.pi,600);ax.plot(3*np.cos(t),3/np.sqrt(2)*np.sin(t),color='#334155',lw=2,label='feasible boundary')
limit=np.sqrt(np.sqrt(19)-1);u=np.linspace(-limit,limit,400)
ax.plot(u,-u*u/2,color='#1555bd',lw=3,label='minimum h = −6')
maxx=np.sqrt(17/2)
ax.scatter([-maxx,maxx],[.5,.5],marker='*',s=170,color='#064e3b',edgecolor='white',lw=.6,zorder=5,label='maximum h = 337/4')
ax.axhline(0,color='#6b7280',lw=.6);ax.axvline(0,color='#6b7280',lw=.6)
ax.set(xlabel='x',ylabel='y',xlim=(-3.25,3.25),ylim=(-2.4,2.4),aspect='equal',title='Squared residual on an ellipse')
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.13),ncol=1,frameon=False)
fig.subplots_adjust(left=.1,right=.93,bottom=.24,top=.91)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white')
plt.close(fig)
