"""Generate the phase diagram in the working directory; Make owns media placement.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8.2, 4.8), dpi=100, facecolor='white')
fig.subplots_adjust(left=.10,right=.97,bottom=.14,top=.89)
C0, CB, CE = .32, .72, 1.0
Tm, T0, TB, TE, Tinf = 1.25, .93, .53, .25, 1.14
cs = np.linspace(0, 1.03, 200)
ax.plot(cs, Tm-cs, color='#285b8f', lw=2.3, label='Liquidus: $T=T_m-mC$')
ax.fill_between(cs, Tm-cs, 1.32, color='#edf5fb')
ax.fill_between(cs[cs<=1], TE, (Tm-cs)[cs<=1], color='#fff5da')
ax.axhline(TE,color='gray',ls=':',lw=1)
ax.plot([0,CB],[TB,TB],color='#b66212',lw=2)
ax.scatter([0,C0,CB],[TB,TB,TB],s=[42,30,42],color=['#b66212','#555555','#b66212'],zorder=5)
ax.annotate('pure solid',xy=(0,TB),xytext=(.025,.40),fontsize=10)
ax.annotate('bulk composition',xy=(C0,TB),xytext=(.17,.34),fontsize=10)
ax.annotate('roof liquid',xy=(CB,TB),xytext=(.73,.60),fontsize=10)
ax.annotate('',xy=(C0,T0),xytext=(C0,Tinf),arrowprops={'arrowstyle':'->','color':'#175747','lw':2})
ax.annotate('',xy=(CB,TB),xytext=(C0,T0),arrowprops={'arrowstyle':'->','color':'#bf302d','lw':2.5})
ax.scatter([C0,C0],[Tinf,T0],color='#175747',s=35,zorder=6)
ax.text(C0+.04,Tinf,'initial liquid',fontsize=10)
ax.text(.50,.86,'residual liquid\nenriches in solute',fontsize=10,color='#a32b29')
ax.text(.07,1.06,'liquid',fontsize=12)
ax.text(.06,.73,'solid + liquid',fontsize=12)
ax.text(1.005,TE+.015,'eutectic',fontsize=9,rotation=90,va='bottom')
ax.set_xticks([0,C0,CB,CE],['$C_s=0$','$C_0$','$C_B$','$C_E$'])
ax.set_yticks([TE,TB,T0,Tinf,Tm],['$T_E$','$T_B$','$T_0$',r'$T_\infty$','$T_m$'])
ax.set(xlim=(-.025,1.09),ylim=(.19,1.33),xlabel='Liquid / bulk solute concentration',ylabel='Temperature',title='Roof-cooled magma: negligible liquid solute diffusivity limit')
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd()/'paper-332-phase-diagram.png',facecolor='white',transparent=False,dpi=100)
plt.close(fig)
