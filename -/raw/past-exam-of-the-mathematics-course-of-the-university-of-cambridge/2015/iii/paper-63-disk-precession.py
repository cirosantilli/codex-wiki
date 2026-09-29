from pathlib import Path
import os
import tempfile
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "codex-wiki-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 10, "savefig.facecolor": "white"})

wp=4.1193613*np.exp(1j*np.deg2rad(76.04384315));t=np.linspace(0,2*np.pi,400)
fig,axes=plt.subplots(1,2,figsize=(8.5,3.6),dpi=100,facecolor='white')
for ax,offset,title in [(axes[0],wp,'Relative to the initial disk plane'),(axes[1],0,'Relative to the planet plane')]:
 circle=offset-wp*np.exp(-1j*t);ax.plot(circle.real,circle.imag,color='#65758b',lw=1.4)
 if offset:
  ax.scatter([wp.real],[wp.imag],color='#ca551b',marker='x',s=50,label='Forced planetary tilt')
  ax.scatter([0],[0],color='black',s=20,label='Initial disk')
 else:ax.scatter([0],[0],color='#ca551b',marker='x',s=50,label='Planet plane')
 for r,color in [(1,'#b52b35'),(1.4,'#d69b16'),(2,'#1269a8'),(3,'#308341')]:
  phase=4*r**(-3.5);w=offset-wp*np.exp(-1j*phase)
  ax.scatter([w.real],[w.imag],color=color,s=30,label=rf'$a/a_{{\rm in}}={r}$')
  z=offset-wp*np.exp(-1j*np.array([phase,phase+.13]));ax.annotate('',xy=(z[1].real,z[1].imag),xytext=(z[0].real,z[0].imag),arrowprops={'arrowstyle':'->','color':color})
 ax.set(xlabel=r'$I\cos\Omega$ (degrees)',ylabel=r'$I\sin\Omega$ (degrees)',title=title);ax.set_aspect('equal');ax.grid(alpha=.18);ax.legend(fontsize=7,loc='lower right')
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-63-disk-precession.png',dpi=100,facecolor='white')
