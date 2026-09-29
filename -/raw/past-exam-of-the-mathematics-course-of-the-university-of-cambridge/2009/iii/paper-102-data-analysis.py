"""Original examination-data plots; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes its same-basename opaque PNG to the caller's working directory.
Guerry reconstruction: Rdatasets/HistData Guerry, excluding missing Region.
IVF data and bus/village excerpts transcribed from the original examination PDF.
Caller-supplied MPLCONFIGDIR is respected. No network or data-file dependencies.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
GUERRY = [['E', 28870.0, 15890.0, 37.0, 5098.0, 73.0], ['N', 26226.0, 5521.0, 51.0, 8901.0, 22.0], ['C', 26747.0, 7925.0, 13.0, 10973.0, 61.0], ['E', 12935.0, 7289.0, 46.0, 2733.0, 76.0], ['E', 17488.0, 8174.0, 69.0, 6962.0, 83.0], ['S', 9474.0, 10263.0, 27.0, 3188.0, 84.0], ['N', 35203.0, 8847.0, 67.0, 6400.0, 33.0], ['S', 6173.0, 9597.0, 18.0, 3542.0, 72.0], ['E', 19602.0, 4086.0, 59.0, 3608.0, 14.0], ['S', 15647.0, 10431.0, 34.0, 2582.0, 17.0], ['S', 8236.0, 6731.0, 31.0, 3211.0, 50.0], ['S', 13409.0, 5291.0, 38.0, 2314.0, 2.0], ['N', 17577.0, 4500.0, 52.0, 27830.0, 10.0], ['C', 18070.0, 11645.0, 31.0, 4093.0, 59.0], ['W', 24964.0, 13018.0, 36.0, 13602.0, 86.0], ['W', 18712.0, 5357.0, 39.0, 13254.0, 18.0], ['C', 21934.0, 10503.0, 13.0, 9561.0, 63.0], ['C', 15262.0, 12949.0, 12.0, 14993.0, 74.0], ['E', 32256.0, 9159.0, 60.0, 2540.0, 16.0], ['W', 28607.0, 7050.0, 16.0, 10387.0, 70.0], ['C', 37014.0, 20235.0, 23.0, 10997.0, 78.0], ['W', 21585.0, 10237.0, 18.0, 4687.0, 60.0], ['E', 11560.0, 5914.0, 73.0, 3436.0, 31.0], ['E', 13396.0, 7759.0, 42.0, 2829.0, 66.0], ['N', 14795.0, 4774.0, 51.0, 11712.0, 20.0], ['C', 21368.0, 4016.0, 54.0, 4553.0, 11.0], ['W', 29872.0, 6842.0, 15.0, 23945.0, 36.0], ['S', 13115.0, 7990.0, 40.0, 3048.0, 26.0], ['S', 18642.0, 7204.0, 31.0, 2286.0, 23.0], ['S', 18642.0, 10486.0, 38.0, 2848.0, 40.0], ['W', 24096.0, 7423.0, 40.0, 5076.0, 8.0], ['S', 12814.0, 10954.0, 45.0, 1680.0, 12.0], ['W', 22138.0, 6524.0, 25.0, 7686.0, 55.0], ['C', 32404.0, 7624.0, 17.0, 11315.0, 54.0], ['C', 19131.0, 6909.0, 27.0, 7254.0, 27.0], ['E', 18785.0, 8326.0, 29.0, 4077.0, 65.0], ['E', 26221.0, 8059.0, 73.0, 3012.0, 62.0], ['W', 17687.0, 6170.0, 28.0, 12059.0, 81.0], ['C', 21292.0, 6017.0, 27.0, 5626.0, 19.0], ['C', 27491.0, 12665.0, 29.0, 3446.0, 24.0], ['C', 16170.0, 18043.0, 21.0, 2746.0, 75.0], ['W', 19314.0, 9392.0, 24.0, 8310.0, 80.0], ['C', 17722.0, 5042.0, 42.0, 4753.0, 9.0], ['S', 5883.0, 9049.0, 24.0, 5194.0, 42.0], ['W', 22969.0, 8943.0, 31.0, 4432.0, 7.0], ['S', 7710.0, 5990.0, 27.0, 2040.0, 77.0], ['W', 29692.0, 8520.0, 23.0, 4410.0, 34.0], ['N', 31078.0, 7424.0, 43.0, 5179.0, 32.0], ['N', 15602.0, 4950.0, 63.0, 3963.0, 13.0], ['E', 26231.0, 9539.0, 72.0, 4013.0, 25.0], ['W', 28331.0, 9198.0, 19.0, 2107.0, 38.0], ['E', 26674.0, 6831.0, 68.0, 3912.0, 57.0], ['N', 24507.0, 9190.0, 74.0, 4196.0, 52.0], ['W', 23316.0, 7940.0, 14.0, 14739.0, 48.0], ['N', 12153.0, 4529.0, 57.0, 9515.0, 53.0], ['C', 25087.0, 8236.0, 20.0, 10452.0, 44.0], ['N', 26740.0, 6175.0, 45.0, 6092.0, 28.0], ['N', 28180.0, 6659.0, 54.0, 5501.0, 15.0], ['N', 28329.0, 8248.0, 45.0, 9242.0, 35.0], ['N', 23101.0, 4040.0, 49.0, 5740.0, 45.0], ['C', 17256.0, 12141.0, 19.0, 5963.0, 51.0], ['W', 16722.0, 8533.0, 47.0, 3299.0, 79.0], ['S', 12223.0, 9797.0, 53.0, 6001.0, 85.0], ['S', 6728.0, 7632.0, 31.0, 11644.0, 71.0], ['E', 12309.0, 4920.0, 62.0, 14472.0, 46.0], ['E', 7343.0, 4915.0, 71.0, 6001.0, 58.0], ['E', 18793.0, 4504.0, 45.0, 1983.0, 6.0], ['E', 22339.0, 7770.0, 59.0, 11701.0, 69.0], ['E', 28391.0, 10708.0, 32.0, 3710.0, 49.0], ['C', 33913.0, 8294.0, 30.0, 3357.0, 41.0], ['N', 13945.0, 1368.0, 71.0, 4204.0, 1.0], ['N', 18355.0, 2906.0, 43.0, 7245.0, 3.0], ['N', 22201.0, 5786.0, 54.0, 5303.0, 4.0], ['N', 12477.0, 3879.0, 56.0, 4007.0, 5.0], ['W', 18400.0, 6863.0, 41.0, 16956.0, 39.0], ['N', 33592.0, 7144.0, 44.0, 4964.0, 21.0], ['S', 13019.0, 6241.0, 20.0, 3449.0, 47.0], ['S', 14790.0, 8680.0, 25.0, 4558.0, 29.0], ['S', 13145.0, 9572.0, 23.0, 2449.0, 43.0], ['S', 13576.0, 5731.0, 37.0, 1246.0, 64.0], ['W', 20827.0, 7566.0, 28.0, 14035.0, 56.0], ['W', 15010.0, 4710.0, 25.0, 8922.0, 68.0], ['C', 16256.0, 6402.0, 13.0, 13817.0, 67.0], ['E', 18835.0, 9044.0, 62.0, 4040.0, 82.0], ['C', 18006.0, 6516.0, 47.0, 4276.0, 30.0]]

a=np.array([r[1:] for r in GUERRY],float);region=np.array([r[0] for r in GUERRY]);ratio=a[:,0]/a[:,1]
year=np.arange(1,15);u=year-7.5
ivf=np.array([[18201,1712,591,70],[21239,2244,738,110],[23517,2391,837,123],[25414,2589,915,106],[27203,3015,1041,123],[25033,2781,888,113],[23551,2812,978,113],[22737,2945,1013,74],[22720,3083,1002,81],[22342,3116,1007,53],[22477,3284,1096,33],[21884,3371,1043,25],[23250,3460,1015,15],[23794,3626,1132,15]],float)
def fit(s,n,k):
 X=np.column_stack([u**j for j in range(k+1)]);b=np.zeros(k+1);b[0]=np.log(s.sum()/(n-s).sum())
 for _ in range(80):
  p=1/(1+np.exp(-X@b));w=n*p*(1-p);step=np.linalg.solve(X.T@(w[:,None]*X),X.T@(s-n*p));b+=step
  if np.max(abs(step))<1e-12:break
 cov=np.linalg.inv(X.T@(w[:,None]*X));pearson=np.sum((s-n*p)**2/w)
 return b,cov,p,pearson
fig,ax=plt.subplots(4,2,figsize=(12,14),layout='constrained',facecolor='white');ax=ax.ravel()
colors=dict(zip(['C','E','N','S','W'],['#577590','#f8961e','#277da8','#d1495b','#43aa8b']))
ax[0].boxplot([ratio[region==r] for r in colors],tick_labels=list(colors),showmeans=True)
ax[0].set(title='Guerry reconstruction: regional crime ratios',xlabel='Region',ylabel='Property / person crimes')
for r,col in colors.items():ax[1].scatter(a[region==r,4],np.log(ratio[region==r]),s=22,color=col,label=r)
ax[1].set(title='Guerry reconstruction: wealth association',xlabel='Wealth rank (smaller = wealthier)',ylabel='Log crime ratio');ax[1].legend(ncol=5,fontsize=8)
X=np.column_stack([np.ones(85)]+[(region==r).astype(float) for r in ['E','N','S','W']]+[a[:,2],a[:,3]/10000,a[:,4]/10]);lams=np.linspace(-.4,1.1,151);ll=[]
for lam in lams:
 z=np.log(ratio) if abs(lam)<1e-12 else np.expm1(lam*np.log(ratio))/lam
 e=z-X@np.linalg.lstsq(X,z,rcond=None)[0];ll.append(-85/2*np.log(e@e/85)+(lam-1)*np.log(ratio).sum())
ll=np.array(ll);ax[2].plot(lams,ll-ll.max(),color='#277da8');ax[2].axhline(-1.92073,color='gray',ls='--');ax[2].axvline(0,color='black',ls=':');ax[2].set(title='Guerry: Box–Cox profile likelihood',xlabel='Transformation parameter',ylabel='Log likelihood relative to maximum',ylim=(-8,.5))
b,cov,p,P=fit(ivf[:,1],ivf[:,0],3);phi=P/10
fine=np.linspace(1,14,200);Uf=np.column_stack([(fine-7.5)**j for j in range(4)]);eta=Uf@b;se=np.sqrt(np.einsum('ij,jk,ik->i',Uf,cov*phi,Uf));sig=lambda x:1/(1+np.exp(-x))
ax[3].scatter(year,ivf[:,1]/ivf[:,0],color='black',s=25,label='Observed');ax[3].plot(fine,sig(eta),color='#277da8',label='Cubic quasi-binomial fit');ax[3].fill_between(fine,sig(eta-2.228*se),sig(eta+2.228*se),alpha=.2,color='#277da8');ax[3].set(title='IVF: singleton probability per cycle',xlabel='Year index',ylabel='Probability');ax[3].legend(fontsize=8)
res=(ivf[:,1]-ivf[:,0]*p)/np.sqrt(ivf[:,0]*p*(1-p));ax[4].scatter(year,res,color='#277da8');ax[4].axhline(0,color='gray');ax[4].set(title='Singleton fit: Pearson residuals',xlabel='Year index',ylabel='Residual (unit-binomial scale)')
B=ivf[:,1:].sum(axis=1);M=ivf[:,2:].sum(axis=1);b,cov,p,P=fit(M,B,2);Uf=np.column_stack([(fine-7.5)**j for j in range(3)])
ax[5].scatter(year,M/B,color='black',s=25,label='Observed');ax[5].plot(fine,sig(Uf@b),color='#d1495b',label='Quadratic binomial fit');ax[5].set(title='IVF: multiple delivery given live delivery',xlabel='Year index',ylabel='Conditional probability');ax[5].legend(fontsize=8)
for village,y,pop,c in [(1,[21,23,25,30,32],[315,322,308,320,326],'#277da8'),(32,[32,29,25,38,52],[279,264,272,273,265],'#d1495b')]:
 ax[6].plot(np.arange(2004,2009),1000*np.array(y)/pop,'o-',label=f'Village {village}',color=c)
ax[6].set(title='Village trajectories: printed excerpt only',xlabel='Year',ylabel='Incidents per 1000 residents');ax[6].legend(fontsize=8);ax[6].set_xticks(np.arange(2004,2009))
ax[7].scatter([3.25,.75,.25,0],[68,80,85,110],color='#577590',s=45)
ax[7].set(title='Bus providers: four printed rows only',xlabel='Fare (dollars)',ylabel='Mean daily passengers')
for a in ax:a.grid(alpha=.15)
fig.savefig(Path.cwd()/'paper-102-data-analysis.png',dpi=125,facecolor='white',transparent=False)
