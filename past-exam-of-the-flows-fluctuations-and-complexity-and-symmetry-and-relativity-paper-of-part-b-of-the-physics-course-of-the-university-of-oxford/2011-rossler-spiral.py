"""Generate the local linearized Rössler phase portrait; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

a=0.16
omega=np.sqrt(1-a*a/4)
t=np.linspace(0,12*np.pi,3000)
# Exact solution of X'=-Y, Y'=X+aY, with (X(0),Y(0))=(.05,0).
X=.05*np.exp(a*t/2)*(np.cos(omega*t)-a*np.sin(omega*t)/(2*omega))
Y=.05*np.exp(a*t/2)*np.sin(omega*t)/omega
fig,ax=plt.subplots(figsize=(5.6,4.9),layout='constrained',facecolor='white')
ax.set_facecolor('white')
ax.axhline(0,color='.8',lw=.7);ax.axvline(0,color='.8',lw=.7)
ax.plot(X,Y,color='#1764a0',lw=1.8)
for idx in [350,1100,1800,2500]:
 ax.annotate('',xy=(X[idx+30],Y[idx+30]),xytext=(X[idx],Y[idx]),arrowprops=dict(arrowstyle='->',color='#1764a0',lw=1.7))
ax.scatter([0],[0],s=28,color='#b23c28',zorder=3)
ax.annotate('Inner equilibrium',xy=(0,0),xytext=(.12,-.12),fontsize=10)
ax.set(xlabel=r'$X=x-x_-$',ylabel=r'$Y=y-y_-$',title='Local planar motion: outward, counterclockwise')
ax.set_aspect('equal',adjustable='box')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=145,facecolor='white',transparent=False)
