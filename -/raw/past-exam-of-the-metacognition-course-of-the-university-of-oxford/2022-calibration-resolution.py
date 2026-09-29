#!/usr/bin/env python3
"""Illustrative confidence models, not experimental measurements. Output to cwd."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

p = np.array([0.55, 0.65, 0.75, 0.85])
correct = np.array([55, 65, 75, 85])
incorrect = 100 - correct
assert np.array_equal(correct + incorrect, np.full(4, 100))
assert np.allclose(correct / 100, p)
fpr = np.r_[0, np.cumsum(incorrect[::-1]) / incorrect.sum()]
tpr = np.r_[0, np.cumsum(correct[::-1]) / correct.sum()]
auc = float(np.trapezoid(tpr, fpr))
wins = sum(int(correct[i]) * int(incorrect[j]) for i in range(4) for j in range(i))
ties = sum(int(a) * int(b) for a, b in zip(correct, incorrect))
assert np.isclose(auc, (wins + ties / 2) / (correct.sum() * incorrect.sum()))
assert np.all(np.diff(p + 0.12) > 0)

plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False})
fig, axes = plt.subplots(1, 3, figsize=(12, 4.2), dpi=100, facecolor='white')
a = axes[0]
a.plot([0.5, 1], [0.5, 1], '--', color='0.65', label='Perfect calibration')
a.plot(p, p, 'o-', color='#166a95', label='Report p')
a.plot(p + 0.12, p, 's-', color='#b44c20', label='Report p + 0.12')
a.set(xlabel='Reported confidence', ylabel='Proportion correct', xlim=(0.5, 1), ylim=(0.5, 1), title='A. Same ordering, different calibration')
a.legend(fontsize=8, loc='upper left')
a.grid(alpha=0.18)

a = axes[1]
a.plot([0, 1], [0, 1], '--', color='0.65', label='Chance')
a.plot(fpr, tpr, 'o-', color='#166a95', label='Both reporting rules')
a.set(xlabel='P(high confidence | incorrect)', ylabel='P(high confidence | correct)', xlim=(0, 1), ylim=(0, 1), title=f'B. Identical type 2 ROC; AUC = {auc:.3f}')
a.legend(fontsize=8, loc='lower right')
a.grid(alpha=0.18)

a = axes[2]
x = np.linspace(-2.5, 2.5, 201)
a.plot(x, x, '--', color='0.65', label='Self-estimate equals observed score')
a.plot(x, 0.5*x, '-', color='#6a3b8f', label='E[self-estimate | score] = score/2')
a.fill_between(x, 0.5*x, x, where=x < 0, color='#b44c20', alpha=0.15)
a.axhline(0, color='0.8', linewidth=0.7)
a.axvline(0, color='0.8', linewidth=0.7)
a.set(xlabel='Observed standardized test score', ylabel='Conditional mean self-estimate', title='C. Selection on a noisy score')
a.text(-2.3, 1.65, 'Low observed scores:\nmean estimate exceeds score', fontsize=8, color='#8d3719')
a.legend(fontsize=7, loc='lower right')
a.grid(alpha=0.18)
fig.suptitle('Two toy models: confidence ranking does not establish calibration', fontsize=13)
fig.tight_layout(rect=(0, 0.025, 1, 0.91), w_pad=1.6)
fig.savefig(Path.cwd() / '2022-calibration-resolution.png', dpi=100, facecolor='white', transparent=False)
plt.close(fig)
print(json.dumps({'group_sizes': [100]*4, 'correct': correct.tolist(), 'incorrect': incorrect.tolist(), 'type2_auc': auc, 'calibrated_average_confidence': float(p.mean()), 'shifted_average_confidence': float((p+0.12).mean()), 'observed_accuracy': float(correct.sum()/400), 'shifted_calibration_bias': 0.12, 'gaussian_example_lambda': 0.5}))
