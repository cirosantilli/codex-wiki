"""Contour geometry of a polynomial with a minimum and two saddle points."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-.7,.7,900);y=np.linspace(-.95,.95,1000);X,Y=np.meshgrid(x,y);Z=X*X+Y*Y+3*X**4-3*Y**4
fig,ax=plt.subplots(figsize=(8,7.4),layout='constrained')
cs=ax.contour(X,Y,Z,levels=[-.2,0,.025,.06,.14,.3,.6],colors=['#266eb2','.5','#2d914c','#2d914c','#2d914c','#2d914c','#2d914c'],linewidths=1.3)
ax.clabel(cs,levels=[-.2,0,.06,.14,.3],fontsize=9,fmt='%.2g')
ax.contour(X,Y,Z,levels=[1/12],colors=['#b9342a'],linewidths=2)
a=1/np.sqrt(6);ax.scatter([0,0,0],[0,a,-a],color=['#222','#b9342a','#b9342a'],s=35,zorder=5)
ax.annotate('minimum: f = 0',(0,0),xytext=(.13,-.12),arrowprops=dict(arrowstyle='-',color='.3'),fontsize=10)
for yy,offset in [(a,(.14,.44)),(-a,(.14,-.49))]:ax.annotate('saddle: f = 1/12',(0,yy),xytext=offset,arrowprops=dict(arrowstyle='-',color='#b9342a'),fontsize=10,color='#b9342a')
ax.set(xlabel='x',ylabel='y',aspect='equal',title=r'$f=x^2+y^2+3x^4-3y^4$'+'\nRed: critical contour f = 1/12');ax.grid(alpha=.12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
