"""Original decay diagrams. Python 3.14, NumPy and Matplotlib; output to cwd."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({"font.size":11,"savefig.facecolor":"white"})
fig,axs=plt.subplots(2,2,figsize=(11,7),layout="constrained")
def line(ax,a,b,label="",reverse=False,style="-",dy=.04):
 ax.plot([a[0],b[0]],[a[1],b[1]],style,color="#16334c",lw=1.8)
 if style=="-":
  p=np.array(a);q=np.array(b)
  if reverse:p,q=q,p
  ax.annotate("",xy=p+.64*(q-p),xytext=p+.45*(q-p),arrowprops={"arrowstyle":"-|>","color":"#16334c","lw":1.5})
 if label:
  mid=(np.array(a)+np.array(b))/2
  ax.text(mid[0],mid[1]+dy,label,ha="center",va="bottom")
def wavy(ax,a,b,label):
 a=np.array(a);b=np.array(b);v=b-a;t=np.linspace(0,1,450);normal=np.array([-v[1],v[0]])/np.linalg.norm(v)
 xy=a[:,None]+v[:,None]*t+.012*normal[:,None]*np.sin(16*np.pi*t)
 ax.plot(*xy,color="#a83826",lw=1.7)
 mid=(a+b)/2;ax.text(mid[0],mid[1]+.055,label,color="#8b2e1f",ha="center")
def dot(ax,p):ax.add_patch(Circle(p,.013,color="black",zorder=5))
for ax in axs.flat:ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
ax=axs[0,0];v=(.38,.48);w=(.64,.48)
line(ax,(.10,.78),v,r"$c$");line(ax,(.10,.18),v,r"$\bar c$",True,dy=-.12)
wavy(ax,v,w,r"$\gamma^*$")
line(ax,w,(.92,.78),r"$\mu^-$");line(ax,w,(.92,.18),r"$\mu^+$",True,dy=-.12)
dot(ax,v);dot(ax,w);ax.set_title(r"(i) $J/\psi$: electromagnetic annihilation",fontsize=12)
ax.text(.12,.92,"Color-singlet bound state",fontsize=10)
ax=axs[0,1];v=(.48,.48)
wavy(ax,(.08,.48),v,r"$W^+$")
line(ax,v,(.90,.80),r"$\nu_e$");line(ax,v,(.90,.17),r"$e^+$",True,dy=-.12);dot(ax,v)
ax.set_title("(ii) Elementary charged-current vertex",fontsize=12)
ax=axs[1,0];v=(.48,.48)
line(ax,(.08,.48),v,r"$\Delta^{++}\ (uuu)$")
line(ax,v,(.91,.80),r"$p\ (uud)$")
line(ax,v,(.91,.17),r"$\pi^+\ (u\bar d)$",style="--",dy=-.12)
ax.add_patch(Circle(v,.036,facecolor="#a83826",edgecolor="black",zorder=5))
ax.text(.5,.01,r"Effective strong vertex: creation of $d\bar d$",ha="center",fontsize=10)
ax.set_title("(iii) Composite hadron decay",fontsize=12)
ax=axs[1,1];v=(.30,.48);w=(.58,.35)
line(ax,(.05,.48),v,r"$\tau^-$")
line(ax,v,(.80,.83),r"$\nu_\tau$")
wavy(ax,v,w,r"$W^{-*}$")
line(ax,w,(.92,.49),r"$d$");line(ax,w,(.92,.13),r"$\bar u$",True,dy=-.12)
ax.plot([.95,.97,.97,.95],[.08,.08,.55,.55],color="black")
ax.text(.88,.67,r"$d\bar u\to\pi^-$",ha="center",fontsize=10)
dot(ax,v);dot(ax,w);ax.set_title("(iv) Weak decay followed by pion formation",fontsize=12)
fig.savefig("paper-1-decay-diagrams.png",dpi=150)
