"""Original bilayer and director schematics; write PNG to the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 3, figsize=(12, 4.6), facecolor='white')
ax = axes[0]
for x in np.linspace(.1, .9, 9):
    for y, sign in [(.69, -1), (.31, 1)]:
        ax.add_patch(plt.Circle((x, y), .025, color='#247ba0'))
        for shift in [-.008, .008]:
            ax.plot([x+shift, x+shift+.012, x+shift], [y+sign*.03, y+sign*.12, y+sign*.17], color='#e59b35', lw=1.6)
ax.text(.5, .85, 'Water / polar heads', ha='center')
ax.text(.5, .50, 'Tail-rich core', ha='center', va='center', bbox={'facecolor':'white','edgecolor':'none','alpha':.8})
ax.text(.5, .14, 'Water / polar heads', ha='center')
ax.set_title('Lipid bilayer')
for i, field in zip([1,2], [False, True]):
    axes[i].remove()
    ax=fig.add_subplot(1,3,i+1,projection='3d')
    for z in [0,1]:
        corners=np.array([[-.25,-.25,z],[.25,-.25,z],[.25,.25,z],[-.25,.25,z],[-.25,-.25,z]])
        ax.plot(*corners.T,color='gray',lw=2)
    for z in np.linspace(0,1,11):
        phi=np.pi*z/2
        theta=(1.48*np.sin(np.pi*z)) if field else 0
        v=.16*np.array([np.cos(phi)*np.cos(theta),np.sin(phi)*np.cos(theta),np.sin(theta)])
        centre=np.array([0,0,z]);ends=np.stack([centre-v/2,centre+v/2])
        ax.plot(*ends.T,color='#8b3fa0',lw=3)
    ax.quiver(.32,.15,0,0,0,1,color='#ba3434',arrow_length_ratio=.09,lw=2)
    ax.text(.33,.15,.45,'Light + field' if field else 'Light',fontsize=8)
    ax.text(-.25,-.3,-.08,'Entrance: x',fontsize=9)
    ax.text(-.25,-.3,1.08,'Exit: y',fontsize=9)
    ax.set_title('High field: dark' if field else 'Low field: transmitting')
    ax.set(xlim=(-.35,.4),ylim=(-.35,.35),zlim=(-.1,1.15))
    ax.set_box_aspect((.7,.7,1.3));ax.view_init(elev=17,azim=-55);ax.set_axis_off()
axes[0].set(xlim=(0,1),ylim=(0,1));axes[0].axis('off')
fig.suptitle('Bilayer packing and twisted-nematic optical switching', fontsize=14)
fig.text(.5,.01,'Nematic panels: rods show the director; plate anchoring is retained at high field.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.04,1,.94))
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white')
plt.close(fig)
