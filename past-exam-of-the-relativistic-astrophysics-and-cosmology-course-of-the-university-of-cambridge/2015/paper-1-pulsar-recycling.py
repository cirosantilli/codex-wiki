"""Original conditional evolutionary flow diagram, not source artwork."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
fig,ax=plt.subplots(figsize=(10,4.3),layout="constrained")
ax.set(xlim=(0,11),ylim=(0,5));ax.axis("off")
def box(x,y,label,color="#dceaf4"):
    ax.add_patch(FancyBboxPatch((x,y),2.7,.85,boxstyle="round,pad=0.07",facecolor=color,edgecolor="#40556b"))
    ax.text(x+1.35,y+.425,label,ha="center",va="center",fontsize=10)
def arrow(a,b,label=None):
    ax.annotate("",b,a,arrowprops=dict(arrowstyle="->",lw=1.7,color="#40556b"))
    if label: ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.16,label,ha="center",fontsize=9)
box(.35,3.3,"Core collapse:\nmagnetized neutron star")
box(4.15,3.3,"Rotation-powered pulsar:\nbeam may cross observer")
box(7.95,3.3,"Spin-down:\nradio activity may cease")
arrow((3.12,3.73),(4.05,3.73))
arrow((6.92,3.73),(7.85,3.73))
box(.35,.9,"Surviving binary:\ncompanion transfers matter","#f5e8d7")
box(4.15,.9,"Accreting X-ray binary:\nangular momentum spins up","#f5e8d7")
box(7.95,.9,"Accretion declines:\nrecycled radio pulsar","#f5e8d7")
arrow((3.12,1.33),(4.05,1.33))
arrow((6.92,1.33),(7.85,1.33))
arrow((9.3,3.2),(1.7,1.85))
ax.text(5.4,2.4,"Only with a suitable binary and mass-transfer history",ha="center",fontsize=10,color="#885c2b",bbox=dict(facecolor="white",edgecolor="none",pad=3))
ax.text(5.5,.25,"Radio silence is an emission state; the neutron star remains.",ha="center",fontsize=10)
fig.suptitle("Ordinary spin-down and the optional accretion-recycling route")
fig.savefig("paper-1-pulsar-recycling.png",dpi=155,facecolor="white")
