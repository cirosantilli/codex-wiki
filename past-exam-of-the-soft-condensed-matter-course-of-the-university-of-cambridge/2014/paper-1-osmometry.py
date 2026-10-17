"""Original explanatory figure. Python 3.14, numpy and matplotlib.
Output is a PNG basename in cwd; no source figures or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,a=plt.subplots(figsize=(6,3.7),layout='constrained');c=np.array([.02,.04,.06,.08]);P=np.array([4.,8.6,13.8,19.6]);x=np.linspace(0,.09,200);a.plot(x,185+750*x,label='Derived linear regression');a.scatter(c,P/c,color='#c33c29',zorder=3,label='Reduced input data');a.scatter([0],[185],color='black',s=25);a.annotate('intercept 185',(0,185),(.025,190),arrowprops=dict(arrowstyle='->'),fontsize=9);a.set(xlabel='Mass concentration (kg m⁻³)',ylabel='Π/c (Pa m³ kg⁻¹)',title='Temperature still needed to convert intercept to molar mass');a.legend(frameon=False,fontsize=8)
fig.savefig('paper-1-osmometry.png',dpi=150);plt.close(fig)
