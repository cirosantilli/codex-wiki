"""Original muon-decay diagram; save basename in cwd."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(8,4),layout="constrained")
ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
def fermion(a,b,label,reverse=False,dy=.06):
 ax.plot([a[0],b[0]],[a[1],b[1]],color="#183a56",lw=2)
 p,q=np.array(a),np.array(b)
 if reverse:p,q=q,p
 ax.annotate("",xy=p+.64*(q-p),xytext=p+.45*(q-p),arrowprops={"arrowstyle":"-|>","color":"#183a56","lw":1.6})
 m=(np.array(a)+np.array(b))/2;ax.text(m[0],m[1]+dy,label,ha="center",fontsize=14)
v=(.33,.48);w=(.65,.35)
fermion((.06,.48),v,r"$\mu^-$")
fermion(v,(.90,.86),r"$\nu_\mu$")
fermion(w,(.94,.47),r"$e^-$")
fermion(w,(.94,.10),r"$\bar\nu_e$",True,-.10)
p=np.array(v);q=np.array(w);t=np.linspace(0,1,400);d=q-p;n=np.array([-d[1],d[0]])/np.linalg.norm(d)
xy=p[:,None]+d[:,None]*t+.013*n[:,None]*np.sin(14*np.pi*t)
ax.plot(*xy,color="#a13d23",lw=2);ax.text(.46,.46,r"$W^{-*}$",fontsize=14,color="#a13d23")
ax.plot([v[0],w[0]],[v[1],w[1]],"o",color="black",ms=5)
ax.text(.50,.02,r"$|q^2|\ll M_W^2$: replace exchange by a local Fermi interaction",ha="center",fontsize=12)
fig.savefig("paper-1-muon-decay.png",dpi=150,facecolor="white")
