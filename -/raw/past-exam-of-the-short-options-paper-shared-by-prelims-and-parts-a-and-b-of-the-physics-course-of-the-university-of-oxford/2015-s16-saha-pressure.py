from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

k=1.380649e-23;me=9.1093837e-31;h=6.62607015e-34;R=13.6*1.602176634e-19;T=np.linspace(1000,20000,1800)
S=(2*np.pi*me*k*T)**1.5/h**3*np.exp(-R/(k*T))
fig,(ax,bx)=plt.subplots(1,2,figsize=(10.3,4.8),layout="constrained")
N=1e20;x=2/(1+np.sqrt(1+4*N/S));P=N*k*T*(1+x)
ax.plot(T/1000,P,lw=2.6,color="#246c94",label="Saha + ideal gas");ax.plot(T/1000,N*k*T,ls=":",color="#777777",label="Neutral limit");ax.plot(T/1000,2*N*k*T,ls="--",color="#9b6b31",label="Ionized limit")
i=np.argmax(np.gradient(P,T));ax.plot(T[i]/1000,P[i],"o",color="#246c94");ax.annotate("Steepest slope\nnear 9.25 × 10³ K",xy=(T[i]/1000,P[i]),xytext=(1.8,37),arrowprops={"arrowstyle":"->"},fontsize=11)
ax.set(xlabel="Temperature (10³ K)",ylabel="Gas pressure (Pa)",xlim=(0,20),ylim=(0,57),title=r"Conserved nucleus density $N=10^{20}$ m$^{-3}$");ax.grid(alpha=.16);ax.legend(fontsize=10,loc="lower right")
for N,col in [(1e20,"#246c94"),(1e21,"#b94a38")]:
 x=2/(1+np.sqrt(1+4*N/S));bx.plot(T/1000,x,color=col,lw=2.6,label=r"$N=10^{%d}$ m$^{-3}$"%round(np.log10(N)))
bx.annotate("Higher density delays\nionization",xy=(10.6,.65),xytext=(12.4,.35),arrowprops={"arrowstyle":"->"},fontsize=11)
bx.set(xlabel="Temperature (10³ K)",ylabel="Ionized fraction",xlim=(0,20),ylim=(0,1.05),title="Density dependence of the crossover");bx.grid(alpha=.16);bx.legend(fontsize=10,loc="lower right")
fig.suptitle("Ground-state hydrogen in thermodynamic equilibrium (calculated curves)",fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
