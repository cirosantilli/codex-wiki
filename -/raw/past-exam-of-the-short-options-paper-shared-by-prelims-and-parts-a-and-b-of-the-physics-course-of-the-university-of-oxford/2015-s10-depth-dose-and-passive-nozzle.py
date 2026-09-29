from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

from matplotlib.patches import FancyBboxPatch
fig=plt.figure(figsize=(11.5,7.2),layout="constrained");gs=fig.add_gridspec(2,1,height_ratios=[2,1]);ax=fig.add_subplot(gs[0]);bx=fig.add_subplot(gs[1])
z=np.linspace(0,23,1200)
ph=(1-.82*np.exp(-z/.55))*np.exp(-z/12);ph/=ph.max()
pr=(.17+.018*z+2.25*np.exp(-.5*((z-16)/.3)**2))/(1+np.exp((z-16.22)/.09));pr/=pr.max()
ax.plot(z,ph,color="#286a99",lw=2.7,label="MV X rays (illustrative)");ax.plot(z,pr,color="#b94a38",lw=2.7,label="Narrow-energy protons (illustrative)")
ax.annotate("Secondary-electron\nbuildup",xy=(1.6,.98),xytext=(4.1,.82),arrowprops={"arrowstyle":"->","color":"#286a99"})
ax.annotate("Bragg peak",xy=(16,.99),xytext=(18.1,.86),arrowprops={"arrowstyle":"->","color":"#b94a38"})
ax.set(xlim=(0,23),ylim=(0,1.13),xlabel="Depth in water (cm; illustrative ranges)",ylabel="Dose / own beam maximum",title="Qualitative depth-dose shapes — not treatment-planning data");ax.grid(alpha=.16);ax.legend(loc="center right",fontsize=11)
labels=["Energy / range\nselection","Range modulator\nweighted energies","Scattering foils\nlateral flattening","Monitor chambers\nfluence / position","Aperture\nlateral contour","Compensator\ndistal contour","Target\nvolume"]
for i,label in enumerate(labels):
 x=i*1.55;bx.add_patch(FancyBboxPatch((x,.1),1.38,.72,boxstyle="round,pad=0.02",facecolor="#edf3f8" if i<6 else "#f6e5dd",edgecolor="#42687c",lw=1.2));bx.text(x+.69,.46,label,ha="center",va="center",fontsize=10)
 if i<6:bx.annotate("",xy=(x+1.54,.46),xytext=(x+1.39,.46),arrowprops={"arrowstyle":"->","lw":1.7,"color":"#42687c"})
bx.set(xlim=(-.1,10.8),ylim=(-.2,1.25),title="Passive proton beam modifiers: functional schematic (ordering varies)");bx.axis("off")
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=110)
plt.close(fig)
