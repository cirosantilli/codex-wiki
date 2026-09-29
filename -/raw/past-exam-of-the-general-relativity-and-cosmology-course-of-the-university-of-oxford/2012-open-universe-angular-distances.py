from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

fig,(ax,bx)=plt.subplots(1,2,figsize=(10.4,4.8),layout="constrained")
x=np.linspace(.001,2.3,500);ax.plot(x,np.sinh(x)/x,color="#286c94",lw=2.6,label="Open: sinh(x)/x");ax.plot(x,np.ones_like(x),color="#555555",lw=2,label="Flat: 1");ax.plot(x,np.sin(x)/x,color="#98619c",lw=2.3,label="Closed: sin(x)/x")
ax.set(xlabel=r"$\sqrt{|k|}\,D_C$",ylabel="Transverse / radial comoving distance",xlim=(0,2.3),ylim=(.25,2.2),title="Compare at fixed radial distance");ax.legend(fontsize=10,loc="upper left");ax.grid(alpha=.12)
z=np.linspace(0,8,700);ae=1/(1+z)
for om,col in [(0,"#286c94"),(.05,"#ba6d30"),(.3,"#8b59a2"),(1,"#4c8b63")]:
 ok=1-om
 if om==0:DC=np.log1p(z)
 elif om==1:DC=2*(1-np.sqrt(ae))
 else:DC=2/np.sqrt(ok)*(np.arcsinh(np.sqrt(ok/om))-np.arcsinh(np.sqrt(ok*ae/om)))
 DM=DC if ok==0 else np.sinh(np.sqrt(ok)*DC)/np.sqrt(ok)
 DA=DM/(1+z);bx.plot(z,DA,color=col,lw=2.4,label=fr"$\Omega_M={om:g}$")
bx.set(xlabel="Redshift z",ylabel=r"$H_0D_A/c$",xlim=(0,8),ylim=(0,.52),title="Dust + curvature; same present Hubble scale");bx.legend(fontsize=10,loc="lower right");bx.grid(alpha=.12)
fig.suptitle("Spatial curvature and expansion history both affect angular size",fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
