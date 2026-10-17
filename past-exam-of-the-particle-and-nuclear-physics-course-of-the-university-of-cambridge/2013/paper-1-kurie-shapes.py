"""Original model comparison, not digitized source data. Python 3.14/numpy/matplotlib."""
import numpy as np
import matplotlib.pyplot as plt

endpoint=4.0
t=np.linspace(0,endpoint,401)
p2=t*(t+2)
q2=(endpoint-t)**2
allowed=endpoint-t
unique=(endpoint-t)*np.sqrt(p2+q2)/endpoint
corrected=unique*endpoint/np.sqrt(p2+q2)
fig,ax=plt.subplots(figsize=(6.5,4.0),layout='constrained')
ax.plot(t,allowed,color='#245c94',lw=2,label='Constant shape / shape-corrected ordinate')
ax.plot(t,unique,color='#a23d25',lw=2,label='Unique-forbidden shape, left uncorrected')
ax.scatter([endpoint],[0],color='0.2',s=20,zorder=5)
ax.set(xlabel=r'Electron kinetic energy $T/(m_ec^2)$',ylabel='Illustrative Kurie ordinate',xlim=(0,4.2),ylim=(0,4.2),title='Same endpoint, different spectral shapes')
ax.text(.04,.08,r'Leading model: $C(T)\propto p_e^2+p_\nu^2$'+'\nCurves normalized to the same value at T = 0.',transform=ax.transAxes,fontsize=8)
ax.legend(fontsize=8)
ax.grid(alpha=.2)
fig.savefig('paper-1-kurie-shapes.png',dpi=150,facecolor='white')
plt.close(fig)
