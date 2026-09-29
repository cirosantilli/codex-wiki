"""Finite-drag point-source contours, original mathematical rendering.
Python 3.14; numpy 2.3.5; matplotlib 3.10.7. Output: basename PNG in cwd.
K0 evaluated by its real integral; no scipy dependency.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def k0(z):
 t=np.linspace(0,10,801);value=np.zeros_like(z,dtype=float)
 for i in range(len(t)-1):
  value+=(np.exp(-z*np.cosh(t[i]))+np.exp(-z*np.cosh(t[i+1])))*(t[i+1]-t[i])/2
 return value

if __name__=='__main__':
 x=np.linspace(-12,4,401);y=np.linspace(-5,5,251);X,Y=np.meshgrid(x,y)
 R=np.maximum(np.hypot(X,Y),.022);response=np.exp(-X/2)*k0(R/2)
 fig,ax=plt.subplots(figsize=(9,10/3),dpi=120,facecolor='white')
 levels=[.05,.1,.2,.4,.8,1.6,3.2]
 cs=ax.contour(X,Y,response,levels=levels,colors='#1765a1',linewidths=1.2)
 ax.clabel(cs,fmt='%g',inline=True,fontsize=8,manual=[(.6,0),(-.9,1.2),(-3,2),(-8,3),(-10,4)])
 ax.plot(0,0,'o',color='#ae452c',ms=5)
 ax.annotate('point source',xy=(0,0),xytext=(1.35,2.6),arrowprops={'arrowstyle':'->','color':'#333'},fontsize=10)
 ax.text(-8,-4.2,'western wake',color='#1765a1');ax.annotate('',xy=(-8,-3.3),xytext=(-5.8,-3.3),arrowprops={'arrowstyle':'->','color':'#1765a1','lw':2})
 ax.set(xlabel='(x − x₀) / ℓ',ylabel='(y − y₀) / ℓ',title='Finite-drag response: contours of −2πr ψ / H,  ℓ = r/β')
 ax.set_aspect('equal');ax.spines[['top','right']].set_visible(False)
 fig.tight_layout();fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
