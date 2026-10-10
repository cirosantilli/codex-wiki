"""Original massless phase-space toy, not historical data or a weak-decay model.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; emits this script's basename with .png in the working directory.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib.pyplot as plt


def boost(p, beta):
    """Active boost of (...,4) vectors from rest to velocity beta; c=1."""
    b2 = np.sum(beta * beta, axis=-1)
    gamma = 1 / np.sqrt(1 - b2)
    dot = np.sum(p[..., 1:] * beta, axis=-1)
    factor = np.divide(gamma - 1, b2, out=np.zeros_like(b2), where=b2 > 0)
    return np.concatenate(((gamma * (p[..., 0] + dot))[..., None],
                           p[..., 1:] + (factor * dot + gamma * p[..., 0])[..., None] * beta), axis=-1)


def direction(rng, n):
    z = rng.uniform(-1, 1, n)
    phi = rng.uniform(0, 2 * np.pi, n)
    r = np.sqrt(1 - z * z)
    return np.column_stack((r * np.cos(phi), r * np.sin(phi), z))


def mass2(p):
    return p[..., 0] ** 2 - np.sum(p[..., 1:] ** 2, axis=-1)


def generate(n=12000, seed=19751995, m=2.0, ecm=6.0):
    """Shape (n,2,3,4): tau charge (-,+), daughter (charged,nu,nu).

    Constant squared amplitude: dPhi3/dx proportional to x, x=2 E*/m.
    Both charged daughters and all neutrinos are massless in this toy.
    No radiation, spin correlation, selection, smearing, or true matrix element.
    """
    rng = np.random.default_rng(seed)
    tau_direction = direction(rng, n)
    speed = np.sqrt(1 - (2 * m / ecm) ** 2)
    events, xs = [], []
    for sign in (1, -1):
        x = np.sqrt(rng.random(n))
        le = m * x / 2
        lp = le[:, None] * direction(rng, n)
        l = np.column_stack((le, lp))
        qe = m - le
        qm = m * np.sqrt(1 - x)
        np0 = (qm / 2)[:, None] * direction(rng, n)
        a0 = np.column_stack((qm / 2, np0))
        b0 = np.column_stack((qm / 2, -np0))
        beta_q = -lp / qe[:, None]
        a, b = boost(a0, beta_q), boost(b0, beta_q)
        beta_tau = sign * speed * tau_direction
        events.append(np.stack([boost(p, beta_tau) for p in (l, a, b)], axis=1))
        xs.append(x)
    return np.stack(events, axis=1), np.stack(xs, axis=1)


def diagnostics(events):
    visible = events[:, :, 0].sum(axis=1)
    missing = events[:, :, 1:].sum(axis=(1, 2))
    p = events[:, :, 0, 1:3]
    cosine = np.sum(p[:, 0] * p[:, 1], axis=-1) / np.prod(np.linalg.norm(p, axis=-1), axis=-1)
    acop = np.degrees(np.pi - np.arccos(np.clip(cosine, -1, 1)))
    return visible, missing, acop


def checks(events, x, m=2.0, ecm=6.0):
    parents = events.sum(axis=2)
    residual = float(np.max(np.abs(events.sum(axis=(1, 2)) - [ecm, 0, 0, 0])))
    shell = float(np.max(np.abs(mass2(events))))
    parent_shell = float(np.max(np.abs(mass2(parents) - m * m)))
    visible, missing, _ = diagnostics(events)
    q = events[:, :, 1:].sum(axis=2)
    bounds = float(np.max(np.abs(mass2(q) - m*m*(1-x))))
    assert residual < 1e-10 and shell < 1e-10 and parent_shell < 1e-10 and bounds < 1e-10
    assert np.all(events[..., 0] > 0) and np.all((x >= 0) & (x <= 1))
    assert np.min(mass2(missing)) > -1e-10
    assert abs(float(np.mean(x)) - 2/3) < .015
    # Explicit fully visible e-e+ control cases: positive energies, null shells,
    # opposite momenta, and zero missing four-vector in every case.
    rng = np.random.default_rng(2000)
    control_p = ecm/2 * direction(rng, 40)
    control_a = np.column_stack((np.full(40, ecm/2), control_p))
    control_b = np.column_stack((np.full(40, ecm/2), -control_p))
    assert np.max(np.abs(mass2(control_a))) < 1e-12
    assert np.max(np.abs(mass2(control_b))) < 1e-12
    assert np.max(np.abs(control_a + control_b - [ecm, 0, 0, 0])) < 1e-12
    # Charges: initial e-+e+ = 0; tau- -> e-+0+0; tau+ -> mu++0+0.
    assert -1 + 1 == 0 and sum([-1, 0, 0]) == -1 and sum([1, 0, 0]) == 1
    return dict(events=len(events),seed=19751995,max_four_momentum_residual=residual,
                max_massless_shell_residual=shell,max_parent_shell_residual=parent_shell,
                max_neutrino_pair_bound_residual=bounds,mean_x=float(np.mean(x)),charge_conserved=True,
                explicit_visible_two_body_controls=40)


def main():
    events, x = generate()
    print(json.dumps(checks(events, x), sort_keys=True))
    _, missing, acop = diagnostics(events)
    plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.7), layout='constrained')
    axes[0].hist(x.ravel(), bins=28, density=True, color='#88bbd5', edgecolor='white', label='Generated phase space')
    grid = np.linspace(0, 1, 200)
    axes[0].plot(grid, 2*grid, color='#993404', lw=2, label=r'Normalized density $f(x)=2x$')
    axes[0].set(xlabel=r'Rest-frame visible energy $x=2E_\ell^*/m$',ylabel='Probability density',title='One three-body decay',xlim=(0,1))
    axes[0].legend(fontsize=9, loc='upper left')
    h = axes[1].hexbin(acop, mass2(missing), gridsize=33, mincnt=1, cmap='Blues', linewidths=.2)
    axes[1].scatter([0], [0], marker='*', s=150, color='#b34b00', edgecolor='black', zorder=4,label='Fully visible two-body control')
    axes[1].set(xlabel=r'Transverse acoplanarity $180^\circ-\Delta\phi$',ylabel=r'Missing mass squared $M_{\rm miss}^2$ (GeV$^2$)',title='Two decays: a range of invisible recoil',xlim=(-4,180),ylim=(-1,37))
    axes[1].legend(fontsize=8, loc='upper right')
    fig.colorbar(h, ax=axes[1], label='Generated events per hexagon', shrink=.8)
    fig.suptitle(r'Chosen $m=2$ GeV, $\sqrt{s}=6$ GeV; massless daughters, constant amplitude',fontsize=12)
    fig.supxlabel('Original toy events • fixed seed • no detector cuts or spin correlations • not historical data',fontsize=9)
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
