"""Original numerical illustration. Tested with Python 3.14, NumPy 2.3 and Matplotlib 3.10.
Writes its PNG basename to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def methylation_score(pattern, observed):
    """Conditional-product score used by the practical's natural loop filling."""
    pattern=np.asarray(pattern,dtype=int);observed=np.asarray(observed,dtype=int)
    if pattern[0]!=1 or pattern[-1]!=1:return -np.inf
    neighbour_sum=pattern[:-2]+pattern[2:]
    p=np.array([.1,.5,.9])[neighbour_sum]
    prior_terms=np.where(pattern[1:-1]==1,p,1-p)
    observation_terms=np.where(pattern==observed,.8,.2)
    return float(np.log(prior_terms).sum()+np.log(observation_terms).sum())

def sample_methylation(observed, nsteps=5000, seed=2024, score=methylation_score):
    rng=np.random.default_rng(seed)
    state=rng.integers(0,2,size=len(observed));state[[0,-1]]=1
    states=np.empty((nsteps,len(state)),dtype=int);values=np.empty(nsteps)
    states[0]=state;values[0]=score(state,observed)
    accepted=0
    for t in range(1,nsteps):
        candidate=state.copy();site=rng.integers(1,len(state)-1)
        candidate[site]=1-candidate[site]
        trial=score(candidate,observed)
        if np.log(rng.random())<min(0.,trial-values[t-1]):
            state=candidate;values[t]=trial;accepted+=1
        else:values[t]=values[t-1]
        states[t]=state
    return values,states,accepted/(nsteps-1)

observed = np.array([1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1])
values, states, _ = sample_methylation(observed)
burnin = 3000
fig, axes = plt.subplots(2, 1, figsize=(9, 6), layout="constrained")
axes[0].plot(values, lw=.65, color="#24609b")
axes[0].axvline(burnin, color="#a33127", ls="--", label="provisional burn-in: 3000")
axes[0].set(xlabel="Stored state index", ylabel="Conditional-product log score")
axes[0].legend(frameon=False)
axes[1].plot(states[burnin:].mean(axis=0), color="#24609b", label="retained-sample mean")
axes[1].scatter(np.arange(len(observed)), .2*observed, s=9, color="#b05429", label="0.2 × observation")
axes[1].set(xlabel="Site index (zero based)", ylabel="Methylation probability", ylim=(-.04,1.04))
axes[1].legend(frameon=False, ncol=2)
fig.suptitle("Methylation sampling: seed 2024, 5000 stored states")
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
