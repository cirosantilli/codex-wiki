"""Original mathematical illustration; write the matching PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Rectangle,Circle
plt.rcParams.update({"font.size":11,"axes.titlesize":13,"figure.facecolor":"white","savefig.facecolor":"white"})
def save(fig):
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=150,facecolor="white")
    plt.close(fig)
fig,axs=plt.subplots(1,3,figsize=(12,4.4),layout='constrained');x=np.linspace(0,1,1000)
for idx,(ax,title) in enumerate(zip(axs,['Above eutectic: 200 °C','At eutectic: 138 °C','Below eutectic: 100 °C'])):
    if idx==0:
        gL=(x-.6)**2-.09
        # Construct exact common tangencies at (solid .02, liquid .33) and
        # (liquid .87, solid .98), rather than asserting empirical energies.
        q=20.;ml=2*(.33-.6);mr=2*(.87-.6)
        cb=.02-ml/q;cs=.98-mr/q
        vb=(.33-.6)**2-.09+ml*(.02-.33);vs=(.87-.6)**2-.09+mr*(.98-.87)
        gB=q/2*(x-cb)**2+vb-q/2*(.02-cb)**2
        gS=q/2*(x-cs)**2+vs-q/2*(.98-cs)**2
        contacts=[(.02,.33,ml,(.33-.6)**2-.09),(.87,.98,mr,(.87-.6)**2-.09)]
        # Each tuple supplies a known tangent point on the liquid branch.
        for lo,hi,m,g in contacts:
            xp=.33 if lo==.02 else .87;t=np.linspace(lo,hi,80)
            ax.plot(t,g+m*(t-xp),c='black',lw=2.5)
    else:
        b,s=(.03,.93) if idx==1 else (.01,.96)
        gB=10*(x-b)**2;gS=10*(x-s)**2;gL=(x-.61)**2+(0 if idx==1 else .035)
        ax.plot([b,s],[0,0],c='black',lw=2.5)
        if idx==1:ax.scatter([b,.61,s],[0,0,0],c='black',s=24,zorder=5)
    for y,c,label in [(gB,'#4878a5','Bi-rich solid'),(gL,'#c77720','Liquid'),(gS,'#779b43','Sn-rich solid')]:ax.plot(x,y,c=c,label=label)
    ax.set(xlim=(0,1),ylim=(-.13,.25),xlabel='Atomic fraction Sn',title=title);ax.set_yticks([])
axs[0].set_ylabel('Gibbs free energy (arbitrary scale)');axs[0].legend(fontsize=8,loc='upper center')
fig.suptitle('Constructed free-energy curves; black lines are coexistence tangents')
save(fig)
