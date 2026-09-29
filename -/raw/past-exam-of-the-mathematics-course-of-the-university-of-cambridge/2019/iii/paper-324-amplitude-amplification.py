#!/usr/bin/env python3
"""Illustrate amplitude amplification, saving a 1000 x 480 PNG to cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

theta = 0.18
fig, (plane, success) = plt.subplots(1, 2, figsize=(10, 4.8), dpi=100, facecolor='white')
for ax in (plane, success):
    ax.set_facecolor('white')
arc = np.linspace(0, np.pi, 240)
plane.plot(np.cos(arc), np.sin(arc), color='#bbbbbb', lw=1.2)
plane.axhline(0, color='#777777', lw=1)
plane.axvline(0, color='#777777', lw=1)
colors = ['#356a94', '#ca8638', '#36875c']
for j, color in zip([0, 1, 4], colors):
    angle = (2*j+1)*theta
    endpoint = np.array([np.cos(angle), np.sin(angle)])
    plane.annotate('', xy=endpoint, xytext=(0, 0),
                   arrowprops={'arrowstyle': '-|>', 'lw': 2.4, 'color': color, 'mutation_scale': 14})
    label = rf'$j={j}$'
    if j == 0:
        plane.text(.68, .07, label, color=color, fontsize=12)
    elif j == 1:
        plane.text(.61, .61, label, color=color, fontsize=12)
    else:
        plane.text(-.29, .84, label, color=color, fontsize=12)
# One iteration adds the same angle 2 theta.
angle = np.linspace(theta, 3*theta, 50)
plane.plot(.48*np.cos(angle), .48*np.sin(angle), color='#777777', lw=1.3)
plane.text(.39, .22, r'$2\theta$', fontsize=11)
plane.set_aspect('equal')
plane.set_xlim(-.4, 1.2)
plane.set_ylim(-.13, 1.2)
plane.set_xticks([])
plane.set_yticks([])
plane.set_xlabel(r'Bad amplitude: $\cos((2j+1)\theta)$', fontsize=10)
plane.set_ylabel(r'Good amplitude: $\sin((2j+1)\theta)$', fontsize=10)
plane.set_title('Each iteration rotates the state', fontsize=12)

iterations = np.arange(13)
probability = np.sin((2*iterations+1)*theta)**2
success.plot(iterations, probability, color='#356a94', marker='o', lw=1.8, ms=5)
for j, color in zip([0, 1, 4], colors):
    success.scatter(j, probability[j], color=color, s=65, zorder=4)
success.annotate('Stop near the first maximum', xy=(4, probability[4]), xytext=(5.1, .85),
                 arrowprops={'arrowstyle': '->', 'color': '#555555'}, fontsize=10)
success.text(.3, .12, rf'Initial probability $p={np.sin(theta)**2:.3f}$', fontsize=10)
success.set_xlim(-.3, 12.3)
success.set_ylim(-.04, 1.08)
success.set_xticks(np.arange(0, 13, 2))
success.set_xlabel('Number of iterations j', fontsize=11)
success.set_ylabel('Good-outcome probability', fontsize=11)
success.set_title(r'$\Pr(\mathrm{good})=\sin^2((2j+1)\theta)$', fontsize=12)
success.grid(alpha=.2)
fig.suptitle(r'Amplitude amplification with $\theta=0.18$ radians', fontsize=14)
fig.subplots_adjust(left=.075, right=.98, bottom=.15, top=.83, wspace=.36)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100, facecolor='white')
plt.close(fig)
