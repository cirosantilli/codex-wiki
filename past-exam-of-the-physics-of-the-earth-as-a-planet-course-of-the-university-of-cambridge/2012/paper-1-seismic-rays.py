"""Original ray integrations for illustrative speed profiles; Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':9,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
# Segments are (upper depth km, lower depth km, speed at upper depth km/s, gradient s^-1).
PROFILES={'high':[(0,40,5,.03),(40,50,6.2,.2),(50,180,8.2,.03)],'low':[(0,40,5,.03),(40,65,6.2,-.04),(65,200,5.2,.03)]}
def path(segments,zt,points=100):
 vt=next(v+b*(zt-a) for a,c,v,b in segments if a<=zt<=c);p=1/vt;X=0.;T=0.;zs=[0.];xs=[0.]
 for a,c,v,b in segments:
  end=min(zt,c)
  if end<=a:break
  ve=v+b*(end-a)
  if max(v,ve)>vt*(1+1e-12):return None
  root0=np.sqrt(max(0,1-(p*v)**2));root1=0. if end==zt else np.sqrt(max(0,1-(p*ve)**2))
  dx=(root0-root1)/(p*b)
  tt=(np.arccosh(max(1,1/(p*v)))-(0. if end==zt else np.arccosh(max(1,1/(p*ve)))))/b
  zz=np.linspace(a,end,points);vv=v+b*(zz-a);rr=np.sqrt(np.maximum(0,1-(p*vv)**2));
  if end==zt:rr[-1]=0.
  local=(root0-rr)/(p*b)
  zs.extend(zz[1:]);xs.extend(X+local[1:]);X+=dx;T+=tt
  if end==zt:break
 return 2*X,2*T,p,np.array(xs),np.array(zs)
def branch(segments,lo,hi):
 out=[path(segments,float(z),points=2) for z in np.linspace(lo,hi,1200)];out=[v for v in out if v is not None];return np.array([v[:3] for v in out])
def main():
 fig,axs=plt.subplots(2,3,figsize=(12,7),layout='constrained');colors=['#246d9c','#bd7831','#7a5d9b']
 for row,key in enumerate(['high','low']):
  seg=PROFILES[key];axv,axr,axt=axs[row]
  for a,c,v,b in seg:axv.plot([v,v+b*(c-a)],[a,c],color='#333333',lw=2)
  axv.axhspan(40,50 if key=='high' else 65,color='#bd7831',alpha=.12);axv.set(xlabel='speed (km/s)',ylabel='depth (km)',ylim=(150,0),title='High-gradient zone' if key=='high' else 'Decreasing-speed zone')
  turns=[15,30,39.8,44,49.8,85,125] if key=='high' else [15,30,39.8,105,130,160]
  for j,zt in enumerate(turns):
   X,T,p,x,z=path(seg,zt);axr.plot(np.r_[x,X-x[::-1]],np.r_[z,z[::-1]],color=colors[min(j//3,2)],lw=1)
  axr.axhspan(40,50 if key=='high' else 65,color='#bd7831',alpha=.12);axr.set(xlabel='surface range (km)',ylabel='depth (km)',ylim=(170,0),title='Surface-returning diving rays')
  ranges=[(.02,39.999),(40.001,49.999),(50.001,170)] if key=='high' else [(.02,39.999),(98.334,190)]
  branches=[]
  for j,(lo,hi) in enumerate(ranges):
   curve=branch(seg,lo,hi);axt.plot(curve[:,0],curve[:,1],lw=2,color=colors[j],label=['above zone','within zone','below zone'][j] if key=='high' else ['above zone','below zone'][j]);branches.append(curve)
  if key=='low':
   start=branches[0][-1,0];end=branches[1][:,0].min()
   if end>start:axt.axvspan(start,end,color='grey',alpha=.1,label='diving-ray shadow')
  axt.set(xlabel='range X (km)',ylabel='travel time T (s)',title='All branches, including later arrivals');axt.legend(fontsize=7)
  if key=='high':axt.set(xlim=(90,270),ylim=(24,50),title='Triplication detail: three arrival branches')
  for ax in [axv,axr,axt]:ax.grid(alpha=.12)
 fig.savefig(Path(__file__).stem+'.png',dpi=145,bbox_inches='tight',facecolor='white');plt.close(fig)
if __name__=='__main__':main()
