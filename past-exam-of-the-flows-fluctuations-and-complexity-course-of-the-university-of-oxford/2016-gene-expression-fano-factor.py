"""Original scientific figure; Python 3.14 with numpy/matplotlib. Writes one PNG in the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","savefig.facecolor":"white"})
def save(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white",transparent=False,metadata={"Software":"Matplotlib"})
    plt.close(fig)

b=np.linspace(0,10,600);phi=.05;F=1+b/(1+phi)
fig,ax=plt.subplots(figsize=(7,4.3),layout="constrained")
ax.plot(b,F,color="#165b91",lw=2,label="exact: 1 + b / (1 + phi)")
ax.plot(b,1+b,color="#777777",ls="--",label="short-RNA approximation: 1 + b")
ax.axhline(1,color="#bf5a13",ls=":",label="Poisson Fano factor = 1")
ax.plot(0,1,"o",mfc="white",mec="#165b91",ms=7,clip_on=False)
ax.set(xlabel="b = translation rate / RNA removal rate",ylabel="Protein Fano factor",title="RNA lifetime / protein lifetime = 0.05",xlim=(0,10),ylim=(.5,11.4));ax.grid(alpha=.2);ax.legend(fontsize=9)
fig.supxlabel("The intercept is the limit from positive mean; at exactly zero production the ratio is undefined.",fontsize=9)
save(fig)
