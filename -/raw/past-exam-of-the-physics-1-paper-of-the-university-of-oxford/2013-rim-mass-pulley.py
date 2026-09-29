"""Original coordinate schematic from the supplied CP1 geometry.
Python 3.14, numpy 2.3.5, matplotlib 3.10.7. Outputs only CWD basename PNG.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Arc
fig,ax=plt.subplots(figsize=(5.5,4.6),layout='constrained',facecolor='white')
ax.add_patch(Circle((0,0),1,fill=False,lw=2,color='#333333'))
ax.plot([0,0],[-1.55,0],color='#555555',lw=2)
ax.plot([-.6,.6],[-1.55,-1.55],color='#555555',lw=2)
r=.18;top=1.8
ax.add_patch(Circle((1+r,top),r,fill=False,lw=1.8,color='#333333'))
ax.plot([1+r,1+r],[top,2.2],color='#555555',lw=2)
ax.plot([.75,1.65],[2.2,2.2],color='#555555',lw=2)
ax.plot([1,1],[0,top],color='#333333',lw=1.6)
arc=np.linspace(0,np.pi,80);ax.plot(1+r+r*np.cos(arc),top+r*np.sin(arc),color='#333333',lw=1.6)
ax.plot([1+2*r,1+2*r],[top,.65],color='#333333',lw=1.6)
ax.add_patch(Circle((1+2*r,.55),.11,color='#4c8cba'))
ax.text(1+2*r+.18,.55,r'$m$',va='center',fontsize=14)
theta=np.deg2rad(38);xm,ym=np.sin(theta),-np.cos(theta)
ax.add_patch(Circle((xm,ym),.11,color='#c96f2b'))
ax.text(xm+.16,ym-.03,r'$M$',fontsize=14)
ax.plot([0,xm],[0,ym],color='#b76125',lw=1.4)
ax.plot([0,0],[0,-1.13],ls='--',color='#888888',lw=1)
ax.add_patch(Arc((0,0),.8,.8,theta1=-90,theta2=-52,color='#b76125',lw=1.3))
ax.text(.16,-.57,r'$\theta$',fontsize=13)
ax.text(.15,-.3,r'$R$',fontsize=13)
ax.annotate('',xy=(.88,1.22),xytext=(.88,.75),arrowprops=dict(arrowstyle='->',color='#27678e',lw=1.6))
ax.text(.55,1.03,'String rises',rotation=90,ha='center',va='center',fontsize=9)
ax.annotate('',xy=(1.9,.25),xytext=(1.9,.9),arrowprops=dict(arrowstyle='->',color='#27678e',lw=1.6))
ax.text(2.03,.57,r'$+R\theta$',va='center',fontsize=12)
ax.text(0,-1.91,'Fixed guide pulley; string grips the rim',ha='left',fontsize=10)
ax.set(xlim=(-1.23,2.6),ylim=(-2,2.35),aspect='equal');ax.axis('off')
fig.savefig('2013-rim-mass-pulley.png',dpi=150,facecolor='white',metadata={'Software':'Matplotlib'})
