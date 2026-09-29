"""Original explanatory figure; run under Python 3.14 with numpy and matplotlib.
Writes its PNG basename to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white","savefig.facecolor":"white"})
fig,ax=plt.subplots(figsize=(8,4.6),layout="constrained")
theta=np.deg2rad(28);t=np.tan(theta);u=np.array([np.cos(theta),np.sin(theta)])
A=np.array([1.,0.]);B=np.array([0.,t]);C=np.array([1.,2*t]);D=A+np.dot(C-A,u)*u
for x in [0,1]:ax.plot([x,x],[-.9,1.65],color="slategray",lw=5,alpha=.6)
ax.plot([-.65,1],[-1.65*t,0],color="#1766a5",lw=2)
ax.plot([1,0,1],[0,t,2*t],color="#1766a5",lw=2)
for Q in [A,C]:
 E=Q+1.4*u;ax.annotate('',E,Q,arrowprops=dict(arrowstyle='->',color='#1766a5',lw=2))
ax.plot([A[0],D[0]],[A[1],D[1]],color='#c33c29',lw=4)
v=(D-C)/np.linalg.norm(D-C)
W1=C-.18*v;W2=D+.42*v
ax.plot([W1[0],W2[0]],[W1[1],W2[1]],'--',color='#38934c')
ax.text(1.45,1.26,'common outgoing\nwavefront',color='#28733a')
for label,Q,offset in [('A',A,(-.04,-.18)),('B',B,(-.13,.06)),('C',C,(-.05,.10)),('D',D,(.08,-.04))]:
 ax.plot(*Q,'o',color='black',ms=4);ax.text(*(Q+offset),label)
ax.annotate('',(1,-.62),(0,-.62),arrowprops=dict(arrowstyle='<->'))
ax.text(.48,-.8,'d');ax.text(.3,.15,r'$d/\cos\theta$',rotation=-28,color='#1766a5')
ax.text(.42,.88,r'$d/\cos\theta$',rotation=28,color='#1766a5')
ax.text(1.65,-.2,r'$AD=2d\tan\theta\sin\theta$',color='#c33c29')
ax.plot([1,1.7],[0,0],':',color='gray');ang=np.linspace(0,theta,40)
ax.plot(1+.48*np.cos(ang),.48*np.sin(ang),color='black');ax.text(1.53,.07,r'$\theta$')
ax.set(xlim=(-.4,2.9),ylim=(-.85,1.75),aspect='equal',title='Compare optical paths at the same wavefront')
ax.axis('off');fig.savefig('paper-2-fabry-perot.png',dpi=170);plt.close(fig)
