"""Original schematic, not a fitted transfer function; Python 3.14/NumPy 2.3.5/Matplotlib 3.10.7.
Write opaque PNG basename to caller CWD, without altering caller MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

k=np.logspace(-4,1,2400)
# Correct k^1 and logarithm-corrected k^-3 asymptotes, illustrative turnover.
q=k/.03
transfer=np.log1p(q)/(q*(1+q))
smooth=k*transfer**2
wiggle=1+.085*np.sin(k*105)*np.exp(-(k/.25)**2)*(1-np.exp(-(k/.025)**2))
p=smooth*wiggle/np.max(smooth)
fig,(ax,bx)=plt.subplots(2,1,figsize=(8.4,6.6),sharex=True,gridspec_kw={'height_ratios':[3,2]},constrained_layout=True)
ax.loglog(k,p,lw=2,color='#176580',label='Illustrative linear spectrum')
ax.loglog(k,smooth/np.max(smooth),ls='--',lw=1,color='0.5',label='Without acoustic modulation')
ax.set(ylim=(1e-7,3),ylabel='Relative P(k)',title='Schematic matter power spectrum; arbitrary normalization')
ax.annotate('Equality turnover',(k[np.argmax(smooth)],1),(.001,1.7),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.text(.08,.25,'Baryon acoustic\nmodulation',fontsize=9)
ax.text(.4,3e-4,'Small scales need nonlinear\nand gas-physics modeling',fontsize=9)
ax.legend(loc='lower left',fontsize=8)
bands=[('CMB (model inference)',1e-4,.2),('Peculiar velocities',.003,.08),('Galaxy redshift surveys',.01,.2),('Clusters (normalization)',.07,.3),('Weak lensing (projection)',.02,3),('Ly-alpha forest (high z)',.3,5)]
for i,(name,lo,hi) in enumerate(bands):
    y=len(bands)-i
    bx.plot([lo,hi],[y,y],lw=5,solid_capstyle='butt',color=plt.cm.tab10(i))
    bx.text(1.35e-4,y,name,fontsize=8,va='center',bbox={'facecolor':'white','edgecolor':'none','alpha':.8})
bx.set(xlim=(1e-4,10),ylim=(.3,6.7),yticks=[],xlabel=r'Comoving wavenumber k (h Mpc$^{-1}$)',title='Approximate overlapping sensitivities, not strict survey limits')
bx.grid(axis='x',alpha=.2)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=110,facecolor='white',transparent=False)
