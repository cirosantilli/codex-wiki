"""Original figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to caller CWD."""
import os
import tempfile
if 'MPLCONFIGDIR' not in os.environ:
    os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp(prefix='ia2-factor-mpl-')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
lo,hi=0.,1.
for _ in range(55):
    mid=(lo+hi)/2
    if mid*mid > np.exp(-mid): hi=mid
    else: lo=mid
b=(lo+hi)/2
fig, ax = plt.subplots(figsize=(7, 4.6),layout='constrained')
x,y=np.meshgrid(np.linspace(-4,.67,21),np.linspace(.25,6.6,17))
m=-(2*x+x*x+y*y)/(2*y)
# Segments are normalized in display coordinates, avoiding misleading steepness.
sx,sy=4.9,7.1
norm=np.sqrt((1/sx)**2+(m/sy)**2)
u=.015/norm; v=m*u
for a,c,d,e in zip(x.flat,y.flat,u.flat,v.flat):
    ax.plot([a-d,a+d],[c-e,c+e],color='#c4c7cd',lw=.8)
t=np.linspace(-4,b,1800,endpoint=False)
ax.plot(t,np.sqrt(np.exp(-t)-t*t),color='#1664ba',lw=2.2,label=r'$y=\sqrt{e^{-x}-x^2}$')
ax.axhline(1,color='#a34a11',ls='--',lw=1.2,label='Barrier y = 1')
ax.plot(0,1,'o',color='#1664ba',ms=5)
ax.plot(b,0,'o',mfc='white',mec='#1664ba',ms=6)
ax.annotate('b = 0.703467…\nvertical limiting tangent',xy=(b,.02),xytext=(-1.8,.5),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.annotate('Steepens without bound\nas x → −∞',xy=(-3.9,5.9),xytext=(-2.6,5.4),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.set(xlim=(-4.12,.85),ylim=(-.15,7),xlabel='x',ylabel='y',title='Initial value a = 1: decreasing positive branch')
ax.legend(loc='upper right',fontsize=9)
fig.savefig('paper-2-integrating-factor.png',dpi=125,facecolor='white',transparent=False)
