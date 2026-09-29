"""Original transformed-data fit; Python 3.14/numpy 2.3.5/matplotlib 3.10.7.

Run from mirrored _media directory. Rates in counts/day, times in ps.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    t=np.array([.25,.75,1.25,1.75,2.25,2.75])
    y=np.log([1339,360,110,31,14,3]);s=.15
    slope,intercept=np.linalg.lstsq(np.column_stack([t,np.ones_like(t)]),y,rcond=None)[0]
    ma=-1/.478;ca=np.mean(y-ma*t)
    line=np.linspace(0,3,301)
    fig,(ax,res)=plt.subplots(2,1,figsize=(7.1,5.6),sharex=True,gridspec_kw={'height_ratios':[2,1]},layout='constrained')
    ax.errorbar(t,y,yerr=s,fmt='o',color='black',capsize=3,label='transformed data')
    ax.plot(line,slope*line+intercept,color='#236bc0',lw=2.2,label=fr'free fit: $\tau={-1/slope:.4f}$ ps')
    ax.plot(line,ma*line+ca,color='#c26712',lw=2,ls='--',label=r'fixed $\tau=0.478$ ps, refitted $R_0$')
    ax.set(ylabel=r'$\ln[R/(1\ \mathrm{count/day})]$',title='Exponential-decay fit with equal fractional rate errors')
    ax.grid(alpha=.18);ax.legend(fontsize=9)
    for m,c,color,marker in [(slope,intercept,'#236bc0','o'),(ma,ca,'#c26712','s')]:
        res.plot(t,(y-m*t-c)/s,marker=marker,ls='-',color=color,ms=5,lw=1.1)
    res.axhline(0,color='0.4',lw=.8)
    res.set(xlim=(0,3),xlabel='Proper time (ps)',ylabel='Residual / 0.15')
    res.grid(alpha=.18)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
