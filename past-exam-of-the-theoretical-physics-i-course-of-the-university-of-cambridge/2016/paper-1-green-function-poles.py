"""Original explanatory plot. Tested with Python 3.14, NumPy and Matplotlib.
Write the PNG basename into the current working directory (Make mirrors it).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white"})
fig,axs=plt.subplots(1,3,figsize=(10,3.6),layout='constrained')
for ax,w0,title in zip(axs,[1.5,1.,.6],['Underdamped','Critical','Overdamped']):
 roots=-1j+np.array([1,-1])*np.sqrt(complex(w0*w0-1))
 ax.axhline(0,color='.35',lw=1);ax.axvline(0,color='.35',lw=1)
 ax.scatter(roots.real,roots.imag,marker='x',s=90,lw=2.5,color='#bc3434',zorder=3)
 ax.set(xlim=(-1.7,1.7),ylim=(-2.3,.4),xlabel=r'$\mathrm{Re}\,\omega$',ylabel=r'$\mathrm{Im}\,\omega$',title=title);ax.grid(alpha=.18);ax.set_aspect('equal')
 ax.text(.04,.07,r'$\omega_0='+str(w0)+r',\ \lambda=1$',transform=ax.transAxes,fontsize=10)
 if w0==1:ax.annotate('double pole',xy=(0,-1),xytext=(.25,-.65),fontsize=9,arrowprops={'arrowstyle':'->'})
fig.savefig('paper-1-green-function-poles.png',dpi=150,facecolor='white');plt.close(fig)
