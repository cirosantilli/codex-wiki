"""Original figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to caller CWD."""
import os
import tempfile
if 'MPLCONFIGDIR' not in os.environ:
    os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp(prefix='ia2-direction-mpl-')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(5.6, 5), layout='constrained')
x, y = np.meshgrid(np.linspace(0, .97, 17), np.linspace(0, 1, 18))
m = x*np.sqrt((1-y*y)/(1-x*x))
dx = .023/np.sqrt(1+m*m)
dy = m*dx
for a,b,c,d in zip(x.flat,y.flat,dx.flat,dy.flat):
    ax.plot([a-c,a+c],[b-d,b+d],color='#87919e',lw=.9)
t = np.linspace(0, 1, 1500, endpoint=False)
ax.plot(t,np.sin(1-np.sqrt(1-t*t)),color='#1664ba',lw=2.4,label='Solution from (0, 0)')
ax.plot(0,0,'o',color='#1664ba',ms=5)
ax.plot(1,np.sin(1),'o',mfc='white',mec='#1664ba',ms=6,clip_on=False)
ax.plot([.93,1],[np.sin(1)]*2,alpha=0)
ax.annotate('Vertical limiting tangent',xy=(.997,np.sin(1)),xytext=(.36,.90),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.annotate('Horizontal tangent',xy=(0,0),xytext=(.17,.10),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.set(xlim=(-.035,1.035),ylim=(-.035,1.045),xlabel='x',ylabel='y',title='Positive square-root direction field')
ax.set_aspect('equal'); ax.legend(loc='center left',fontsize=9)
fig.savefig('paper-2-direction-field.png',dpi=125,facecolor='white',transparent=False)
