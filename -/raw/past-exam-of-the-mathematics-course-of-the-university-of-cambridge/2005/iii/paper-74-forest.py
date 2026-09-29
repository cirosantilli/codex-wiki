"""Original schematic; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Emit an opaque PNG basename to the caller's CWD; respect caller MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, (ax, bx) = plt.subplots(2, 1, figsize=(8.2, 6.4), constrained_layout=True)
x = np.linspace(4000, 5150, 4500)
emission = 1 + 1.1*np.exp(-0.5*((x-4862.68)/40)**2)
centers = [4030,4068,4094,4142,4200,4255,4280,4318,4385,4411,4452,4505,4550,4593,4622,4670,4690,4738,4770,4805]
tau = np.zeros_like(x)
for i, center in enumerate(centers):
    tau += (0.25+0.8*((i*7)%11)/10)*np.exp(-0.5*((x-center)/(.25+0.035*(i%4)))**2)
ax.plot(x, emission*np.exp(-tau), color='#176580', lw=1.3)
ax.axvline(4862.68, color='0.5', ls='--', lw=1)
ax.annotate('Broad quasar Ly-alpha emission\n(z = 3)', (4863,2.04), (4550,2.23), arrowprops={'arrowstyle':'->'}, fontsize=9)
ax.text(4210,1.23,'Foreground Ly-alpha forest',fontsize=10)
ax.set(xlim=(4000,5150), ylim=(0,2.7), xlabel='Observed wavelength (angstroms)', ylabel='Relative flux', title='Original schematic quasar spectrum')
logn = np.linspace(12,22,600)
logf = np.where(logn<17, -1.5*(logn-13), np.where(logn<20.3,-6-(logn-17),-9.3-2*(logn-20.3)))
logf -= np.maximum(0, 10**(logn-21.6)-0.5)
bx.loglog(10**logn, 10**logf, color='#176580',lw=2)
for v,label in [(17.2,'Lyman limit'),(20.3,'Damped systems')]:
    bx.axvline(10**v, color='0.5',ls='--',lw=1)
    bx.text(10**(v+.08),0.5,label,fontsize=9,rotation=90,va='top')
bx.text(10**13,1e-2,'Forest: approximate slope -1.5',fontsize=9)
bx.set(xlim=(1e12,1e22),ylim=(1e-15,50),xlabel=r'Neutral hydrogen column $N_{\rm HI}$ (cm$^{-2}$)',ylabel=r'Relative $f_X(N)$ (arbitrary normalization)',title='Schematic column distribution at z about 3; breaks are illustrative')
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=110,facecolor='white',transparent=False)
