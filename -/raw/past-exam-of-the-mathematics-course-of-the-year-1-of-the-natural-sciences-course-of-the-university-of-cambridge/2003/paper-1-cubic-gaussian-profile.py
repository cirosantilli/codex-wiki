"""Original cubic Gaussian curve, showing its stationary flat crossing."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-3.5,3.5,1300);f=x**3/3*np.exp(-1.5*x*x)
height=np.exp(-1.5)/3
fig,ax=plt.subplots(figsize=(7.1,4.4),layout="constrained")
ax.plot(x,f,color="#287da5",lw=2)
ax.axhline(0,color="#777777",lw=.8);ax.axvline(0,color="#777777",lw=.8)
ax.scatter([-1,0,1],[-height,0,height],color=["#ad6730","#704d91","#ad6730"],zorder=5,s=32)
ax.annotate("Global minimum",xy=(-1,-height),xytext=(-3.1,-.084),arrowprops=dict(arrowstyle="->",color="#555555"),fontsize=10)
ax.annotate("Global maximum",xy=(1,height),xytext=(1.55,.083),arrowprops=dict(arrowstyle="->",color="#555555"),fontsize=10)
ax.annotate("Stationary inflection",xy=(0,0),xytext=(-2.9,.039),arrowprops=dict(arrowstyle="->",color="#555555"),fontsize=10)
ax.set(xlim=(-3.5,3.5),ylim=(-.1,.1),xlabel="x",ylabel="f(x)",title=r"$f(x)=\frac{x^3}{3}\,e^{-3x^2/2}$")
ax.grid(alpha=.14)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
