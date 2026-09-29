"""Original far-field interference for amplitudes(1/2,1,1/2), spacing5lambda."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

u=np.linspace(-1,1,3001);intensity=(1+np.cos(10*np.pi*u))**2
fig,ax=plt.subplots(figsize=(10,4.8),dpi=100,facecolor="white")
ax.plot(u,intensity,lw=2.2,color="#285d89");maxima=np.arange(-5,6)/5;zeros=np.arange(-9,10,2)/10
ax.scatter(maxima,np.full_like(maxima,4),s=20,color="#285d89",zorder=3)
ax.scatter(zeros,np.zeros_like(zeros),s=18,color="#a04c35",zorder=3)
ax.annotate(r"Maxima at $u=m/5$",xy=(.4,4),xytext=(.05,4.6),arrowprops={"arrowstyle":"->"},fontsize=11)
ax.annotate(r"Zeros at $u=(2m+1)/10$",xy=(.7,0),xytext=(.24,1.35),arrowprops={"arrowstyle":"->"},fontsize=11)
ax.set(xlabel=r"Direction $u=\sin\theta$",ylabel=r"Intensity $I/I_0$",xlim=(-1.025,1.025),ylim=(-.2,5.1),title="Outer-slit amplitude weighting removes secondary maxima")
ax.set_xticks(np.linspace(-1,1,11));ax.grid(alpha=.2)
fig.text(.5,.025,r"$I_0$: central slit alone; slit width envelope omitted in the narrow-slit model.",ha="center",fontsize=11)
fig.subplots_adjust(left=.08,right=.98,top=.87,bottom=.18)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white")
