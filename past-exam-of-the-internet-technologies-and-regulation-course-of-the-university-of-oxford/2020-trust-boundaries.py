"""Original schematic; Python 3.14.4 / Matplotlib 3.10.7. Output PNG to CWD.
The diagrams show chosen trust endpoints, not a measured network topology.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10})
fig,ax=plt.subplots(figsize=(8,4.6),dpi=100,facecolor="white")
ax.set_xlim(0,10);ax.set_ylim(0,6);ax.axis("off")
blue="#2166ac";green="#22744a";orange="#a85a12"
def box(x,y,w,label,edge,fill="#ffffff"):
 p=FancyBboxPatch((x-w/2,y-.34),w,.68,boxstyle="round,pad=.035,rounding_size=.07",ec=edge,fc=fill,lw=1.4,zorder=3)
 ax.add_patch(p);ax.text(x,y,label,ha="center",va="center",fontsize=9.5,zorder=4)
def wire(x1,x2,y):
 ax.add_patch(FancyArrowPatch((x1,y),(x2,y),arrowstyle="->",mutation_scale=11,lw=1.3,color=blue,zorder=1))
def channel(x1,x2,y,label,color=green):
 ax.annotate("",(x2,y),(x1,y),arrowprops={"arrowstyle":"<->","lw":1.5,"color":color})
 ax.text((x1+x2)/2,y+.13,label,color=color,ha="center",va="bottom",fontsize=9.4)
ax.text(.15,5.78,"A. Origin is the remote TLS endpoint",fontweight="bold",fontsize=11)
y=4.68
for x,w,t,e in [(1.1,1.5,"Browser",green),(3.5,1.55,"IP router",blue),(6.0,1.55,"IP router",blue),(8.8,1.55,"Origin",green)]:box(x,y,w,t,e)
for a,b in [(1.85,2.69),(4.31,5.19),(6.81,7.98)]:wire(a,b,y)
channel(1.1,8.8,5.2,"One authenticated encrypted channel")
ax.text(5,3.96,"Forwarders do not hold the TLS traffic keys in this model.",ha="center",fontsize=9.3)
ax.plot([.1,9.9],[3.56,3.56],color="#bbbbbb",lw=.8)
ax.text(.15,3.25,"B. A provider-authorised CDN edge terminates TLS",fontweight="bold",fontsize=11)
y=2.15
for x,w,t,e,f in [(1.1,1.5,"Browser",green,"white"),(3.5,1.55,"Address\ntranslator",blue,"white"),(6.,1.55,"CDN edge",orange,"#fff1df"),(8.8,1.55,"Origin",green,"white")]:box(x,y,w,t,e,f)
for a,b in [(1.85,2.69),(4.31,5.19),(6.81,7.98)]:wire(a,b,y)
channel(1.1,6,2.69,"TLS channel 1");channel(6,8.8,2.69,"TLS channel 2")
ax.text(6,1.43,"The edge can process plaintext.",ha="center",color=orange,fontsize=9.3)
ax.text(5,.76,"Address translation alone need not decrypt the TLS payload.",ha="center",fontsize=9.3)
ax.text(5,.23,"Many edge locations can share one operator: physical replication is not independent control.",ha="center",fontsize=8.6)
fig.subplots_adjust(left=.015,right=.985,top=.99,bottom=.015)
fig.savefig(Path.cwd()/"2020-trust-boundaries.png",dpi=100,facecolor="white",transparent=False,metadata={"Software":"codex-wiki Matplotlib"})
plt.close(fig)
