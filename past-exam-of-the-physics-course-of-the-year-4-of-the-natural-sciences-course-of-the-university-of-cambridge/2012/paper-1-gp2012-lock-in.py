"""Original functional optical-modulation and synchronous-detection diagram."""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
fig, ax = plt.subplots(figsize=(11, 4.5), facecolor='white', layout='constrained')
ax.set(xlim=(0, 12), ylim=(0, 4.6)); ax.axis('off')
def box(x,y,w,h,text,color='#e8f0f7'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.05',edgecolor='#26455f',facecolor=color))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=11)
def arrow(a,b,style='-'):
    ax.annotate('',b,a,arrowprops=dict(arrowstyle='->',color='#26455f',linestyle=style,lw=1.4))
box(.15,2.6,1.15,.75,'Wanted\nsource'); box(1.75,2.6,1.1,.75,'Chopper'); box(3.35,2.6,2.25,.75,'Slits + scanning\ngrating'); box(6.15,2.6,1.5,.75,'Photodiode\n+ preamp')
for a,b in [((1.35,2.975),(1.7,2.975)),((2.9,2.975),(3.3,2.975)),((5.65,2.975),(6.1,2.975))]: arrow(a,b)
box(8.2,2.6,1.2,.75,'Multiply'); box(9.95,2.6,1.75,.75,'Low-pass\n+ readout')
arrow((7.7,2.975),(8.15,2.975)); arrow((9.45,2.975),(9.9,2.975))
box(1.65,.55,2.3,.7,'Shared phase reference', '#fff3df'); arrow((2.3,2.55),(2.3,1.3),'--')
ax.plot([4,8.8],[.9,.9],color='#26455f',ls='--',lw=1.4); arrow((8.8,.9),(8.8,2.55),'--')
ax.text(5.8,3.9,'Stray light / dark-current noise',ha='center',fontsize=11,color='#9a4f0c'); arrow((6.9,3.7),(6.9,3.4))
ax.text(6.6,.28,'Coherent wanted modulation survives averaging; unmodulated offsets do not.',ha='center',fontsize=11)
ax.set_title('Chopped-source spectral detection',fontsize=15,pad=12)
fig.savefig('paper-1-gp2012-lock-in.png', dpi=160, facecolor='white')
plt.close(fig)
