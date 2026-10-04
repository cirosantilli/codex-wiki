"""Original energy contours; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes paper-65-hamiltonian.png to CWD; preserves supplied MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    fig,ax=plt.subplots(figsize=(7,4.2),constrained_layout=True)
    u=np.linspace(-2.6,2.6,500);v=np.linspace(-2.8,2.8,500);U,V=np.meshgrid(u,v);H=V**2/2+U-U**3/3
    cs=ax.contour(U,V,H,levels=[-.6,-.3,0,.3,.58,.9,1.3,2],colors='#7891a4',linewidths=.8);ax.clabel(cs,fontsize=8)
    cs=ax.contour(U,V,H,levels=[2/3],colors='#b04a3e',linewidths=1.2)
    z=np.linspace(-2,1,600);vv=np.sqrt(2/3)*(1-z)*np.sqrt(z+2);ax.plot(z,vv,color='#b04a3e',lw=2);ax.plot(z,-vv,color='#b04a3e',lw=2)
    ax.plot(-1,0,'ko',ms=5);ax.plot(1,0,'ko',ms=5);ax.annotate('center: H=−2/3',(-1,0),xytext=(-1.8,-.4));ax.annotate('saddle: H=2/3',(1,0),xytext=(.6,-.5))
    ax.annotate('',xy=(-.5,1.5),xytext=(-.9,1.43),arrowprops={'arrowstyle':'->','color':'#b04a3e'})
    ax.annotate('',xy=(-.9,-1.43),xytext=(-.5,-1.5),arrowprops={'arrowstyle':'->','color':'#b04a3e'})
    ax.set(xlim=(-2.6,2.6),ylim=(-2.8,2.8),xlabel='u',ylabel='v',title='Hamiltonian contours, α=1; saddle loop in red')
    fig.savefig('paper-65-hamiltonian.png',dpi=150,facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
