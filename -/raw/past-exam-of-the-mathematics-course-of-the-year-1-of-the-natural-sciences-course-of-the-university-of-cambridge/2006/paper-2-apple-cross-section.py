"""Original cardioid meridian and horizontal disk slice, not an angular wedge."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

theta=np.linspace(0,np.pi,800)
radius=1-np.cos(theta)
horizontal=radius*np.sin(theta)
vertical=radius*np.cos(theta)
outline=np.column_stack([np.r_[horizontal,-horizontal[::-1]],
                         np.r_[vertical,vertical[::-1]]])
fig,ax=plt.subplots(figsize=(7.4,6.0),layout="constrained")
shape=Polygon(outline,facecolor="#eef4f8",edgecolor="#245b9f",lw=2)
ax.add_patch(shape)
lower=theta>=np.pi/2
lower_shape=Polygon(np.column_stack([np.r_[horizontal[lower],-horizontal[lower][::-1]],
                                    np.r_[vertical[lower],vertical[lower][::-1]]]),
                    facecolor="#f5dfbe",edgecolor="none")
ax.add_patch(lower_shape)
angle=2*np.pi/3
upper_z=(1-np.cos(angle))*np.cos(angle)
lower_z=(1-np.cos(angle+.07))*np.cos(angle+.07)
slice_patch=ax.axhspan(lower_z,upper_z,color="#d09438",alpha=.7)
slice_patch.set_clip_path(shape)
ax.axhline(0,color="0.4",lw=.8)
ax.axvline(0,color="0.4",lw=.8)
ax.plot(np.r_[horizontal,-horizontal[::-1]],np.r_[vertical,vertical[::-1]],
        color="#245b9f",lw=1.8)
ax.plot([0,1,-1,0],[0,0,0,-2],"o",color="#245b9f",ms=4)
ax.annotate(r"$\theta=0$: cusp",xy=(0,0),xytext=(.15,.38),
            arrowprops={"arrowstyle":"->","lw":.8},fontsize=10)
ax.annotate(r"$\theta=\pi/2$",xy=(1,0),xytext=(1.07,.14),fontsize=10)
ax.annotate(r"$\theta=\pi$",xy=(0,-2),xytext=(.15,-2.12),fontsize=10)
ax.annotate("",xy=(1.43,upper_z),xytext=(1.43,lower_z),
            arrowprops={"arrowstyle":"<->","lw":1})
ax.text(1.48,(upper_z+lower_z)/2,r"$|dz|$",va="center",fontsize=10)
ax.text(-.86,-.8,"horizontal slice",fontsize=10)
ax.set(aspect="equal",xlim=(-1.65,1.9),ylim=(-2.22,.6),xlabel=r"$y/a$",ylabel=r"$z/a$",
       title=r"Apple meridian: $r/a=1-\cos\theta$")
ax.grid(alpha=.12)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
