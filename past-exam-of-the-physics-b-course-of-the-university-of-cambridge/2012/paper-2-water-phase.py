"""Original explanatory figure; Python 3.14 with NumPy and Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(figsize=(7.2,4.7),layout='constrained');t=np.linspace(0,1,200);tp=np.array([1.,1.3])
ax.plot(t,1.3*t*t,color='#537c9e',lw=2,label='sublimation')
z=np.linspace(0,1,200);ax.plot(1-.18*z,1.3+2.7*z,color='#397567',lw=2,label='melting: negative slope')
ax.plot(1+2.6*z,1.3+2.1*z**.8,color='#ab7444',lw=2,label='vaporization')
ax.plot(*tp,'ko');ax.annotate('triple point\n273.16 K, 612 Pa',xy=tp,xytext=(1.35,.62),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.plot(3.6,3.4,'ko',ms=4);ax.text(2.75,3.62,'critical point',fontsize=9)
ax.text(.19,2.25,'solid',fontsize=13);ax.text(1.55,2.7,'liquid',fontsize=13);ax.text(2.7,.9,'vapour',fontsize=13)
ax.set(xlim=(-.1,4),ylim=(-.1,4.1),xticks=[],yticks=[],xlabel='temperature (schematic)',ylabel='pressure (schematic)',title='Ordinary-water phase topology, not to scale');ax.legend(loc='upper left',fontsize=8)

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
