"""Integrate original top-hat plume equations by quadrature; save PNG in CWD.
Only NumPy 2.3.5 / Matplotlib 3.10.7, tested with Python 3.14.4.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
alpha=.09;E=2*alpha*np.sqrt(np.pi)
t=np.linspace(0,100,100001);r=t*t
I=np.r_[0,np.cumsum((2*t[1:]*(1+t[1:]**4)**.75+2*t[:-1]*(1+t[:-1]**4)**.75)*np.diff(t)/2)]
q=np.sqrt(2*I);dx=np.full_like(t,np.sqrt(2));dz=np.zeros_like(t);ds=dx.copy()
dx[1:]=2*t[1:]/q[1:];dz[1:]=r[1:]*dx[1:];ds[1:]=np.sqrt(1+r[1:]**2)*dx[1:]
integ=lambda f:np.r_[0,np.cumsum((f[1:]+f[:-1])*np.diff(t)/2)]
x,z,s=map(integ,[dx,dz,ds]);m=np.sqrt(1+r*r)
b=E/np.sqrt(np.pi)*q/np.sqrt(m)
xinf=x[-1]+2*np.sqrt(5)/t[-1]**.5
shat=r[-1]**.75/np.sqrt(.45);zv=z[-1]-shat
fig,ax=plt.subplots(figsize=(7.2,5.4),dpi=100,facecolor='white')
visible=z<17
ax.plot(x[visible],z[visible],color='#1c6b88',lw=2.4,label='centreline')
ax.plot((x-r/m*b)[visible],(z+b/m)[visible],color='#73a9bb',lw=1.3)
ax.plot((x+r/m*b)[visible],(z-b/m)[visible],color='#73a9bb',lw=1.3,label='top-hat edge')
zz=np.linspace(zv,17,200);cone=6*alpha/5*(zz-zv)
ax.plot(xinf+cone,zz,'--',color='#a26935',lw=1.2);ax.plot(xinf-cone,zz,'--',color='#a26935',lw=1.2,label='far-field extrapolation')
ax.axvline(xinf,color='#999999',ls=':',label='vertical asymptote')
ax.scatter([0,xinf],[0,zv],s=30,color=['#1c6b88','#a26935'],zorder=5)
ax.annotate('actual source',(0,0),xytext=(.3,1),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.annotate('virtual source',(xinf,zv),xytext=(1.1,-1.5),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.set(xlim=(-.3,8),ylim=(-2.3,16),xlabel='$x/\\ell_J$',ylabel='$z/\\ell_J$',title='Horizontal forced plume ($\\alpha=0.09$)')
ax.legend(loc='upper left',fontsize=9,frameon=False);ax.spines[['top','right']].set_visible(False)
fig.tight_layout();fig.savefig('paper-345-plume.png',facecolor='white',transparent=False)
