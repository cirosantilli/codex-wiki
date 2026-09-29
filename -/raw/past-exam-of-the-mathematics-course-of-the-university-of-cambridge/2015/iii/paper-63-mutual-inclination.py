from pathlib import Path
import os
import tempfile
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "codex-wiki-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 10, "savefig.facecolor": "white"})

Id=np.deg2rad(87);dO=np.deg2rad(4);ip=np.linspace(85,95,501);ir=np.deg2rad(ip)
im=np.rad2deg(np.arccos(np.cos(Id)*np.cos(ir)+np.sin(Id)*np.sin(ir)*np.cos(dO)))
approx=np.sqrt((ip-87)**2+4**2)
fig,ax=plt.subplots(figsize=(6.6,3.4),dpi=100,facecolor='white')
ax.plot(ip,im,color='#1269a8',label='Exact normal-vector formula')
ax.plot(ip,approx,ls='--',color='#ca551b',label='Second-order approximation')
ax.scatter([88],[4.1193613],color='black',s=24,zorder=5)
ax.annotate('Observed planet: (88, 4.119)',xy=(88,4.1193613),xytext=(89,5.1),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.axvline(86.99268774,color='gray',ls=':',lw=1)
ax.set(xlabel='Planet sky-plane inclination (degrees)',ylabel='Mutual inclination (degrees)',title='Different nodes prevent an exactly coplanar orbit',xlim=(85,95),ylim=(3.5,9.5))
ax.grid(alpha=.18);ax.legend(fontsize=8);fig.tight_layout()
fig.savefig(Path.cwd()/'paper-63-mutual-inclination.png',dpi=100,facecolor='white')
