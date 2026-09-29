"""Original reflected-price curve. Python3.14, NumPy, Matplotlib. Output CWD."""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
from math import erf,sqrt,log,exp
rate,vol,tau,B,K=.05,.25,1,100,120
def call(s):
 d1=(log(s/K)+(rate+.5*vol*vol)*tau)/(vol*sqrt(tau));d2=d1-vol*sqrt(tau)
 phi=lambda z:.5*(1+erf(z/sqrt(2)))
 return s*phi(d1)-K*exp(-rate*tau)*phi(d2)
s=np.linspace(B,220,500);ce=np.array([call(x)for x in s])
image=np.array([(x/B)**(1-2*rate/vol**2)*call(B*B/x)for x in s])
fig,ax=plt.subplots(figsize=(7,4.5),facecolor="white")
ax.plot(s,ce,color="#2166ac",lw=2,label="European call")
ax.plot(s,image,color=".45",ls="--",lw=1.5,label="reflected image term")
ax.plot(s,ce-image,color="#b2182b",lw=2,label="down-and-out call, still alive")
ax.axvline(B,color=".4",ls=":");ax.scatter([B],[0],color="#b2182b",s=35)
ax.set(xlabel="current stock S",ylabel="option price",title="Subtracting the image enforces zero value at the barrier")
ax.legend(frameon=False);ax.spines[["top","right"]].set_visible(False)
ax.text(128,70,"B=100, K=120, r=0.05,\nvolatility=0.25, remaining time=1",fontsize=9)
fig.tight_layout();fig.savefig("2007-barrier-reflection.png",dpi=150,facecolor="white")
