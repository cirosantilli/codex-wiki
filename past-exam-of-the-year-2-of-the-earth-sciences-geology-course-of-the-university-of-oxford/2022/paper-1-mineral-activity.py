"""Original mathematical solution diagram; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes its PNG to the current working directory; no source images are copied.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':10})

x=np.linspace(-8,-3,700);y=np.linspace(0,17,700);X,Y=np.meshgrid(x,y)
N=3.44-X-Y;A=-7.59-3*X-Y
field=np.argmin(np.stack([np.zeros_like(X),N,A]),axis=0)
fig,ax=plt.subplots(figsize=(6.8,4.5),dpi=100)
ax.contourf(X,Y,field,levels=[-.5,.5,1.5,2.5],colors=['#f1f2f3','#fce9d5','#e5f1f6'])
star=-5.515;ystar=8.955
left=x[x<=star];right=x[x>=star]
ax.plot(left,3.44-left,color='#b34c27',lw=2)
ax.plot(right,3.44-right,'--',color='#b34c27',lw=1.3)
ax.plot(right,-7.59-3*right,color='#177ca4',lw=2)
ax.plot(left,-7.59-3*left,'--',color='#177ca4',lw=1.3)
ax.plot([star,star],[ystar,17],color='#613f8e',lw=2)
ax.plot([star,star],[0,ystar],'--',color='#613f8e',lw=1.3)
ax.plot(star,ystar,'o',color='#283741')
ax.annotate('(−5.515, 8.955)',xy=(star,ystar),xytext=(-5.30,9.7),fontsize=9,
            arrowprops={'arrowstyle':'->','color':'#283741'})
ax.text(-7.30,13.7,'Nepheline',color='#7c391e',fontsize=12)
ax.text(-4.35,12.2,'Albite',color='#126885',fontsize=12)
ax.text(-6.35,3.0,'Corundum',color='#4a555c',fontsize=12)
ax.set(xlim=(-8,-3),ylim=(0,17),xlabel='log₁₀ a(H₄SiO₄⁰)',ylabel='log₁₀ [a(Na⁺) / a(H⁺)]')
ax.set_title('Three-mineral equilibrium at fixed temperature and pressure',fontsize=11)
ax.text(-7.85,.6,'Solid: stable boundary     Dashed: metastable continuation',fontsize=9)
fig.tight_layout(pad=1.1)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
