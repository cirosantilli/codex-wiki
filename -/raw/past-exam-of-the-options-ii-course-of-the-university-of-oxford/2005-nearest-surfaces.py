"""Original y=0 section. Python3.14.4, NumPy2.3.5, Matplotlib3.10.7; output CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6.8,5),facecolor='white',layout='constrained');ax.set_facecolor('white')
t=np.linspace(0,2*np.pi,600);x=np.linspace(-3.1,3.1,600)
ax.plot(np.cos(t),np.sin(t),color='#2563eb',lw=2,label=r'unit sphere section: $x^2+z^2=1$')
ax.plot(x,(x*x-6)/2,color='#dc2626',lw=2,label=r'other surface section: $z=(x^2-6)/2$')
for sign in [-1,1]:
 b=np.array([2*sign,-1.]);a=b/np.sqrt(5)
 ax.plot([a[0],b[0]],[a[1],b[1]],color='#059669',lw=3)
 ax.scatter([a[0],b[0]],[a[1],b[1]],s=26,color='#059669',zorder=5)
 if sign==1:
  ax.annotate(r'$b=(2,0,-1)$',b,xytext=(1.75,-1.75),arrowprops={'arrowstyle':'->'})
  ax.annotate(r'$a=b/\sqrt{5}$',a,xytext=(.1,1.35),arrowprops={'arrowstyle':'->'})
ax.text(-2.95,1.9,r'minimum distance $=\sqrt{5}-1$',fontsize=12)
ax.axhline(0,lw=.6,color='#9ca3af');ax.axvline(0,lw=.6,color='#9ca3af')
ax.set(xlim=(-3.2,3.2),ylim=(-3.3,2.2),xlabel=r'$x$',ylabel=r'$z$');ax.set_aspect('equal')
ax.set_title('Closest pairs in the section y = 0');ax.legend(loc='lower center',fontsize=8)
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd()/'2005-nearest-surfaces.png',dpi=150,facecolor='white')
