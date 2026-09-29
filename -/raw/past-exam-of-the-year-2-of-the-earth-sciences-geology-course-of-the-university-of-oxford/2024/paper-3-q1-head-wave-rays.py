"""Original ray constructions; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory: writes an opaque basename PNG to CWD.
The 40 m head segment is illustrative; first appearance has zero head length.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({'font.size': 9})
    fig, axes = plt.subplots(2, 3, figsize=(12, 6.4), layout='constrained')
    for row, speed in enumerate((2500., 1600.)):
        for col, (down, up) in enumerate(((1500., 1500.), (1500., 900.), (900., 900.))):
            ax = axes[row, col]
            p = 1 / speed
            water = np.arcsin(1500 * p)
            sd, su = np.arcsin(down * p), np.arcsin(up * p)
            w, d, u = 50*np.tan(water), 20*np.tan(sd), 20*np.tan(su)
            first = 2*w+d+u
            xs = np.cumsum([0, w, d, 40, u, w])
            ys = [0, 50, 70, 70, 50, 0]
            ax.axhspan(0, 50, color='#e0f2fa')
            ax.axhspan(50, 70, color='#f4e5c6')
            ax.axhspan(70, 88, color='#e1dfdb')
            for a, b in ((0,1),(1,2),(3,4),(4,5)):
                color = '#a42f21' if ((a==1 and down==900) or (a==3 and up==900)) else '#175b89'
                ax.plot(xs[a:b+1], ys[a:b+1], color=color, lw=2)
            ax.annotate('', xy=(xs[3],70), xytext=(xs[2],70), arrowprops={'arrowstyle':'->','color':'#442071','lw':2.4})
            ax.plot([0,xs[-1]],[0,0], 'ko', ms=4)
            ax.axhline(50,color='0.4',lw=.6); ax.axhline(70,color='0.4',lw=.6)
            ax.text(0,-4,'source',va='bottom'); ax.text(xs[-1],-4,'receiver',ha='right',va='bottom')
            ax.text(.03,.05, f'Water P: {np.degrees(water):.2f}°\nSediment: {np.degrees(sd):.2f}° down, {np.degrees(su):.2f}° up',transform=ax.transAxes, fontsize=8)
            modes = ('P' if down==1500 else 'S')+('P' if up==1500 else 'S')
            ax.set(title=f'Basement {"P" if row==0 else "S"} head; sediment {modes}\nFirst appearance: {first:.2f} m',xlabel='Surface offset / m',ylabel='Depth / m',ylim=(88,-12),xlim=(-8,xs[-1]+8))
    fig.suptitle('Surface source and receiver: all sediment-mode combinations\nAngles from the vertical normal; a 40 m head segment is added for visibility')
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'), dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
