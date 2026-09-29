"""Original grey-layer flux accounting for the supplied stellar/planet data.
Python3.14/NumPy2.3/Matplotlib3.10. Output PNG basename to cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
Ts=312.;Teq=5000*np.sqrt(8.1e8/(2*1.1e11))*.95**.25
eff=(Teq/Ts)**4;ea=2*(1-eff);Ta=Ts/2**.25
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white"})
fig,ax=plt.subplots(figsize=(9,4.4),layout="constrained")
ax.add_patch(Rectangle((0,.06),1,.10,facecolor="#806647",edgecolor="0.3"))
ax.add_patch(Rectangle((0,.48),1,.13,facecolor="#d6e7ee",edgecolor="0.55"))
ax.text(.48,.10,rf"Surface: $T_s={Ts:g}\,$K; thermal flux $=1$",color="white",ha="center",va="center")
ax.text(.5,.55,rf"Grey atmosphere: $T_a={Ta:.1f}\,$K, $\epsilon_a={ea:.4f}$",ha="center",va="center")
ax.text(.5,.97,"Space",ha="center",va="center")
def arr(x,y0,y1,color):ax.annotate("",(x,y1),(x,y0),arrowprops={"arrowstyle":"->","lw":2.5,"color":color})
arr(.15,.16,.89,"#b76c15");ax.text(.13,.77,rf"Direct escape\n${1-ea:.4f}$".replace("\\n","\n"),ha="right",color="#8f5310")
arr(.42,.16,.48,"#b76c15");ax.text(.40,.29,rf"Absorbed\n${ea:.4f}$".replace("\\n","\n"),ha="right",color="#8f5310")
arr(.69,.61,.89,"#b2322b");ax.text(.67,.74,rf"Layer to space\n${ea/2:.4f}$".replace("\\n","\n"),ha="right",color="#a12c26")
arr(.69,.48,.16,"#b2322b");ax.text(.71,.29,rf"Back radiation\n${ea/2:.4f}$".replace("\\n","\n"),ha="left",color="#a12c26")
arr(.94,.90,.16,"#b6a011");ax.text(.92,.82,rf"Absorbed sunlight\n${eff:.4f}$".replace("\\n","\n"),ha="right",color="#8d7a0b")
ax.set(xlim=(-.05,1.05),ylim=(0,1.05));ax.axis("off")
fig.suptitle(r"One-layer fluxes normalized by $\sigma T_s^4$: surface, layer and space budgets balance")
fig.savefig("paper-1-ap2013-greenhouse-fluxes.png",dpi=140,facecolor="white",bbox_inches="tight")
