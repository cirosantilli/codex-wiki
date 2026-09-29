"""Original numerical illustration. Tested with Python 3.14, NumPy 2.3 and Matplotlib 3.10.
Writes its PNG basename to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

EPIDEMIC_RNG=np.random.default_rng(2345)

def sir_sim(t_max,X0,beta,gamma,rng=None):
    if rng is None:rng=EPIDEMIC_RNG
    state=np.array(X0,dtype=int);population=state.sum();time=0.
    times=[time];states=[state.copy()]
    while time<t_max and state[1]>0:
        infection=beta*state[0]*state[1]/population;recovery=gamma*state[1]
        rate=infection+recovery
        if rate==0:
            times.append(float(t_max));states.append(state.copy());break
        next_time=time+rng.exponential(1/rate)
        if next_time>t_max:
            times.append(float(t_max));states.append(state.copy());break
        if rng.random()<infection/rate:state+=np.array([-1,1,0])
        else:state+=np.array([0,-1,1])
        time=next_time;times.append(time);states.append(state.copy())
    return np.array(times),np.array(states)

def sir_sim_stats(n_sim,t_max,X0,beta,gamma,rng=None):
    result=np.empty((n_sim,2))
    for run in range(n_sim):
        t,s=sir_sim(t_max,X0,beta,gamma,rng)
        result[run]=s[:,1].max(),t[-1]
    return result

rng = np.random.default_rng(2345)
# Consume exactly the ten trajectories shown in the companion illustration.
for _ in range(10):
    sir_sim(100, [99,1,0], 1, .25, rng)
stats = sir_sim_stats(1000, 100, [99,1,0], 1, .25, rng)
fig, axes = plt.subplots(1, 2, figsize=(9, 3.8), layout="constrained")
axes[0].hist(stats[:,0], bins=np.arange(.5,65.6,2), color="#3478a5", edgecolor="white")
axes[1].hist(stats[:,1], bins=np.arange(0,61,2), color="#3478a5", edgecolor="white")
for ax in axes:
    ax.axvline(10, ls="--", color="#a33127", label="classification cutoff: 10")
    ax.set_ylabel("Number of outbreaks")
    ax.legend(frameon=False, fontsize=8)
axes[0].set_xlabel("Peak infected population")
axes[1].set_xlabel("Extinction time (days)")
fig.suptitle("1000 further stochastic SIR outbreaks (seed 2345)")
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
