"""Original explanatory diagram; Python 3.14, numpy and matplotlib (root pyproject)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Ellipse
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})

x=np.linspace(-0.65,1.8,700)
fa=np.where(x<0,-2.5*x-0.18,-0.18*np.exp(-3*x))
fr=np.where(x<0.4,-2.5*x-0.18,0.)
fig,ax=plt.subplots(figsize=(8,4.6))
ax.plot(x,fa,label='approach',color='#2171b5',lw=2)
ax.plot(x,fr,label='withdrawal',color='#d95f0e',lw=2)
mask=(x>0)&(x<.4)
ax.fill_between(x,fa,fr,where=mask,color='#fdd0a2',alpha=.7,label='hysteresis area: dissipated work')
ax.annotate('',xy=(.4,-1.18),xytext=(.4,0),arrowprops={'arrowstyle':'<->','color':'#993404','lw':1.6})
ax.text(.47,-.68,'pull-off force\n(magnitude)',color='#993404')
ax.annotate('contact branch',xy=(-.4,.82),xytext=(-.25,1.32),arrowprops={'arrowstyle':'->'})
ax.text(.85,.15,'separated probe')
ax.axhline(0,color='0.5',lw=.8)
ax.set(xlabel='Imposed separation (arbitrary units)',ylabel='Force (arbitrary units)',title='Adhesive contact: force and energy are different observables',ylim=(-1.45,1.65))
ax.legend(loc='upper right',fontsize=9)
fig.tight_layout()
fig.savefig("paper-1-afm-contact.png", dpi=170, bbox_inches="tight", facecolor="white")
plt.close(fig)
