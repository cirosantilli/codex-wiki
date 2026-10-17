"""Original Argand diagram of 1+i and both square roots; output to cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

root = np.sqrt(1+1j)
fig, ax = plt.subplots(figsize=(6.0, 5.0), layout="constrained")
theta = np.linspace(0,2*np.pi,600)
for radius,color in [(np.sqrt(2),"#6b91aa"),(2**0.25,"#bc9270")]:
    ax.plot(radius*np.cos(theta),radius*np.sin(theta),ls="--",lw=1,color=color)
for z,color,label,offset in [(1+1j,"#246fa3",r"$1+i$",(12,13)),(root,"#bd5727",r"$z_+$",(13,-2)),(-root,"#bd5727",r"$z_-$",(-25,-20))]:
    ax.plot([0,z.real],[0,z.imag],color=color,lw=1.5)
    ax.scatter([z.real],[z.imag],color=color,s=36,zorder=4)
    ax.annotate(label,(z.real,z.imag),xytext=offset,textcoords="offset points",fontsize=12)
for radius,angle,color in [(0.48,np.pi/4,"#246fa3"),(0.8,np.pi/8,"#bd5727")]:
    t=np.linspace(0,angle,80)
    ax.plot(radius*np.cos(t),radius*np.sin(t),color=color,lw=1.4)
ax.text(0.42,0.33,r"$\pi/4$",fontsize=10,color="#246fa3")
ax.text(0.84,0.19,r"$\pi/8$",fontsize=10,color="#bd5727")
ax.axhline(0,color="black",lw=0.7);ax.axvline(0,color="black",lw=0.7)
ax.set(xlim=(-1.7,1.7),ylim=(-1.6,1.6),xlabel="Real part",ylabel="Imaginary part",title="Square roots halve the argument and take the square root of the modulus")
ax.set_title("The two square roots of $1+i$")
ax.set_aspect("equal");ax.grid(alpha=0.2)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
