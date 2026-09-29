"""Illustrative topographic circulation with parabolic basin depth.
Python 3.14; numpy 2.3.5; matplotlib 3.10.7. Writes basename PNG to cwd.
Solves a conservative diffusion / upwind advection discretization with zero
boundary transport streamfunction. The vanishing depth is an idealized limit.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def solve(n=100,r=.025,beta=.25,f0=1,F0=1e-3):
 dx=1/(n+1);x=np.arange(1,n+1)*dx;y=x.copy();X,Y=np.meshgrid(x,y)
 H=4*X*(1-X);Hp=4*(1-2*X);f=f0+beta*Y
 vx=-beta/H;vy=-f*Hp/H**2
 west=r/(4*(X-dx/2)*(1-X+dx/2))/dx**2+np.maximum(vx,0)/dx
 east=r/(4*(X+dx/2)*(1-X-dx/2))/dx**2+np.maximum(-vx,0)/dx
 south=r/H/dx**2+np.maximum(vy,0)/dx
 north=r/H/dx**2+np.maximum(-vy,0)/dx
 diag=west+east+south+north
 rhs=-F0*np.sin(2*np.pi*Y);a=np.zeros((n+2,n+2));mask=(np.indices((n,n)).sum(axis=0)%2)==0
 residual=1.
 for it in range(30000):
  for color in (mask,~mask):
   candidate=(rhs+west*a[1:-1,:-2]+east*a[1:-1,2:]+south*a[:-2,1:-1]+north*a[2:,1:-1])/diag
   inner=a[1:-1,1:-1];inner[color]=candidate[color]
  if it%100==0:
   res=diag*a[1:-1,1:-1]-west*a[1:-1,:-2]-east*a[1:-1,2:]-south*a[:-2,1:-1]-north*a[2:,1:-1]-rhs
   residual=float(np.max(np.abs(res)))
   if residual<1e-11:break
 assert residual<1e-10,(it,residual)
 return np.linspace(0,1,n+2),a,it,residual

if __name__=='__main__':
 x,psi,it,res=solve();X,Y=np.meshgrid(x,x)
 fig,(ax,bx)=plt.subplots(1,2,figsize=(9,3.5),dpi=120,facecolor='white')
 pos=np.max(psi);neg=-np.min(psi)
 levels=np.r_[-neg*np.array([.85,.6,.35,.1]),pos*np.array([.1,.35,.6,.85])]
 cs=ax.contour(X,Y,psi,levels=levels,colors=['#b4443b']*4+['#1765a1']*4,linestyles=['dashed']*4+['solid']*4,linewidths=1.25)
 ax.axhline(.5,color='#888',ls=':',lw=1);ax.text(.05,.51,'wind-curl zero',fontsize=8,color='#555')
 ax.set(xlabel='x / Lₓ',ylabel='y / Lᵧ',title='Transport streamfunction ψ\nred dashed: negative; blue solid: positive')
 xq=np.linspace(.07,.93,12);yq=np.linspace(.07,.93,11);QX,QY=np.meshgrid(xq,yq)
 H=4*QX*(1-QX);f=1+.25*QY;vx=-.25/H;vy=-f*4*(1-2*QX)/H**2;norm=np.hypot(vx,vy)
 bx.quiver(QX,QY,vx/norm,vy/norm,color='#444',scale=17,width=.004)
 xf=np.linspace(.025,.975,250)
 for Q in np.linspace(1.08,3.5,13):
  yf=(Q*4*xf*(1-xf)-1)/.25;yf[(yf<0)|(yf>1)]=np.nan;bx.plot(xf,yf,color='#81ad8a',lw=1)
 bx.set(xlim=(0,1),ylim=(0,1),xlabel='x / Lₓ',ylabel='y / Lᵧ',title='Pseudovelocity direction\nand background f/H contours')
 for panel in (ax,bx):panel.set_aspect('equal')
 fig.suptitle('Parabolic depth; illustrative r = 0.025, β = 0.25, f₀ = 1',fontsize=12)
 fig.tight_layout();fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
 print({'iterations':it,'discrete_residual':res,'psi_min':float(psi.min()),'psi_max':float(psi.max())})
