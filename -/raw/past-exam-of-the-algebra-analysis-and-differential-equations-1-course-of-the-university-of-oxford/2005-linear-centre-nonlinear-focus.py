"""Original RK4 example: imaginary eigenvalues hide a weak repelling focus."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def field(z):
    x,y=z
    return np.array([y*np.exp(x*y),1-x**4-y*y])

def local_function(x,y):
    x=2*(x-1)
    return (x*x+y*y)/2+7*x**3/12+x*y*y/2+y**3/3+x**4/4-3*x**3*y/16+3*x*y**3/16

def main():
    t=np.linspace(0,8*np.pi,32001);dt=t[1]-t[0]
    z=np.empty((len(t),2));z[0]=[1.05,0]
    for j in range(len(t)-1):
        a=field(z[j]);b=field(z[j]+dt*a/2);c=field(z[j]+dt*b/2);d=field(z[j]+dt*c)
        z[j+1]=z[j]+dt*(a+2*b+2*c+d)/6
    linear_x=1+.05*np.cos(2*t);linear_y=-.1*np.sin(2*t)
    fig,axes=plt.subplots(1,2,figsize=(10.2,4.3),layout='constrained')
    axes[0].plot(linear_x,linear_y,'--',lw=2,color='#176fa8',label='Linearized ellipse')
    axes[0].plot(z[:,0],z[:,1],color='#ac4b28',lw=.8,label='Printed nonlinear system')
    axes[0].scatter([1],[0],color='#222',s=19);axes[0].set(xlabel='x',ylabel='y',title='Eight rotations from the same initial point');axes[0].legend(fontsize=8);axes[0].set_aspect('equal',adjustable='box')
    h=local_function(z[:,0],z[:,1]);axes[1].plot(t/np.pi,h/h[0],color='#ac4b28',lw=1.8)
    axes[1].set(xlabel='Time / linearized period π',ylabel='H(t) / H(0)',title='A positive local function grows along the spiral')
    for ax in axes:ax.grid(alpha=.18)
    fig.suptitle('The nonlinear equilibrium is a weak repelling focus')
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,facecolor='white');plt.close(fig)

if __name__=='__main__':
    main()
