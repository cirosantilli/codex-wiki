"""Original scalar knife-edge calculation, including spherical spreading."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
z,w=np.polynomial.legendre.leggauss(240)
def transmission(d):
    d=np.asarray(d);u=.5*np.sqrt(20*(.2+1/d))
    q=(z+1)*u[...,None]/2
    integ=(np.exp(1j*np.pi*q*q/2)*w).sum(axis=-1)*u/2
    return np.abs((.5+.5j)-integ)**2/2
d=np.geomspace(.12,45,900);tr=transmission(d);init=float(transmission(45));absolute=tr/(5+d)**2/(init/50**2)
fig=plt.figure(figsize=(10,6),layout="constrained")
gs=fig.add_gridspec(2,2,height_ratios=[.8,1])
ax=fig.add_subplot(gs[0,:]);ax.set(xlim=(-1,51),ylim=(4.3,6.2));ax.axis("off")
ax.plot([0,50],[5,5],"--",color=".5")
ax.plot([0,5,50],[5,5.5,5],color="#b2602c")
ax.add_patch(Rectangle((4.8,4.3),.4,1.2,facecolor="#8e9ca8"))
ax.plot([0,50],[5,5],"o",color="#245d84")
ax.plot(5,5.5,"o",color="#b2602c",ms=4)
for x,lab in [(0,"S"),(5,"O"),(50,"P")]:ax.text(x,4.85,lab,ha="center")
ax.text(2.5,5.1,"a = 5 m",ha="center",fontsize=9)
ax.text(27.5,5.1,"b = 45 m initially",ha="center",fontsize=9)
ax.text(6.2,5.62,"Q at x = h = 0.5 m above direct ray",fontsize=9)
ax.set_title("Long opaque fence: one transverse knife edge; ground reflection omitted")
ax=fig.add_subplot(gs[1,0]);ax.plot(d,tr,color="#245d84",lw=2)
ax.plot(45,init,"o",color="#b2602c")
ax.set(xlabel="Receiver distance d from fence (m)",ylabel=r"$I_{\rm fence}/I_{\rm free}(d)$",title="Transmission ratio falls toward fence")
bx=fig.add_subplot(gs[1,1]);bx.plot(d,absolute,color="#245d84",lw=2)
j=np.argmax(absolute);bx.plot(d[j],absolute[j],"o",color="#b2602c")
bx.annotate(f"Peak near {d[j]:.2f} m",xy=(d[j],absolute[j]),xytext=(13,14),arrowprops=dict(arrowstyle="->"),fontsize=9)
bx.set(xlabel="Receiver distance d from fence (m)",ylabel="Absolute intensity / initial intensity",title="Absolute signal includes inverse-square gain")
for a in [ax,bx]:
    a.axvspan(0,.5,color=".8",alpha=.6)
    a.grid(alpha=.2)
fig.suptitle("Paraxial prediction; shaded d < 0.5 m is outside its reliable geometry")
fig.savefig("paper-2-fence-diffraction.png",dpi=150,facecolor="white")
