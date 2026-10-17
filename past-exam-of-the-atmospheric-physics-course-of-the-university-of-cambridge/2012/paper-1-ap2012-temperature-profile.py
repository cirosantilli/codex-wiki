"""Original teaching plot. Python3.14,NumPy2.3.5,Matplotlib3.10.7. PNG basename written to cwd."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

z=np.array([0,12,50,85,120]);temp=np.array([288,216,270,190,500])
fig,ax=plt.subplots(figsize=(6.7,5.6),layout='constrained')
regions=[(0,12,'Troposphere','#e7eff5'),(12,50,'Stratosphere','#f8f0df'),(50,85,'Mesosphere','#eef3e7'),(85,120,'Thermosphere','#f2e9f4')]
for lo,hi,label,color in regions:ax.axhspan(lo,hi,color=color);ax.text(430 if label=='Thermosphere' else 390,93 if label=='Thermosphere' else (lo+hi)/2,label,ha='center',va='center',fontsize=10)
ax.plot(temp,z,color='#285e88',lw=2.6);ax.scatter(temp,z,color='#285e88',s=24,zorder=3)
ax.set(xlim=(160,530),ylim=(0,120),xlabel='Temperature (K; schematic)',ylabel='Height (km; schematic)',title='Illustrative atmospheric temperature structure');ax.grid(alpha=.15)
fig.savefig(Path(__file__).stem+'.png',dpi=150,facecolor='white');plt.close(fig)
