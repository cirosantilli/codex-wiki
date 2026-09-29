"""Original trapped-mode profile; output PNG in CWD using pinned plotting packages."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
k=1.;H=1.;a=k/np.tanh(k*H)
lo,hi=0.,np.pi/H
for _ in range(70):
 m=(lo+hi)/2
 if m*H+np.arctan(m/a)+np.arctan(m/k)<np.pi:lo=m
 else:hi=m
m=(lo+hi)/2;delta=np.arctan(m/a)
z=np.linspace(0,4,1000)
w=np.where(z<H,np.sin(delta)*np.sinh(k*z)/np.sinh(k*H),np.where(z<=2*H,np.sin(m*(z-H)+delta),np.sin(m*H+delta)*np.exp(-k*(z-2*H))))
fig,ax=plt.subplots(figsize=(6.8,4.8),dpi=100,facecolor='white')
ax.axhspan(H,2*H,color='#e5f1f8');ax.plot(w,z,color='#27698f',lw=2.5)
ax.axvline(0,color='#999999',ls='--');ax.axhline(H,color='#555555',ls=':');ax.axhline(2*H,color='#555555',ls=':');ax.axhline(0,color='black',lw=2)
ax.text(-.55,.5,'unstratified\nlower layer',ha='center');ax.text(-.55,1.5,'stratified\nwave guide',ha='center');ax.text(-.55,3.2,'unstratified\nupper layer',ha='center')
ax.set(xlim=(-.9,1.2),ylim=(0,4),xlabel='Vertical-velocity mode amplitude (arbitrary units)',ylabel='$z/H$',title='Fundamental trapped mode, $kH=1$')
ax.set_yticks([0,1,2,3,4]);ax.spines[['top','right']].set_visible(False)
fig.tight_layout();fig.savefig('paper-345-trapped-wave.png',facecolor='white',transparent=False)
