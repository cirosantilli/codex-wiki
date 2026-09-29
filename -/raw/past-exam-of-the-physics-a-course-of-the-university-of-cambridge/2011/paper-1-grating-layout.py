"""Original pedagogical figure; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run from the destination directory: output is the script's basename PNG in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})
fig,ax=plt.subplots(figsize=(9,3),layout='constrained')
ax.axhline(0,c='0.75',ls='--',lw=.7)
for x,label in [(2,'Collimating lens'),(6,'Imaging lens')]:
 ax.annotate('',xy=(x,1.1),xytext=(x,-1.1),arrowprops={'arrowstyle':'<->','lw':2,'color':'#176493'});ax.text(x,-1.35,label,ha='center')
ax.plot([4,4],[-1.05,1.05],c='k',lw=4);ax.text(4,-1.35,'Grating',ha='center')
ax.plot([8,8],[-1.05,1.05],c='0.3',lw=2);ax.text(8,-1.35,'Focal screen',ha='center')
for y in [-.45,0,.45]:
 ax.plot([0,2,4,6,8],[0,y,y,y+.5,.5],c='#b64b24',lw=1)
ax.plot(0,0,'ko');ax.text(0,-.3,'Point source\nat front focus',ha='center')
ax.plot(8,.5,'o',c='#b64b24');ax.text(8.12,.5,r'$x=f\tan\theta$',va='center')
ax.annotate('',xy=(6,-.85),xytext=(8,-.85),arrowprops={'arrowstyle':'<->'});ax.text(7,-.78,r'$f$',ha='center')
ax.text(2.95,.85,'Plane illumination',ha='center');ax.text(5.1,.9,r'Order $m$',ha='center',color='#b64b24')
ax.set(xlim=(-.7,9.45),ylim=(-1.65,1.3));ax.axis('off')
fig.savefig("paper-1-grating-layout.png", dpi=165, facecolor="white", bbox_inches="tight")
plt.close(fig)
