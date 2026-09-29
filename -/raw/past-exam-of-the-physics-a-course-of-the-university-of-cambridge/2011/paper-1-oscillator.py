"""Original pedagogical figure; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run from the destination directory: output is the script's basename PNG in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})
m,k,b=9.1e-31,2.9,5.7e-18
w0=np.sqrt(k/m);gam=b/m;Om=np.sqrt(w0*w0-gam*gam/4)
fig,axs=plt.subplots(1,2,figsize=(9,3.5),layout='constrained')
z=np.linspace(-4,4,2500);w=w0+gam*z;P=gam**2/((w0*w0/w-w)**2+gam**2)
axs[0].plot(z,P,c='#176493',lw=2);axs[0].axhline(.5,c='0.5',ls='--',lw=1)
axs[0].annotate('',xy=(-.5,.5),xytext=(.5,.5),arrowprops={'arrowstyle':'<->','color':'#b64b24'})
axs[0].text(.65,.54,r'$\Delta\omega=\gamma$')
axs[0].set(xlabel=r'$(\omega-\omega_0)/\gamma$',ylabel=r'$P/P_{\max}$',title='Power response',ylim=(0,1.08))
t=np.linspace(0,1e-12,14000);xx=np.exp(-gam*t/2)*(np.cos(Om*t)+gam/(2*Om)*np.sin(Om*t))
axs[1].plot(t/1e-12,xx,lw=.45,c='#176493')
for sign in [-1,1]:axs[1].plot(t/1e-12,sign*np.exp(-gam*t/2),c='#b64b24',ls='--',lw=1.2)
axs[1].set(xlabel='Time after release (ps)',ylabel=r'$x/x_s$',title='Free release and amplitude envelope',xlim=(0,1),ylim=(-1.07,1.07))
fig.savefig("paper-1-oscillator.png", dpi=165, facecolor="white", bbox_inches="tight")
plt.close(fig)
