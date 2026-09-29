"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,3,figsize=(11,3.6),layout='constrained');x=np.linspace(0,1,250)
for ax,pinch in zip(axs[:2],[False,True]):
 w=.22+.18*x if not pinch else np.minimum(.25+.85*x,1)
 ax.fill_between(x,1-w,1,color='thistle');ax.fill_between(x,-1,-1+w,color='thistle')
 ax.plot([0,1,1,0,0],[-1,-1,1,1,-1],color='0.35');ax.plot(x,1-w,color='tab:purple');ax.plot(x,-1+w,color='tab:purple')
 ax.text(-.03,0,'Source',ha='right',va='center');ax.text(1.03,0,'Drain',va='center');ax.text(.5,1.12,'Gate: p+ region',ha='center');ax.text(.5,-1.23,'Reverse-biased gate',ha='center');ax.annotate('Electrons',(.7,0),(.22,0),ha='center',va='center',arrowprops=dict(arrowstyle='->',color='tab:blue'),color='tab:blue')
 ax.text(.34,.78,'Depletion',ha='center',fontsize=9);ax.set(xlim=(-.28,1.3),ylim=(-1.5,1.5),title='Drain-end pinch-off' if pinch else 'Open neutral channel');ax.axis('off')
 if pinch:ax.annotate('High field',(.94,.05),(.66,-.72),fontsize=8,arrowprops=dict(arrowstyle='->'))
v=np.linspace(0,2,500)
for vg in [0,-.3,-.6]:
 vp=1+vg;r=v/vp;isat=(1+vg)**2;current=np.where(r<1,isat*(2*r-r*r),isat*(1+.025*(v-vp)))
 axs[2].plot(v,current,label=rf'$V_{{GS}}/|V_{{off}}|={vg:g}$')
axs[2].set(xlabel=r'$V_{DS}/|V_{off}|$',ylabel=r'$I_D/I_{DSS}$',title='Approximate output characteristics');axs[2].grid(alpha=.2);axs[2].legend(fontsize=8)
fig.suptitle('Original schematic n-channel JFET: pinch-off allows saturated current; full gate depletion cuts it off')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
