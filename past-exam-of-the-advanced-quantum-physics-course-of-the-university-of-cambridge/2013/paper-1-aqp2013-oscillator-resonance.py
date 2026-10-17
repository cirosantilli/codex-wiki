"""Original oscillator wavefunctions and square-pulse line shape.
Python 3.14, NumPy 2.3, Matplotlib 3.10. Output is a basename in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
fig, axes = plt.subplots(1, 2, figsize=(9, 3.5), layout="constrained")
q=np.linspace(-3.6, 3.6, 700)
u0=np.pi**(-0.25)*np.exp(-q*q/2)
u1=np.sqrt(2)*q*u0
axes[0].plot(q,u0,label=r"$\sqrt{a_0}\,\psi_0$",lw=2)
axes[0].plot(q,u1,label=r"$\sqrt{a_0}\,\psi_1$",lw=2)
axes[0].axhline(0,color="0.7",lw=0.7)
axes[0].set(xlabel=r"$(x-x_0)/a_0$",ylabel="Dimensionless amplitude",title="Lowest oscillator states")
axes[0].legend(frameon=False)
z=np.linspace(-5*np.pi,5*np.pi,1600)
profile=np.sinc(z/np.pi)**2
axes[1].plot(z/np.pi,profile,lw=2,color="#145d80")
axes[1].set(xlabel=r"$(\Omega-\omega)T/(2\pi)$",ylabel=r"$p_1/p_{\rm resonant}$",ylim=(-0.03,1.1),title="Finite-time resonance")
axes[1].set_xticks(np.arange(-5,6))
axes[1].grid(alpha=0.2)
fig.savefig("paper-1-aqp2013-oscillator-resonance.png",dpi=140,facecolor="white",bbox_inches="tight")
