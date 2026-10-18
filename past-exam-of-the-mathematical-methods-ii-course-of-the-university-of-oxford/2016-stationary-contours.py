"""Original illustration for the 2016 Oxford Mathematical Methods II solution.
Run from any output directory; writes only the matching PNG to that directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

s=np.sqrt(2/3)
x=np.linspace(-2.05,2.05,801);X,Y=np.meshgrid(x,x);F=X**3+Y**3-2*X-2*Y
fig,ax=plt.subplots(figsize=(7.5,6.8),layout='constrained')
cs=ax.contour(X,Y,F,levels=[-8,-5,-3,-2,-1,1,2,3,5,8],cmap='coolwarm',linewidths=1.1)
ax.clabel(cs,fontsize=9,fmt='%g')
ax.contour(X,Y,F,levels=[0],colors=['#303030'],linewidths=2)
for xx,yy,label,col,offset in [(s,s,'local minimum', '#1456a0',(9,12)),(-s,-s,'local maximum','#a02323',(-103,-23)),(s,-s,'saddle','#20804b',(9,-23)),(-s,s,'saddle','#20804b',(-52,12))]:
 ax.scatter([xx],[yy],s=48,c=col,edgecolors='white',zorder=5)
 ax.annotate(label,(xx,yy),xytext=offset,textcoords='offset points',fontsize=10,color=col,bbox=dict(facecolor='white',alpha=.85,edgecolor='none',pad=1))
ax.set(xlim=(-2.05,2.05),ylim=(-2.05,2.05),xlabel='$x$',ylabel='$y$',title=r'$f(x,y)=x^3+y^3-2x-2y$'+'\nBlack zero contour: line and ellipse')
ax.set_aspect('equal');ax.grid(alpha=.15)
fig.savefig(Path.cwd()/'2016-stationary-contours.png',dpi=140,transparent=False)
plt.close(fig)
