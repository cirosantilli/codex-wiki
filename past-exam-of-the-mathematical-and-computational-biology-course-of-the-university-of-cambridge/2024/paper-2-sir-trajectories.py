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
trajectories = [sir_sim(100, [99,1,0], 1, .25, rng) for _ in range(10)]
fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
for t, x in trajectories:
    ax.step(t, x[:,1], where="post", lw=1.1, alpha=.8)
ax.set(xlabel="Time (days)", ylabel="Infected individuals", xlim=(0,60), ylim=(0,65), title="Ten stochastic SIR outbreaks (seed 2345)")
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
