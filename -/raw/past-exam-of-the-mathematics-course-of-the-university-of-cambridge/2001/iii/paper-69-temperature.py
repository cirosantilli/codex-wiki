"""Fixed-charge RN temperature. Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7.
Only emit paper-69-temperature.png to the caller's CWD; honor MPLCONFIGDIR.
"""
from pathlib import Path
import os
import tempfile
if not os.environ.get("MPLCONFIGDIR"):
    os.environ["MPLCONFIGDIR"] = tempfile.mkdtemp(prefix="paper-69-mpl-")
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
def temperature(x):
    d=np.sqrt(x*x-1)
    return d/(2*np.pi*(x+d)**2)
xx=np.r_[np.linspace(1,1.3,800),np.linspace(1.3,7,1200)]
peak_x=2/np.sqrt(3)
peak_y=1/(6*np.sqrt(3)*np.pi)
fig,ax=plt.subplots(figsize=(8.4,5),layout="constrained")
ax.plot(xx,temperature(xx),lw=2.2,color="#1565a3")
ax.scatter([1,peak_x],[0,peak_y],color="#1565a3",s=28,zorder=5)
ax.axhline(peak_y*1.09,ls="--",color="#8a5d00",lw=1.5)
ax.text(3.1,peak_y*1.09+0.0006,
        r"Example threshold $m|Q|\geq1/(6\sqrt{3}\pi)$",fontsize=10,color="#8a5d00")
ax.annotate(r"Maximum: $M/|Q|=2/\sqrt{3}$"+"\n"+r"$|Q|T=1/(6\sqrt{3}\pi)$",
            (peak_x,peak_y),(2.35,peak_y*.67),fontsize=11,
            arrowprops={"arrowstyle":"->","color":"#444444"})
ax.annotate("Extremal endpoint\n"+r"$M=|Q|,\ T=0$",(1,0),(2.15,peak_y*.12),
            fontsize=10,arrowprops={"arrowstyle":"->","color":"#444444"})
ax.annotate("",(4.2,float(temperature(4.2))),(5.7,float(temperature(5.7))),
            arrowprops={"arrowstyle":"->","color":"#1565a3","lw":2})
ax.text(4.35,0.011,"Evaporation: decreasing mass",fontsize=10)
ax.annotate("",(1.025,float(temperature(1.025))),
            (1.095,float(temperature(1.095))),
            arrowprops={"arrowstyle":"->","color":"#1565a3","lw":1.6})
ax.set_xlim(.95,7);ax.set_ylim(-.0005,peak_y*1.25)
ax.set_xlabel(r"Mass $M/|Q|$",fontsize=12)
ax.set_ylabel(r"Temperature $|Q|T$",fontsize=12)
ax.set_title("Reissner–Nordström temperature at fixed nonzero charge",fontsize=13)
ax.grid(alpha=.2)
fig.savefig(Path.cwd()/"paper-69-temperature.png",dpi=125,
            facecolor="white",transparent=False)
plt.close(fig)
