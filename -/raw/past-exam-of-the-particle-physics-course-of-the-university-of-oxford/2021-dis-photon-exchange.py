from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})
fig, ax = plt.subplots(figsize=(7.5,4.1),layout="constrained")
ax.set_xlim(-0.6,6.5);ax.set_ylim(-1.0,3.8);ax.axis("off")
def fermion(start,end,label,where):
    ax.annotate("",xy=end,xytext=start,arrowprops={"arrowstyle":"->","lw":1.8,"shrinkA":0,"shrinkB":0})
    ax.text(*where,label,ha="center")
fermion((0,3),(2.7,2.3),r"$e^-(p_1)$",(0.7,3.25))
fermion((2.7,2.3),(5.5,3),r"$e^-(p_3)$",(4.8,3.25))
fermion((0,0),(2.7,0.7),r"$q_f(xp_2)$",(0.6,-0.45))
fermion((2.7,0.7),(5.5,0),"struck parton → hadrons",(4.8,-0.5))
t=np.linspace(0,1,450)
ax.plot(2.7+0.10*np.sin(12*np.pi*t),0.7+1.6*t,color="#1769aa",lw=1.7)
ax.text(3.05,1.55,r"$\gamma^*(q)$",color="#1769aa")
ax.text(3.05,1.16,r"$q^2=-Q^2<0$",color="#1769aa",fontsize=10)
ax.plot([2.7,2.7],[0.7,2.3],"ko",ms=5)
ax.text(2.25,2.6,r"$e$");ax.text(2.1,0.32,r"$e e_q$")
ax.plot([-0.15,5.5],[-0.65,-0.65],color="0.5",lw=4,alpha=.35)
ax.text(2.6,-0.92,"proton remnant (schematic)",ha="center",fontsize=10)
ax.set_title("Leading electromagnetic deep-inelastic scattering")
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
