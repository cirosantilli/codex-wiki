"""Original bilateral Fourier-response sketch.
Python 3.14, NumPy 2.3, SciPy 1.16 and Matplotlib 3.10; PNG is written to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq


def y(t):
    t=np.asarray(t)
    return np.where(t<0,-np.exp(2*t)/18,(t/3-5/9)*np.exp(-t)+np.exp(-2*t)/2)

minimum=brentq(lambda t:8/9-t/3-np.exp(-t),0,.5)
maximum=brentq(lambda t:8/9-t/3-np.exp(-t),2,8/3)
zero=brentq(lambda t:t/3-5/9+np.exp(-t)/2,1,2)
t=np.linspace(-3.2,8,2000)
fig,ax=plt.subplots(figsize=(8.4,4.2),facecolor="white")
ax.axvspan(-3.2,0,color="#edf2f7",alpha=1)
ax.axhline(0,color="#7b838e",lw=.8);ax.axvline(0,color="#7b838e",lw=.8)
ax.plot(t,y(t),color="#245b80",lw=2)
ax.plot(0,-1/18,"o",color="#245b80",ms=4)
ax.annotate(r"$y(0)=-1/18$",(0,-1/18),(-2.6,-.067),arrowprops={"arrowstyle":"->","color":"#5d6673"},fontsize=10)
for root,offset in [(minimum,(18,-12)),(maximum,(35,-20))]:
    ax.plot(root,float(y(root)),"o",color="#b44d27",ms=4)
    ax.annotate(fr"$t\simeq{root:.3f}$",(root,float(y(root))),xytext=offset,textcoords="offset points",fontsize=10)
ax.plot(zero,0,"o",color="#b44d27",ms=4)
ax.annotate(fr"zero at $t\simeq{zero:.3f}$",(zero,0),xytext=(14,12),textcoords="offset points",fontsize=10)
ax.text(-2.5,-.018,r"$t<0:\ -e^{2t}/18$",fontsize=11)
ax.set(xlim=(-3.2,8),ylim=(-.077,.039),xlabel=r"$t$",ylabel=r"$y(t)$",title="Decay at both temporal infinities allows a negative-time response")
ax.spines[["top","right"]].set_visible(False)
ax.grid(axis="y",alpha=.15)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=145,facecolor="white")
plt.close(fig)
print(f"minimum t={minimum:.9f}, y={float(y(minimum)):.9f}; zero t={zero:.9f}; maximum t={maximum:.9f}, y={float(y(maximum)):.9f}")
