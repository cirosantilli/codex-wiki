"""Original bidisperse shocks/composition figure; output PNG basename to cwd.
Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.
"""
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR',str(Path.cwd()/'.paper-74-mplconfig'))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
 fig,(ax,dep)=plt.subplots(1,2,figsize=(12,6.5),dpi=100,facecolor='white',gridspec_kw={'width_ratios':[1.6,1]});ax.set_facecolor('white');dep.set_facecolor('white')
 t1=192/203;t2=24/7;h1=5/29
 ta=np.linspace(0,t1,100);tb=np.linspace(t1,t2,160);T=np.r_[ta,tb[1:]]
 small=1-7*T/32;bed=np.where(T<=t1,35*T/192,h1+(T-t1)/32)
 ax.fill_betweenx(T,small,1,color='#f6fbfc');ax.fill_betweenx(T,bed,small,color='#d7e9f3')
 fast=1-7*ta/8;ax.fill_betweenx(ta,35*ta/192,fast,color='#c8badd',alpha=.8)
 ax.fill_betweenx(T,0,np.minimum(bed,h1),color='#bc956b',alpha=.8);ax.fill_betweenx(tb,h1,h1+(tb-t1)/32,color='#e4c573',alpha=.8)
 ax.plot(small,T,c='#387aa0',lw=2.4,label='Small-particle clearing');ax.plot(fast,ta,c='#7d51a0',lw=2.4,label='Large-particle clearing')
 ax.plot(35*ta/192,ta,c='#87522f',lw=2.4,label='Mixed deposition');ax.plot(h1+(tb-t1)/32,tb,c='#b2851c',lw=2.4,label='Small-only deposition')
 ax.plot([h1,.25],[t1,t2],'ko',ms=4)
 ax.annotate(r'$(h_1/H,W_st_1/H)=(5/29,192/203)$',xy=(h1,t1),xytext=(.42,.8),fontsize=9,arrowprops={'arrowstyle':'-','color':'#555'})
 ax.annotate(r'$(h_2/H,W_st_2/H)=(1/4,24/7)$',xy=(.25,t2),xytext=(.33,3.58),fontsize=9,arrowprops={'arrowstyle':'-','color':'#555'})
 ax.text(.79,2,'Clear fluid',ha='center',fontsize=11);ax.text(.40,1.9,'Small particles only',ha='center',rotation=35,fontsize=10);ax.text(.16,.26,'Both sizes',ha='center',fontsize=9)
 ax.set_xlim(0,1);ax.set_ylim(0,3.95);ax.set_xlabel('Height above bottom, $z/H$');ax.set_ylabel('Time, $W_s(a)t/H$');ax.set_title('Shock paths and their merger',fontsize=13);ax.legend(loc='upper right',fontsize=8)
 dep.barh(h1/2,72.5,height=h1,left=0,color='#87522f',label='Large-particle solid volume');dep.barh(h1/2,27.5,height=h1,left=72.5,color='#e4c573',label='Small-particle solid volume');dep.barh((h1+.25)/2,100,height=.25-h1,color='#e4c573')
 dep.axhline(h1,c='#333',lw=.9,ls='--');dep.axhline(.25,c='#333',lw=.9)
 dep.text(36,h1/2,'72.5% large',ha='center',va='center',color='white',fontsize=10);dep.text(86,h1/2,'27.5%\nsmall',ha='center',va='center',fontsize=9);dep.text(50,(h1+.25)/2,'100% small',ha='center',va='center',fontsize=10)
 dep.text(50,.295,'Clear fluid above the deposit',ha='center',fontsize=10)
 dep.set_xlim(0,100);dep.set_ylim(0,.34);dep.set_xlabel('Percentage of deposited solid volume');dep.set_ylabel('Height above bottom, $z/H$');dep.set_yticks([0,h1,.25],['0','5/29','1/4']);dep.set_title('Final deposit composition',fontsize=13)
 fig.suptitle('Bidisperse batch settling: large radius a, small radius a/2',fontsize=15)
 fig.tight_layout(rect=[0,0,1,.95]);fig.savefig(Path.cwd()/'paper-74-bidisperse-shocks.png',facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
