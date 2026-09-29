"""Original teaching diagram. Tested with Python 3.14, numpy, matplotlib.
Run in the desired output directory; PNG is written as a basename in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

f=np.linspace(0,.94,600)
fig,ax=plt.subplots(figsize=(7,4.5),layout="constrained")
ax.plot(f,1/(1-f),lw=2,color="#326a97",label="total maximum displacement / Y")
ax.plot(f,f/(1-f),lw=2,color="#b77327",label="additional maximum displacement / Y")
ax.axvline(1,ls="--",color="#aa3939");ax.text(.75,13,"linear-model pole\nat Euler load",fontsize=10)
ax.set(xlim=(0,1.06),ylim=(0,16),xlabel="Compressive load F / Fc",ylabel="Midspan displacement / Y",title="Sinusoidal imperfection amplifies continuously below buckling")
ax.grid(alpha=.2);ax.legend(loc="upper left",fontsize=9)
fig.savefig("paper-1-imperfect-beam.png",dpi=155,facecolor="white")
