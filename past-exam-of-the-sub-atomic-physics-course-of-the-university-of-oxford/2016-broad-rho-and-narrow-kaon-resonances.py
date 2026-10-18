from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white", "font.family": "DejaVu Sans"})
def fermion(ax,a,b,label,anti=False,offset=(0,0.14)):
    a,b=np.array(a,dtype=float),np.array(b,dtype=float)
    ax.plot([a[0],b[0]],[a[1],b[1]],color="#174c75",lw=2)
    p,q=(a+.40*(b-a),a+.60*(b-a))
    if anti:p,q=q,p
    ax.annotate("",xy=q,xytext=p,arrowprops=dict(arrowstyle="-|>",color="#174c75",lw=1.5,mutation_scale=12))
    m=(a+b)/2+offset
    ax.text(*m,label,ha="center",va="bottom",color="#123b59")
def boson(ax,a,b,label):
    a,b=np.array(a,dtype=float),np.array(b,dtype=float)
    d=b-a; n=np.array([-d[1],d[0]])/np.linalg.norm(d)
    t=np.linspace(0,1,400);v=a[:,None]+d[:,None]*t+0.055*n[:,None]*np.sin(2*np.pi*9*t)
    ax.plot(v[0],v[1],color="#b35b15",lw=1.8)
    ax.text(*((a+b)/2+np.array([0,0.16])),label,ha="center",va="bottom",color="#8b440f")

fig,axs=plt.subplots(1,2,figsize=(11.6,4.8),layout="constrained")
mK,gK,mr,gr=498.,7.4e-12,769.,147.
def rho(E):return 3*gr**2/((E*E-mr*mr)**2+E*E*gr**2)
# Inclusive formation: entrance branching .69 and exit branching 1.
kpeak=.69/mK**2
E=np.linspace(470,830,1600)
axs[0].plot(E,rho(E)/kpeak,color="#b35b15",lw=2,label=r"$\rho^0$ / kaon peak")
axs[0].axvline(mK,color="#174c75",lw=1.5,ls=":")
axs[0].scatter([498,500],rho(np.array([498.,500.]))/kpeak,color="#b35b15",zorder=4)
axs[0].annotate("Kaon lies here; its width is\nunresolved on this MeV scale",xy=(498,.1),xytext=(545,.95),arrowprops=dict(arrowstyle="->"),fontsize=10)
axs[0].set(xlabel="Total collision energy (MeV)",ylabel="Inclusive formation cross section / kaon peak",title="Broad rho contribution",ylim=(0,2))
axs[0].grid(alpha=.2)
# Stable evaluation avoids subtracting two nearly equal ~498-MeV squares.
x=np.linspace(-5,5,1600);d=x*gK
K=.69/(((2*mK+d)*x)**2+(mK+d)**2)
axs[1].plot(x,K/kpeak,color="#174c75",lw=2,label=r"$K_S$")
axs[1].axhline(rho(mK)/kpeak,color="#b35b15",lw=1.8,label=r"$\rho^0$ background")
axs[1].set(xlabel=r"Detuning $(E-m_K)/\Gamma_K$",ylabel="Cross section / kaon peak",title="Kaon on its natural width scale",ylim=(0,1.08))
axs[1].text(0,1.04,r"$\Gamma_K=7.4\times10^{-12}$ MeV",ha="center",fontsize=11)
axs[1].legend(frameon=False);axs[1].grid(alpha=.2)
fig.suptitle("Finite peak height does not imply a useful narrow-resonance yield",fontsize=15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,transparent=False)
