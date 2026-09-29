"""Exact modular inverses of3 and their real versus2-adic errors from1/3."""
from fractions import Fraction
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def valuation_two(n):
    assert n>0
    return (n & -n).bit_length()-1


def main():
    ns=list(range(1,13));rs=[pow(3,-1,2**n) for n in ns]
    real=[float(Fraction(3*r-1,3)) for r in rs]
    valuations=[valuation_two(3*r-1) for r in rs]
    distances=[2.**(-v) for v in valuations]
    assert rs[:8]==[1,3,3,11,11,43,43,171]
    assert all((3*r-1)%(2**n)==0 for n,r in zip(ns,rs))
    fig,(a,b)=plt.subplots(1,2,figsize=(12.2,5.8),dpi=100,facecolor='white')
    fig.suptitle('Modular inverses converge to 1/3 in the 2-adic distance',fontsize=18,y=.97)
    a.plot(ns,distances,'o-',color='#256d98',lw=2,ms=5,label='Exact 2-adic error')
    a.plot(ns,2.**(-np.array(ns)),'--',color='#7297ad',lw=1.4,label='Precision bound 2⁻ⁿ')
    a.set_yscale('log',base=2);a.set(xlabel='Modulus precision n: modulo 2ⁿ',ylabel='2-adic distance from 1/3',title='Every residue satisfies 3rₙ ≡ 1 mod 2ⁿ')
    a.legend(fontsize=10,loc='upper right')
    b.plot(ns,real,'o-',color='#c57826',lw=2,ms=5)
    b.set_yscale('log',base=2);b.set(xlabel='Modulus precision n: modulo 2ⁿ',ylabel='Ordinary real distance from 1/3',title='The same representatives grow as real numbers')
    for ax in (a,b):ax.set_xticks([1,2,4,6,8,10,12]);ax.grid(alpha=.18);ax.spines[['top','right']].set_visible(False)
    fig.text(.5,.055,'Least nonnegative residues rₙ: 1, 3, 3, 11, 11, 43, 43, 171, … · Original exact modular arithmetic',ha='center',fontsize=11)
    fig.subplots_adjust(left=.08,right=.97,bottom=.18,top=.79,wspace=.32)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white');plt.close(fig)


if __name__=='__main__':main()
