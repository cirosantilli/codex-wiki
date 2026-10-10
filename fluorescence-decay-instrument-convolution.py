"""Plot a stipulated fluorescence decay, timing response and background.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
No experimental data; writes the matching PNG to the current directory.
"""
from math import erfc
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def model(t, tau=4.0, sigma=0.6):
    """Exact convolution of exp(-t/tau)H(t) with a unit-area Gaussian."""
    intrinsic = np.exp(-np.maximum(t, 0)/tau)*(t >= 0)
    response = np.exp(-0.5*(t/sigma)**2)/(sigma*np.sqrt(2*np.pi))
    complement = np.array([erfc(float((sigma*sigma/tau-x)/(np.sqrt(2)*sigma))) for x in t])
    convolved = 0.5*np.exp(sigma*sigma/(2*tau*tau)-t/tau)*complement
    return intrinsic, response, convolved


def main():
    plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
    t = np.linspace(-2.5, 24, 2651)
    intrinsic, response, convolved = model(t)
    background = 0.025
    fig, axs = plt.subplots(1, 2, figsize=(10, 4.5), dpi=130, facecolor='white')
    axs[0].plot(t, intrinsic, '--', color='#18845b', label='Intrinsic decay')
    axs[0].plot(t, convolved, color='#2460a7', lw=2, label='Decay ∗ timing response')
    axs[0].plot(t, response/response.max(), ':', color='#7753a6', label='Response (unit peak)')
    axs[0].set(xlim=(-2.5, 15), ylim=(-0.02, 1.1), ylabel='Common signal units', title='Finite timing broadens the onset')
    axs[0].legend(loc='upper right', fontsize=9)
    axs[1].semilogy(t, convolved, color='#2460a7', lw=2, label='Background removed')
    axs[1].semilogy(t, convolved+background, color='#b65e0a', lw=2, label='With background')
    axs[1].axhline(background, color='#777777', ls=':', label='Background level')
    axs[1].set(xlim=(0, 24), ylim=(0.001, 1.1), ylabel='Common signal units (log scale)', title='Background flattens the tail')
    axs[1].legend(loc='upper right', fontsize=9)
    for ax in axs:
        ax.set_xlabel('Delay from excitation reference (ns)')
        ax.grid(alpha=0.2)
        ax.spines[['top', 'right']].set_visible(False)
    fig.suptitle('Synthetic model: lifetime 4 ns; Gaussian timing width σ = 0.6 ns', fontsize=14)
    fig.text(0.5, 0.025, 'No measured data. Background = 0.025; response centre = 0 ns. Only response display is peak-normalized.',
             ha='center', fontsize=9)
    fig.subplots_adjust(left=0.075, right=0.98, top=0.82, bottom=0.19, wspace=0.28)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
