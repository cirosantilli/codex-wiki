"""Explicit calculated Barkhausen jump/filter model, never measured data.
Python 3.14 / numpy 2.3.5 / matplotlib 3.10.7. Emits basename.png to CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

TIMES_MS = np.array([1.0, 3.0, 3.2])
JUMPS = np.array([1000., 500., 500.])  # A/m
K = 4*np.pi*1e-11  # V s m/A, stipulated ideal geometry


def response(t_ms, tau_ms):
    """Exact causal exponential output and its integral; unit gain."""
    v_mV = np.zeros_like(t_ms)
    area_mV_ms = np.zeros_like(t_ms)
    for ti, jump in zip(TIMES_MS, JUMPS):
        u = t_ms-ti
        mask = u >= 0
        # K*jump in V s -> mV ms uses 1e6; tau stays in ms.
        a = -K*jump*1e6
        v_mV[mask] += a/tau_ms*np.exp(-u[mask]/tau_ms)
        area_mV_ms[mask] += a*(-np.expm1(-u[mask]/tau_ms))
    return v_mV, area_mV_ms


def zero_dc_area(t_ms, tau_ms=.5, highpass_ms=1.):
    """Integral after extra zero-DC stage; analytic convolution result."""
    out = np.zeros_like(t_ms)
    for ti, jump in zip(TIMES_MS, JUMPS):
        u = t_ms-ti
        mask = u >= 0
        out[mask] += -K*jump*1e6*highpass_ms/(highpass_ms-tau_ms)*(
            np.exp(-u[mask]/highpass_ms)-np.exp(-u[mask]/tau_ms))
    return out


def main():
    t = np.linspace(0, 10, 50001)
    magnetization = sum(jump*(t >= ti) for ti, jump in zip(TIMES_MS, JUMPS))
    plt.rcParams.update({'font.size': 12, 'axes.spines.top': False, 'axes.spines.right': False})
    fig, axs = plt.subplots(3, 1, figsize=(11, 9), dpi=110, sharex=True)
    fig.patch.set_facecolor('white')
    fig.suptitle('Discrete jumps → induced voltage → filtered readout', fontsize=19, weight='bold', y=.98)
    fig.text(.12, .935, 'Constructed model only • no measured traces • unit voltage gain', fontsize=12, color='#444444')
    axs[0].plot(t, magnetization, color='#245d8c', lw=2)
    axs[0].set_ylabel(r'$M-M_0$ (A/m)')
    axs[0].set_ylim(-130, 2300)
    axs[0].text(5.0, 850, 'Jumps: 1000, 500, 500 A/m\nTimes: 1.0, 3.0, 3.2 ms', fontsize=12)
    axs[0].set_title('A   Stipulated magnetization staircase', loc='left', fontsize=13)
    colors = ['#ab571a', '#245d8c']
    for tau, color in zip([.1, .5], colors):
        v, area = response(t, tau)
        axs[1].plot(t, v, lw=1.8, color=color, label=rf'$\tau={tau:.2f}$ ms')
    axs[1].set_ylabel(r'$v_{\rm out}$ (mV)')
    axs[1].set_ylim(-1.4, .12)
    axs[1].set_title('B   Same jump areas; different peaks and tails', loc='left', fontsize=13)
    axs[1].legend(loc='lower right', frameon=False)
    axs[1].annotate('Nearby events overlap', xy=(3.2, -.21), xytext=(4.5, -.55),
                    arrowprops={'arrowstyle':'->', 'color':'#444444'}, fontsize=11)
    _, area = response(t, .5)
    axs[2].plot(t, area, color=colors[1], lw=2, label='Low-pass only')
    axs[2].plot(t, zero_dc_area(t), color='#9b3f69', lw=2, ls='--', label='Low-pass + zero-DC stage')
    target = -K*JUMPS.sum()*1e6
    axs[2].axhline(target, color='#777777', lw=1, ls=':')
    axs[2].text(5.2, target-.027, f'Total area → {target:.6f} mV ms', fontsize=11)
    axs[2].set_ylim(-.30, .035)
    axs[2].set_ylabel('Cumulative area\n(mV ms)')
    axs[2].set_title('C   Complete signed area depends on DC response', loc='left', fontsize=13)
    axs[2].legend(loc='center right', frameon=False)
    axs[2].set_xlabel('Time (ms)')
    for ax in axs:
        ax.set_xlim(0, 10)
        ax.axhline(0, color='#999999', lw=.7)
        ax.grid(alpha=.16)
    fig.subplots_adjust(left=.13, right=.975, top=.875, bottom=.09, hspace=.47)
    fig.savefig(Path(__file__).stem+'.png', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
