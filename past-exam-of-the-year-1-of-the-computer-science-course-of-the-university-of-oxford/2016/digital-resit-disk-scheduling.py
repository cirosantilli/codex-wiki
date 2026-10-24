"""Plot original service routes; save the PNG in cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    routes={'FCFS':[133,76,157,91,142,97,135,112,23],
            'SSTF':[133,135,142,157,112,97,91,76,23],
            'SCAN':[133,112,97,91,76,23,0,135,142,157],
            'LOOK':[133,112,97,91,76,23,135,142,157]}
    fig,axes=plt.subplots(1,2,figsize=(10,4.2),dpi=100,facecolor='white')
    colors={'FCFS':'#a14b30','SSTF':'#176b8e','SCAN':'#713ea5','LOOK':'#247643'}
    for ax,names,title in zip(axes,[['FCFS','SSTF'],['SCAN','LOOK']],['Arrival order and nearest track','Downward sweep and turnaround']):
        for name in names:
            ys=routes[name];distance=sum(abs(a-b)for a,b in zip(ys,ys[1:]));ax.plot(range(len(ys)),ys,'-o',ms=4,lw=1.8,color=colors[name],label=f'{name}: {distance} tracks')
        ax.set_ylim(-10,210);ax.set_xlabel('Service or turnaround step');ax.set_ylabel('Head track');ax.grid(alpha=.25);ax.set_title(title,fontsize=12);ax.legend(fontsize=10)
    axes[1].annotate('Physical endpoint',xy=(6,0),xytext=(3.8,45),arrowprops=dict(arrowstyle='->',color='#713ea5'),fontsize=10)
    fig.suptitle('Disk scheduling from track 133',fontsize=14)
    fig.tight_layout(rect=(0,0,1,.93))
    fig.savefig(Path.cwd()/'digital-resit-disk-scheduling.png',facecolor='white',transparent=False)
    plt.close(fig)
if __name__ == '__main__': main()
