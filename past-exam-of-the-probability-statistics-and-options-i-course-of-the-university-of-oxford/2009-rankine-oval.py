"""Python 3.14, root NumPy/Matplotlib versions. Representative m/(2πU)=1.
One original image, written to the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1.8,2.8,470);y=np.linspace(-1.6,1.6,320);X,Y=np.meshgrid(x,y);z=X+1j*Y
q=1-1/(z*(z-1));mask=(abs(z)<.08)|(abs(z-1)<.08)
u=np.ma.array(q.real,mask=mask);v=np.ma.array(-q.imag,mask=mask)
fig,ax=plt.subplots(figsize=(7.3,4.1),layout='constrained',facecolor='white')
ax.streamplot(x,y,u,v,color='#5b8ba5',density=1.4,linewidth=.7,arrowsize=.7)
psi=Y+np.angle(z)-np.angle(z-1)
psi=np.ma.array(psi,mask=mask|((abs(Y)<.025)&(X>0)&(X<1)))
ax.contour(X,Y,psi,levels=[0],colors='#be4b28',linewidths=1.7)
roots=[(1-np.sqrt(5))/2,(1+np.sqrt(5))/2];ax.scatter(roots,[0,0],color='black',s=30,zorder=3)
ax.scatter([0],[0],color='#c34d22',marker='+',s=90,zorder=3);ax.scatter([1],[0],color='#c34d22',marker='_',s=90,zorder=3)
ax.text(0,-.18,'source',ha='center');ax.text(1,-.18,'sink',ha='center')
ax.set(xlabel='x',ylabel='y',title='Uniform stream + source − sink: m/(2πU) = 1',xlim=(-1.8,2.8),ylim=(-1.5,1.5));ax.set_aspect('equal')
fig.savefig('2009-rankine-oval.png',dpi=155,facecolor='white')
