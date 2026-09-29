"""Original explanatory figure; Python 3.14 and root pyproject dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white","axes.facecolor":"white"})

def p_of_v(v,t):return 8*t/(3*v-1)-3/v**2

def coexist(t):
 roots=np.roots([4*t,-9,6,-1]);s=sorted(z.real for z in roots if abs(z.imag)<1e-8 and z.real>1/3)
 assert len(s)==2
 pmin=p_of_v(s[0],t);pmax=p_of_v(s[1],t);lo=max(pmin,0.);hi=pmax;eps=(hi-lo)*1e-7;lo+=eps;hi-=eps
 def area(p):
  r=np.roots([3*p,-(p+8*t),9,-3]);v=sorted(z.real for z in r if abs(z.imag)<1e-7 and z.real>1/3);assert len(v)==3
  vl,vg=v[0],v[-1];A=8*t/3*np.log((3*vg-1)/(3*vl-1))+3*(1/vg-1/vl)-p*(vg-vl)
  return A,vl,vg
 assert area(lo)[0]>0 and area(hi)[0]<0
 for _ in range(65):
  mid=(lo+hi)/2
  if area(mid)[0]>0:lo=mid
  else:hi=mid
 p=(lo+hi)/2;A,vl,vg=area(p);return p,vl,vg
fig,(ax,bx)=plt.subplots(1,2,figsize=(9,4),layout="constrained");v=np.linspace(.4,5,1500)
for t,col in [(.85,"#1565c0"),(1.,"#777"),(1.12,"#d84315")]:ax.plot(v,p_of_v(v,t),label=f"T/Tc = {t:g}",color=col,lw=1.8)
pstar,vl,vg=coexist(.85);vv=np.linspace(vl,vg,500);pp=p_of_v(vv,.85);ax.fill_between(vv,pp,pstar,where=pp>=pstar,color="#66bb6a",alpha=.4);ax.fill_between(vv,pp,pstar,where=pp<pstar,color="#ef5350",alpha=.4);ax.plot([vl,vg],[pstar,pstar],color="#222",lw=2);ax.scatter([vl,vg],[pstar,pstar],color="#222",s=18)
ax.set(xlabel=r"Molar volume $v/v_c$",ylabel=r"Pressure $p/p_c$",xlim=(.4,5),ylim=(0,1.8),title="Equal areas select coexistence");ax.legend(fontsize=8)
Ts=np.linspace(.72,.997,85);Ps=np.array([coexist(t)[0] for t in Ts]);bx.plot(Ts,Ps,color="#1565c0",lw=2);bx.plot([Ts[-1],1],[Ps[-1],1],color="#1565c0",lw=2);bx.scatter([1],[1],color="#d84315");bx.annotate("Critical point",(1,1),xytext=(.8,1.2),arrowprops={"arrowstyle":"->"},fontsize=9);bx.text(.79,.87,"Liquid",fontsize=11);bx.text(.94,.27,"Gas",fontsize=11);bx.text(1.035,1.2,"Fluid",fontsize=9,ha="center");bx.set(xlabel=r"Temperature $T/T_c$",ylabel=r"Coexistence pressure $p/p_c$",xlim=(.72,1.1),ylim=(.05,1.35),title="Fluid model: no solid or triple point")
for a in (ax,bx):a.grid(alpha=.15)

fig.savefig(Path(__file__).stem+".png",dpi=150,facecolor="white",bbox_inches="tight")
plt.close(fig)
