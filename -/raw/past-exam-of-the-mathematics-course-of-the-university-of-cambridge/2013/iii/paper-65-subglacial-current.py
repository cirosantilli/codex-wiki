"""Original schematic. Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7.
Writes one opaque PNG basename to caller cwd; preserves caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
x=np.linspace(0,9,400);h=1.8-.11*x-.005*x*x
fig,ax=plt.subplots(figsize=(9,4.8),dpi=100,facecolor='white');ax.set_facecolor('white')
ax.fill_between(x,0,h,color='#b9dff1',label='Meltwater')
ax.fill_between(x,h,2.5,color='#e0e8eb');ax.fill_between(x,-.5,0,color='#9c968a')
ax.plot(x,h,color='#435860',linewidth=2);ax.axhline(0,color='#49443b',linewidth=2)
ax.fill_between(x,0,.10,color='#639ebb',alpha=.7)
ax.fill_between(x,h-.10,h,color='#639ebb',alpha=.7)
ax.text(.25,2.15,'Glacial ice',fontsize=12);ax.text(.25,-.32,'Horizontal bedrock',fontsize=11)
ax.text(5.0,1.42,r'Ice–water interface: $p=p_0$',fontsize=11)
ax.text(.4,.72,r'$p=p_0+\rho_wg(h-z)$',fontsize=12)
ax.annotate('',(6.1,.33),(3.6,.33),arrowprops={'arrowstyle':'->','linewidth':2.5,'color':'#164f79'})
ax.text(3.8,.49,r'$u=-Dhh_x>0$',fontsize=12,color='#164f79')
ax.annotate('',(2.8,.1),(2.8,0),arrowprops={'arrowstyle':'<->','linewidth':1.1})
ax.annotate(r'Viscous layer $\delta_v$',(2.8,.08),xytext=(.15,-.70),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.annotate('',(8.6,h[np.argmin(abs(x-8.6))]),(8.6,0),arrowprops={'arrowstyle':'<->','linewidth':1.2})
ax.text(8.72,.24,r'$h$',fontsize=12)
ax.annotate('',(7.6,.5),(7.6,1.04),arrowprops={'arrowstyle':'->','linewidth':1.4});ax.text(7.74,.83,r'$g$',fontsize=12)
ax.annotate('',(1.6,h[np.argmin(abs(x-1.6))]+.37),(1.6,h[np.argmin(abs(x-1.6))]),arrowprops={'arrowstyle':'->','linewidth':1.2,'color':'#aa4327'})
ax.text(1.8,1.78,r'Melt retreat $v_m$',fontsize=10,color='#aa4327')
ax.text(5.8,-.70,'Both wall stresses oppose flow',ha='center',fontsize=10)
ax.set(xlim=(-.15,9.4),ylim=(-1.0,2.65),title='Pressure-driven subglacial current: constant wall-layer closure')
ax.set_xlabel(r'Along-bed coordinate $x$');ax.set_ylabel(r'Vertical coordinate $z$');ax.set_xticks([]);ax.set_yticks([])
for spine in ['top','right']:ax.spines[spine].set_visible(False)
fig.tight_layout();fig.savefig('paper-65-subglacial-current.png',dpi=100,transparent=False,facecolor='white');plt.close(fig)
