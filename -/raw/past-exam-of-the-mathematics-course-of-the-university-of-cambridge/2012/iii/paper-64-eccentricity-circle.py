"""Original secular eccentricity diagram. Tested Python 3.14.4,
numpy 2.3.5, matplotlib 3.10.7. Output is a cwd basename; MPLCONFIGDIR is preserved.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots(figsize=(6.8001,4.8001),dpi=100,facecolor='white')
fig.subplots_adjust(left=.13,right=.96,bottom=.15,top=.86)
phase=np.linspace(0,2*np.pi,801)
z=1-np.exp(1j*phase)
ax.plot(z.real,z.imag,color='#1669bb',lw=2.5)
ax.axhline(0,color='#888888',lw=.8);ax.axvline(0,color='#888888',lw=.8)
for p in [.4,2.2,4.1]:
    za=1-np.exp(1j*p);zb=1-np.exp(1j*(p+.23))
    ax.annotate('',xy=(zb.real,zb.imag),xytext=(za.real,za.imag),arrowprops={'arrowstyle':'->','color':'#1669bb','lw':1.7})
for p,label,dx,dy in [(0,r'$At=0,\ 2\pi$',-.03,.17),(np.pi/2,r'$At=\pi/2$',.04,-.19),(np.pi,r'$At=\pi$',.10,.12),(3*np.pi/2,r'$At=3\pi/2$',.04,.10)]:
    zi=1-np.exp(1j*p)
    ax.scatter([zi.real],[zi.imag],s=32,color='#1669bb')
    ax.text(zi.real+dx,zi.imag+dy,label,fontsize=10,ha='center' if p==0 else 'left')
ax.scatter([1],[0],s=38,color='#c35d30',zorder=5)
ax.annotate('',xy=(1,0),xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#c35d30','lw':1.8})
ax.annotate(r'Forced vector $Z_f$',xy=(.55,0),xytext=(.08,.46),fontsize=11,color='#9a431e',arrowprops={'arrowstyle':'->','color':'#c35d30'})
p=3.7;point=1-np.exp(1j*p)
ax.annotate('',xy=(point.real,point.imag),xytext=(1,0),arrowprops={'arrowstyle':'->','color':'#c35d30','lw':1.7})
ax.text(1.50,.72,r'Free radius $Z_f$',color='#9a431e',fontsize=10)
ax.set_aspect('equal');ax.set_xlim(-.4,2.5);ax.set_ylim(-1.4,1.4)
ax.set_xlabel(r'$\operatorname{Re}z/Z_f$');ax.set_ylabel(r'$\operatorname{Im}z/Z_f$')
ax.set_title(r'$z=Z_f(1-e^{iAt})$: forced + free eccentricity',fontsize=13,pad=12)
ax.grid(alpha=.15)
fig.savefig('paper-64-eccentricity-circle.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
