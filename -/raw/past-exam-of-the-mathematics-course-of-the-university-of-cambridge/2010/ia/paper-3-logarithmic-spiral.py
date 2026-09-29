"""Original spiral sketch. Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7.
Writes only paper-3-logarithmic-spiral.png to the caller's CWD.
Matplotlib inherits MPLCONFIGDIR when supplied by the caller.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    a,b=1.0,0.1
    u=np.linspace(0,3*np.pi,1400);r=a*np.exp(b*u)
    fig,ax=plt.subplots(figsize=(5.6,5.0),dpi=130,facecolor='white')
    ax.plot(r*np.cos(u),r*np.sin(u),color='#245c9b',lw=2.4)
    for k,label in [(0,'0'),(1,r'$\pi$'),(2,r'$2\pi$'),(3,r'$3\pi$')]:
        t=k*np.pi;rr=a*np.exp(b*t);x,y=rr*np.cos(t),rr*np.sin(t)
        ax.scatter([x],[y],s=28,color='#a53b28',zorder=4)
        ax.annotate(label,(x,y),xytext=(5,7 if k%2==0 else -19),textcoords='offset points',fontsize=10)
    for t in [0.7*np.pi,2.6*np.pi]:
        dt=0.11;x=a*np.exp(b*t)*np.cos(t);y=a*np.exp(b*t)*np.sin(t)
        x2=a*np.exp(b*(t+dt))*np.cos(t+dt);y2=a*np.exp(b*(t+dt))*np.sin(t+dt)
        ax.annotate('',(x2,y2),(x,y),arrowprops={'arrowstyle':'->','color':'#245c9b','lw':2})
    ax.axhline(0,color='0.55',lw=0.7);ax.axvline(0,color='0.55',lw=0.7)
    ax.set_xlim(-2.9,2.6);ax.set_ylim(-2.1,2.7)
    ax.set_aspect('equal');ax.set_xlabel('$x$');ax.set_ylabel('$y$')
    ax.set_title('Logarithmic spiral: one and a half turns\n' + r'$a=1$, $b=0.1$, $0\leq u\leq3\pi$',fontsize=11)
    ax.grid(alpha=0.15);fig.tight_layout()
    fig.savefig('paper-3-logarithmic-spiral.png',facecolor='white',transparent=False)
    plt.close(fig)
if __name__=='__main__':main()
