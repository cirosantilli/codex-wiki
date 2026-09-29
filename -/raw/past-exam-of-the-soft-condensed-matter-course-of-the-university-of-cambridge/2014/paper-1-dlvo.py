"""Original explanatory figure. Python 3.14, numpy and matplotlib.
Output is a PNG basename in cwd; no source figures or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,a=plt.subplots(figsize=(7,3.8),layout='constrained');x=np.geomspace(.025,7,1400)
for k,col,lab in [(.4,'#1766a5','lower screening'),(2,'#c78124','intermediate screening'),(8,'#c33c29','higher screening')]:
 U=12*np.exp(-k*x)-1.3/x+.002*(.08/x)**12;a.plot(x,U,color=col,label=lab)
a.axhline(0,color='gray',ls=':');a.set(xlim=(0,5),ylim=(-5,9),xlabel='Surface separation (chosen units)',ylabel='Potential / kBT (schematic)',title='Chosen DLVO-like curves; short-range core added');a.legend(frameon=False,fontsize=9);a.text(2.4,6.2,'Salt shortens the repulsive range',fontsize=10)
fig.savefig('paper-1-dlvo.png',dpi=150);plt.close(fig)
