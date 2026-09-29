"""Original forced-pendulum and response curves; save basename to cwd."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,(ax,bx)=plt.subplots(1,2,figsize=(10,3.5),layout="constrained")
t=np.linspace(0,4*np.pi,900);y=(2*np.sin(t)-np.sin(2*t))/3
ax.plot(t,y,lw=2,color="#245d84")
for tx,yy in [(2*np.pi/3,np.sqrt(3)/2),(4*np.pi/3,-np.sqrt(3)/2)]:
    ax.plot(tx,yy,"o",color="#af572e")
ax.axhline(0,color=".6",lw=.7)
ax.set(xticks=[0,np.pi,2*np.pi,3*np.pi,4*np.pi],xticklabels=["0",r"$\pi$",r"$2\pi$",r"$3\pi$",r"$4\pi$"],xlabel=r"$\omega_0 t$",ylabel=r"$m\omega_0^2x/F_0$",title=r"Initial rest; drive $\omega=2\omega_0$")
ax.annotate(r"Peak $=\sqrt{3}/2$",xy=(2*np.pi/3,np.sqrt(3)/2),xytext=(4,.65),arrowprops=dict(arrowstyle="->"),fontsize=9)
q=np.linspace(.7,1.3,700);gam=.04
exact=1/np.sqrt((1-q*q)**2+(2*gam*q)**2)
approx=1/(2*np.sqrt((q-1)**2+gam*gam))
bx.plot(q,exact,color="#245d84",label="Exact")
bx.plot(q,approx,"--",color="#b2602c",label="Near-resonant")
bx.set(xlabel=r"$\omega/\omega_0$",ylabel=r"$m\omega_0^2|R|$",title=r"$\gamma/\omega_0=0.04$")
for a in (ax,bx):a.grid(alpha=.2)
bx.legend()
fig.savefig("paper-2-driven-response.png",dpi=150,facecolor="white")
