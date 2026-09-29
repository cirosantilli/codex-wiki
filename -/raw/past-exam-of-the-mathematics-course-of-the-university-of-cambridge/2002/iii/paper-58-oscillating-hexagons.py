"""Original real-amplitude portrait; integrate the cyclic normal form, output to CWD."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def main():
 mu=4.2;h=(1+np.sqrt(1+20*mu))/10;r=np.sqrt(mu)
 def f(t,y):return np.array([mu*y[i]+y[(i+1)%3]*y[(i+2)%3]-y[i]**3-4*y[(i+1)%3]**2*y[i] for i in range(3)])
 sol=solve_ivp(f,(0,140),[h+.015,h-.006,h-.009],rtol=1e-10,atol=1e-12,max_step=.025,dense_output=True)
 fig=plt.figure(figsize=(8,5.6),layout='constrained');ax=fig.add_subplot(111,projection='3d')
 transient=sol.sol(np.linspace(0,100,6000));ax.plot(*transient,color='#adb5bd',lw=.7,alpha=.65,label='approaching trajectory')
 cycle=sol.sol(np.linspace(125,125+1,1500));ax.plot(*cycle,color='#17659d',lw=2,label='attracting cycle')
 for t in [125.12,125.39,125.67]:
  y=sol.sol(t);v=f(t,y);v=.15*v/np.linalg.norm(v);ax.quiver(*y,*v,color='#17659d',arrow_length_ratio=.45,lw=1.4)
 ax.scatter([h],[h],[h],marker='x',color='#b34b25',s=70,label='unstable hexagon')
 for i in range(3):
  p=np.zeros(3);p[i]=r;ax.scatter(*p,marker='x',color='#7d3c98',s=50,label='unstable rolls' if i==0 else None)
  off=np.zeros(3);off[i]=.06;ax.text(*(p+off),'ABC'[i]+' roll',fontsize=9)
 ax.scatter([0],[0],[0],color='.5',s=20);ax.text(0,0,.07,'O (unstable)',fontsize=8)
 ax.set(xlim=(0,2.25),ylim=(0,2.25),zlim=(0,2.25),xlabel='A',ylabel='B',zlabel='C',title=r'$\nu_1=1,\ \nu_2=2,\ \delta=2,\ \mu=4.2$')
 ax.view_init(elev=24,azim=-46);ax.legend(loc='upper left',fontsize=8);ax.set_box_aspect((1,1,1))
 fig.savefig('paper-58-oscillating-hexagons.png',dpi=135,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
