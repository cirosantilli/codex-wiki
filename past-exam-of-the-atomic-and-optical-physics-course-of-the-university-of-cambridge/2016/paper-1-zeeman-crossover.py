"""Original spectrum calculation. Python3.14/NumPy/Matplotlib; output cwd."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,3,figsize=(13,4.8),layout="constrained")
colors={1.5:"#274e82",.5:"#bc5429",-.5:"#288969",-1.5:"#87529a"}
x=np.linspace(0,.18,200)
for J,g,base,ms in [(1.5,4/3,.5,[-1.5,-.5,.5,1.5]),(.5,2/3,-1,[-.5,.5])]:
 for m in ms:
  e=base+g*m*x
  axs[0].plot(x,e,color=colors[m],lw=1.8)
  axs[0].text(.184,e[-1],rf"$J={J:g},m={m:g}$",fontsize=8,va="center")
axs[0].set(xlim=(0,.34),ylim=(-1.2,1),xlabel=r"$x/\beta=\mu_BB/\beta$",ylabel=r"$(E_P-E_P^{(0)})/\beta$",title="Weak-field P levels")
axs[0].text(.01,.83,r"$g_{3/2}=4/3;\quad g_{1/2}=2/3$",fontsize=10)
x=np.linspace(0,4,500)
for m in [-1.5,1.5]:axs[1].plot(x,.5+np.sign(m)*2*x,color=colors[m],lw=1.8)
for m in [-.5,.5]:
 for sign in [-1,1]:
  e=m*x-.25+sign*.5*np.sqrt(x*x+2*m*x+2.25)
  axs[1].plot(x,e,color=colors[m],ls="-" if sign==1 else "--",lw=1.8)
for ml,ms in [(-1,-.5),(-1,.5),(0,-.5),(0,.5),(1,-.5),(1,.5)]:
 e=x*(ml+2*ms)+ml*ms
 axs[1].plot(x[x>2],e[x>2],":",color=".35",lw=1)
 y=e[-1]
 if ml==-1 and ms==.5:y+=.45
 if ml==1 and ms==-.5:y-=.45
 axs[1].text(4.05,y,rf"$({ml},{ms:g})$",fontsize=8,va="center")
axs[1].set(xlim=(0,5.2),ylim=(-8.1,9),xlabel=r"$x/\beta$",ylabel=r"$(E_P-E_P^{(0)})/\beta$",title="Exact P levels and high-field limits")
axs[1].text(.08,.96,r"End labels: $(m_L,m_S)$",transform=axs[1].transAxes,va="top",fontsize=9)
axs[2].plot(x,x,color="#bc5429",label=r"$m_S=+1/2$")
axs[2].plot(x,-x,color="#288969",label=r"$m_S=-1/2$")
axs[2].set(xlabel=r"$x/\beta$",ylabel=r"$(E_S-E_S^{(0)})/\beta$",title="S levels: no spin-orbit term")
axs[2].legend(fontsize=10)
for ax in axs:ax.axvline(0,color=".5",lw=.6);ax.grid(alpha=.2)
fig.savefig("paper-1-zeeman-crossover.png",dpi=150,facecolor="white")
