"""Plot expected cache service time; save the PNG in cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    fig,ax=plt.subplots(figsize=(6.4,3.6),dpi=100,facecolor='white')
    ax.plot([0,1],[45,1],lw=2.3,color='#176b8e')
    for h,t,offset in [(0,45,(12,-3)),(.5,23,(12,4)),(1,1,(-70,10))]:
        ax.plot(h,t,'o',color='#a34729');ax.annotate(f'({h:g}, {t:g} ms)',(h,t),xytext=offset,textcoords='offset points',fontsize=10)
    ax.set_xlim(-.04,1.04);ax.set_ylim(-1,49);ax.set_xlabel('Cache hit rate h');ax.set_ylabel('Expected service time (ms)');ax.set_title('T(h) = 45 − 44h milliseconds');ax.grid(alpha=.25)
    fig.tight_layout();fig.savefig(Path.cwd()/'digital-resit-cache-latency.png',facecolor='white',transparent=False);plt.close(fig)
if __name__ == '__main__': main()
