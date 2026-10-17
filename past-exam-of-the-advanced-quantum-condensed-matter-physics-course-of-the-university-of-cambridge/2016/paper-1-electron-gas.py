"""Original analytic teaching diagram; tested with Python 3.14, numpy, matplotlib.
Run from the intended output directory; PNG output is a basename in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
A=3*(9*np.pi/4)**(2/3)/10;B=3*(9*np.pi/4)**(1/3)/(4*np.pi)
rs=np.linspace(1.2,12,700);cross=A*(2**(2/3)-1)/(B*(2**(1/3)-1))
fig,axs=plt.subplots(1,2,figsize=(10,4),layout="constrained")
axs[0].plot(rs,A/rs**2,label="kinetic",color="#286b93")
axs[0].plot(rs,-B/rs,label="exchange",color="#b35c25")
axs[0].plot(rs,A/rs**2-B/rs,label="sum",color="#333333")
axs[0].set(xlabel="Dimensionless spacing r_s",ylabel="Unpolarized energy / N E_H*",title="Uniform Hartree-Fock energy scales")
# Positive difference means uniform polarized determinant is higher in energy.
delta=A*(2**(2/3)-1)/rs**2-B*(2**(1/3)-1)/rs
axs[1].plot(rs,delta,color="#7c53a0");axs[1].axhline(0,color="#333333",lw=1)
axs[1].axvline(cross,color="#777777",ls="--");axs[1].text(cross+.2,.018,f"restricted crossing\nr_s = {cross:.2f}",fontsize=10)
axs[1].set(xlabel="Dimensionless spacing r_s",ylabel="(E_polarized - E_unpolarized) / N E_H*",title="Compare only two uniform determinants",ylim=(-.02,.08))
axs[0].legend();
for ax in axs:ax.grid(alpha=.2)
fig.suptitle("Original 3D jellium calculation: no correlation or density-wave energy included")
fig.savefig("paper-1-electron-gas.png",dpi=155,facecolor="white")
