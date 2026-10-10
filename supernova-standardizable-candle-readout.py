"""Generate a functional, schematic supernova distance readout (Python 3.14, NumPy 2.3, Matplotlib 3.10)."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


def main():
    fig = plt.figure(figsize=(12, 7.8), facecolor='white', dpi=100)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set(xlim=(0, 12), ylim=(0, 7.8)); ax.axis('off')
    ink, blue, orange = '#233548', '#17658a', '#ad5318'
    def box(x, y, w, h, title, body, color=blue):
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.08',fc='#f4f8fa',ec=color,lw=1.5))
        ax.text(x+w/2,y+h-.25,title,ha='center',va='top',fontsize=12.5,weight='bold',color=color)
        ax.text(x+w/2,y+h/2-.17,body,ha='center',va='center',fontsize=11,color=ink,linespacing=1.5)
    def arrow(a,b):
        ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,lw=1.6,color=ink))
    ax.text(.45,7.42,'How a standardizable candle measures relative distance',fontsize=20,weight='bold',color=ink)
    ax.text(.45,7.05,'Functional schematic • arbitrary light curves below • no survey data',fontsize=12,color='#596875')
    box(.45,5.3,3.2,1.35,'1  Find and separate','Repeat images − reference image\nRemove host light; recover source flux')
    box(4.4,5.3,3.2,1.35,'2  Measure a spectrum','Classify the transient\n'+r'$z=\lambda_{\rm obs}/\lambda_{\rm rest}-1$')
    box(8.35,5.3,3.2,1.35,'3  Follow brightness','Calibrate several filters over time\nFit peak, width and colour')
    arrow((3.75,5.97),(4.27,5.97)); arrow((7.7,5.97),(8.22,5.97))
    plot = fig.add_axes([.065,.365,.30,.245],facecolor='white')
    time=np.linspace(-20,60,350)
    for stretch,amp,col in [(.8,.78,orange),(1.15,1.15,blue)]:
        u=time/stretch
        template=np.where(u<0,np.exp(-.5*(u/8)**2),np.exp(-u/24))
        plot.plot(time,amp*template,color=col,lw=2,label=f'width {stretch:.2f} (toy)')
    plot.set(xlabel='Rest-frame time (days)',ylabel='Flux (arbitrary units)',xlim=(-20,60),ylim=(0,1.32))
    plot.spines[['top','right']].set_visible(False);plot.tick_params(labelsize=9);plot.legend(fontsize=9,frameon=False,loc='upper right')
    box(5.05,2.88,6.5,1.83,'4  Standardize in a common emitted band',r'$u=(t_{\rm obs}-t_{\max})/[s(1+z)]$'+'\n'+r'$m_{\rm corr}=m_{\rm obs}-K-A+\alpha(s-1)$'+'\nCorrect band shift, attenuation and intrinsic width',orange)
    arrow((4.1,3.82),(4.9,3.82)); arrow((9.95,5.2),(9.95,4.83))
    box(.45,.68,5.15,1.42,'5  Read a relative distance',r'$m_{\rm corr}=M_0+\mu$'+'\n'+r'$d_{L,2}/d_{L,1}=10^{(m_{{\rm corr},2}-m_{{\rm corr},1})/5}$')
    box(6.4,.68,5.15,1.42,'6  Test an expansion history','Compare the shape with FLRW predictions\nAssume stable calibration, populations and transparency',orange)
    arrow((5.7,1.38),(6.25,1.38)); arrow((6.1,2.78),(3.05,2.22))
    ax.text(6,.22,r'Unknown $M_0$ and $H_0$ share an intercept; brightness alone does not determine acceleration.',ha='center',fontsize=11,color=ink)
    fig.savefig(Path(__file__).stem+'.png',facecolor='white',dpi=100)
    plt.close(fig)


if __name__ == '__main__':
    main()
