#!/usr/bin/env python3
"""Generate paper-316-dust-loci.png."""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, tan, pi


mu=1.0
q=1.0
p=2*q

def comet_state(f):
    r=p/(1+np.cos(f))
    pos=np.array([r*np.cos(f),r*np.sin(f)],float)
    vel=np.sqrt(mu/p)*np.array([-np.sin(f),1+np.cos(f)],float)
    return pos,vel

def comet_time(f):
    D=np.tan(f/2)
    return np.sqrt(2*q**3/mu)*(D+D**3/3)

def propagate(pos,vel,beta,dt):
    if dt <= 0: return pos.copy(),vel.copy()
    y=np.r_[pos,vel].astype(float)
    n=max(300,int(1200*dt/(comet_time(pi/2)-comet_time(-pi/2))))
    h=dt/n
    def rhs(y):
        r=y[:2]; rr=np.linalg.norm(r)
        return np.r_[y[2:],-(1-beta)*mu*r/rr**3]
    for _ in range(n):
        k1=rhs(y); k2=rhs(y+h*k1/2); k3=rhs(y+h*k2/2); k4=rhs(y+h*k3)
        y += h*(k1+2*k2+2*k3+k4)/6
    return y[:2],y[2:]

tobs=comet_time(pi/2)
comet_obs,_=comet_state(pi/2)
fs=np.linspace(-pi/2,pi/2,220)
orb=np.array([comet_state(f)[0] for f in fs])
fig,axs=plt.subplots(1,2,figsize=(11,5),constrained_layout=True)
for ax in axs:
    ax.plot(orb[:,0],orb[:,1],color='#777',lw=1.4,label='comet orbit')
    ax.scatter([0],[0],s=100,color='#f4b942',edgecolor='#8c5f00',zorder=5,label='star')
    ax.scatter([comet_obs[0]],[comet_obs[1]],marker='*',s=120,color='black',zorder=6,label=r'comet at $f=\pi/2$')
    ax.set_aspect('equal'); ax.grid(alpha=.22); ax.set_xlabel('$x/q$'); ax.set_ylabel('$y/q$')

# Synchrone: release at pericentre
p0,v0=comet_state(0)
betas=np.linspace(0.08,1.55,160)
pts=np.array([propagate(p0,v0,b,tobs)[0] for b in betas])
axs[0].plot(pts[:,0],pts[:,1],color='#006bb6',lw=2.4,label='pericentre synchrone')
for b in [0.3,0.7,1.0,1.3,1.5]:
    pp=propagate(p0,v0,b,tobs)[0]
    axs[0].scatter(*pp,s=18,color='#006bb6')
    axs[0].annotate(rf'$\beta={b:g}$',pp,xytext=(4,4),textcoords='offset points',fontsize=8)
axs[0].set_title('Same release time: synchrone')

# Syndynes: fixed beta, release times vary
colors=['#2ca02c','#d62728','#7b2cbf']
for b,c in zip([0.7,1.0,1.3],colors):
    relfs=np.linspace(-pi/2,pi/2,180)
    line=[]
    for f0 in relfs:
        pp,vv=comet_state(f0)
        line.append(propagate(pp,vv,b,tobs-comet_time(f0))[0])
    line=np.array(line)
    axs[1].plot(line[:,0],line[:,1],lw=2.1,color=c,label=rf'$\beta={b:g}$')
axs[1].set_title(r'Same $\beta$: syndynes')
for ax in axs:
    ax.legend(fontsize=8,loc='best')
fig.suptitle('Zero-ejection-speed dust released from a parabolic comet',fontsize=13)
output = Path(Path(__file__).stem + ".png")
fig.savefig(output, dpi=100, facecolor="white")
plt.close(fig)
