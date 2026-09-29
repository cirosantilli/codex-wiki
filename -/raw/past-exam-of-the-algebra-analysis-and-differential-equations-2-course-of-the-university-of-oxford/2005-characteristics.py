"""Characteristic families for y*u_xx=u_yy. Python 3.14; NumPy/Matplotlib."""
import numpy as np
import matplotlib.pyplot as plt

y=np.linspace(0,2.2,400)
fig,ax=plt.subplots(figsize=(7,4.5),facecolor='white')
for j,c in enumerate(np.arange(-9,10,2)):
 ax.plot((c+2*y**1.5)/3,y,color='#1769aa',lw=1.4,label=r'$3x-2y^{3/2}=c$' if j==0 else None)
 ax.plot((c-2*y**1.5)/3,y,color='#c45514',lw=1.4,ls='--',label=r'$3x+2y^{3/2}=c$' if j==0 else None)
ax.axhline(0,color='black',lw=1)
ax.set(xlim=(-3,3),ylim=(-.08,2.2),xlabel='$x$',ylabel='$y$',title=r'Characteristics of $y u_{xx}=u_{yy}$ in $y>0$')
ax.legend(loc='upper center',framealpha=1);ax.grid(alpha=.15);fig.tight_layout()
fig.savefig('2005-characteristics.png',dpi=150,facecolor='white')
