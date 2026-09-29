"""Original reciprocal-cube integral comparison with a unit-width rectangle."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

a=3
x=np.linspace(a,a+1,600)
fig,ax=plt.subplots(figsize=(6.7,4.5),layout="constrained")
ax.fill_between(x,0,a**-3,color="#999999",alpha=.2)
ax.plot(x,x**-3,color="#267ba6",lw=2,label=r"$x^{-3}$")
ax.plot(x,(x-1)**-3,color="#b3632b",lw=2,label=r"$(x-1)^{-3}$")
ax.hlines(a**-3,a,a+1,color="#444444",lw=1.7,label=r"Rectangle height $a^{-3}$")
ax.vlines([a,a+1],0,a**-3,color="#777777",lw=.8)
ax.set(xlim=(a-.05,a+1.05),ylim=(0,.135),xlabel="x",ylabel="Height",title="A decreasing curve between successive unit rectangles (a = 3)")
ax.set_xticks([a,a+1],labels=["a = 3","a + 1 = 4"])
ax.grid(alpha=.15);ax.legend(fontsize=10)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
