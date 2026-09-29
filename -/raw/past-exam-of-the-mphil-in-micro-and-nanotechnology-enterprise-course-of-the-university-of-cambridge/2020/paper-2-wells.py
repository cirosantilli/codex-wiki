"""Original normalized quantum-well models; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-.55,1.55,5000);inside=(x>=0)&(x<=1)
# Units L=1 and hbar^2/(2m)=1; exterior barrier V0=100.
z0=5.;finite=[]
for n in range(3):
 lo=n*np.pi/2+1e-9;hi=min((n+1)*np.pi/2-1e-9,z0-1e-9)
 def fun(z):return (z*np.tan(z) if n%2==0 else -z/np.tan(z))-np.sqrt(z0*z0-z*z)
 for _ in range(100):
  mid=(lo+hi)/2
  if fun(lo)*fun(mid)<=0:hi=mid
  else:lo=mid
 z=(lo+hi)/2;k=2*z;kap=2*np.sqrt(z0*z0-z*z);y=x-.5
 f=np.cos(k*y) if n%2==0 else np.sin(k*y)
 edge=np.cos(z) if n%2==0 else np.sin(z)
 f=np.where(np.abs(y)<=.5,f,edge*np.exp(-kap*(np.abs(y)-.5))*(1 if n%2==0 else np.sign(y)))
 f/=np.sqrt(np.trapezoid(f*f,x));finite.append((k*k,f))
fig,axs=plt.subplots(2,2,figsize=(11,8),layout="constrained")
for ax,mode in zip(axs[0],["infinite","finite"]):
 for n in range(1,4):
  e,f=(n*n*np.pi*np.pi,np.where(inside,np.sqrt(2)*np.sin(n*np.pi*x),0)) if mode=="infinite" else finite[n-1]
  ax.hlines(e,0,1,colors="gray",linestyles=":",lw=.7)
  ax.plot(x,e+3*f,label=f"n={n}, E={e:.2f}")
 ax.vlines([0,1],0,105,colors="k",lw=1.5)
 if mode=="finite":ax.hlines([100,100],[-.55,1],[0,1.55],colors="k",lw=2)
 ax.set(xlim=(-.4,1.4),ylim=(0,110),xlabel=r"$x/L$",ylabel="energy + scaled wavefunction",title=f"{'A' if mode=='infinite' else 'B'}  {mode.capitalize()} well")
 ax.legend(fontsize=9,loc="upper right")
ax=axs[1,0];inf=np.where(inside,2*np.sin(2*np.pi*x)**2,0)
ax.plot(x,inf,label="infinite barrier");ax.plot(x,finite[1][1]**2,label="finite barrier")
for b in [0,1]:ax.axvline(b,color="gray",ls=":")
ax.set(xlim=(-.4,1.4),xlabel=r"$x/L$",ylabel=r"$L|\psi_2|^2$",title="C  Second-state probability densities");ax.legend(fontsize=9)
ax=axs[1,1];r=np.linspace(0,2,700)
# Qualitative central section of a nodeless envelope, with finite exterior tails.
bare=np.where(r<=1,np.cos(.95*r),np.cos(.95)*np.exp(-1.2*(r-1)))
core=np.where(r<=1,np.cos(.95*r),np.cos(.95)*np.exp(-3.8*(r-1)))
shell=np.where(r<=1,np.cos(.85*r),np.cos(.85)*np.exp(-2.8*(r-1)))
ax.axvspan(1,1.55,color="lightgray",alpha=.5,label="shell");ax.axvline(1,color="gray",ls=":")
ax.plot(r,bare,label="chosen weak bare barrier");ax.plot(r,core,label="core-shell electron");ax.plot(r,shell,ls="--",label="core-shell hole")
ax.text(.18,.15,"core");ax.set(xlabel=r"$r/R_{\rm core}$",ylabel="relative envelope amplitude",title="D  Conditional type-I envelope sketch",ylim=(0,1.05));ax.legend(fontsize=8)
fig.savefig("paper-2-wells.png",dpi=155,facecolor="white")

