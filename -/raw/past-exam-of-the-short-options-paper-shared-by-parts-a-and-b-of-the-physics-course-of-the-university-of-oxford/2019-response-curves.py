"""Illustrate qualitative depth dose and the specified climate model; Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
fig,(a,b)=plt.subplots(1,2,figsize=(12,4.8),layout='constrained')
x=np.linspace(0,1.4,1000)
# These depth-dose profiles are illustrative shapes, not transport calculations.
ph=(1-np.exp(-x/.05))*np.exp(-x/1.1)
pr=(.24+.1*x+1.2*np.exp(-((x-.96)/.055)**2))/(1+np.exp((x-1.02)/.014))
a.plot(x,ph/ph.max(),label='photons: build-up and exit dose',lw=2)
a.plot(x,pr/pr.max(),label='monoenergetic protons: Bragg peak',lw=2)
a.set_title('Depth dose: qualitative shapes only');a.set_xlabel('Depth (arbitrary units)');a.set_ylabel('Dose (separately normalized)');a.legend(fontsize=9);a.set_ylim(0,1.15)
a.annotate('sharp distal fall-off',(1.07,.03),(1.1,.55),arrowprops={'arrowstyle':'->'},ha='center',fontsize=10)
b.set_title('70-year forcing ramp, then constant forcing')
t=np.linspace(0,1000,2001);u=np.minimum(t,70)
f1=4/70*(1-np.exp(-70/4));f2=400/70*(1-np.exp(-70/400));bs=(1/3-f1)/(f2-f1);bf=1-bs
response=3/70*(u-bf*4*(1-np.exp(-u/4))-bs*400*(1-np.exp(-u/400)))
late=t>70;z=t[late]-70
response[late]=3-3*bf*f1*np.exp(-z/4)-3*bs*f2*np.exp(-z/400)
b.plot(t,response,label='surface temperature',lw=2);b.plot(t,3*u/70,ls=':',label='instantaneous equilibrium temperature')
b.scatter([70],[2],color='black',zorder=4);b.annotate('TCR = 2 K',(70,2),(180,1.2),arrowprops={'arrowstyle':'->'})
b.axhline(3,color='0.5',ls='--');b.text(650,3.08,'ECS = 3 K')
b.set_xlabel('Years from start');b.set_ylabel('Warming (K)');b.set_ylim(0,3.5);b.set_xlim(0,1000);b.legend(loc='lower right',fontsize=9)
b.text(380,.65,'Fast time: 4 years\nSlow time: 400 years')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
