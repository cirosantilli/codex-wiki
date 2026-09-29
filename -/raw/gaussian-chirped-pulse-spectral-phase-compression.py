"""Original Gaussian-envelope FFT experiment and independent moment checks.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7; run from _media.
A has units sqrt(W); |A|² is power. Fourier convention B(Ω)=∫A(t)exp(+iΩt)dt,
A(t)=(2π)^−1∫B(Ω)exp(−iΩt)dΩ. All plotted time widths concern power.
fs units are used numerically, with A scaled so ∫|A|²dt_fs=1 nJ.
No traces or parameters are taken from an experiment.
"""

from pathlib import Path
import json

import matplotlib.pyplot as plt
import numpy as np


def calculate(n=2**17, dt_fs=0.125):
    tau_fs, beta_fs2, residual_fs2, cubic_fs3 = 30.0, 3000.0, 300.0, 20000.0
    sigma_t = tau_fs / (2 * np.sqrt(2 * np.log(2)))
    sigma_omega = 1 / (2 * sigma_t)
    t = (np.arange(n) - n // 2) * dt_fs
    omega = np.fft.fftshift(np.fft.fftfreq(n, dt_fs)) * 2 * np.pi
    domega = 2 * np.pi / (n * dt_fs)
    a0 = np.exp(-t**2 / (4 * sigma_t**2)) / np.sqrt(np.sqrt(2 * np.pi) * sigma_t)
    b0 = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(a0))) * n * dt_fs

    def inverse(b):
        return np.fft.fftshift(np.fft.fft(np.fft.ifftshift(b))) / (n * dt_fs)

    spectra = {
        "seed": b0,
        "stretched": b0 * np.exp(0.5j * beta_fs2 * omega**2),
        "recovered": b0 * np.exp(0.5j * beta_fs2 * omega**2) * np.exp(-0.5j * beta_fs2 * omega**2),
        "residual_gdd": b0 * np.exp(0.5j * residual_fs2 * omega**2),
        "residual_tod": b0 * np.exp(1j * cubic_fs3 * omega**3 / 6),
        # G(Ω)=G0 exp[-Ω²/(2σg²)], σg=σΩ; divide field by sqrt(G0).
        "narrowed": b0 * np.exp(-omega**2 / (4 * sigma_omega**2)),
    }
    fields = {name: inverse(b) for name, b in spectra.items()}
    result = {}
    for name, a in fields.items():
        p = np.abs(a)**2
        energy = np.sum(p) * dt_fs
        energy_spectral = np.sum(np.abs(spectra[name])**2) * domega / (2 * np.pi)
        mean = np.sum(t * p) * dt_fs / energy
        rms = np.sqrt(np.sum((t - mean)**2 * p) * dt_fs / energy)
        assert abs(energy - energy_spectral) < 2e-13
        result[name] = {"energy_nj_divided_by_G0_if_narrowed": float(energy), "centroid_fs": float(mean), "rms_fs": float(rms), "parseval_error": float(abs(energy - energy_spectral))}
    # These analytic checks use Gaussian frequency moments, not a second FFT.
    expected = {
        "seed": (0, sigma_t), "recovered": (0, sigma_t),
        "stretched": (0, np.sqrt(sigma_t**2 + beta_fs2**2 * sigma_omega**2)),
        "residual_gdd": (0, np.sqrt(sigma_t**2 + residual_fs2**2 * sigma_omega**2)),
        "residual_tod": (cubic_fs3 * sigma_omega**2 / 2, np.sqrt(sigma_t**2 + cubic_fs3**2 * sigma_omega**4 / 2)),
        "narrowed": (0, np.sqrt(2) * sigma_t),
    }
    for name, (mean, rms) in expected.items():
        assert np.isclose(result[name]["centroid_fs"], mean, atol=1e-9)
        assert np.isclose(result[name]["rms_fs"], rms, rtol=1e-10)
    assert np.max(np.abs(fields["recovered"] - a0)) < 1e-13
    assert np.isclose(result["narrowed"]["energy_nj_divided_by_G0_if_narrowed"], 1 / np.sqrt(2))
    for name in ["seed", "stretched", "recovered", "residual_gdd", "narrowed"]:
        p = np.abs(fields[name])**2
        half = max(p) / 2
        crossing = np.flatnonzero((p[:-1] - half) * (p[1:] - half) < 0)
        roots = [t[j] + dt_fs * (half - p[j]) / (p[j+1] - p[j]) for j in crossing]
        assert len(roots) == 2
        fwhm = roots[1] - roots[0]
        assert abs(fwhm - 2 * np.sqrt(2*np.log(2)) * expected[name][1]) < 0.001
        result[name]["fwhm_fs"] = float(fwhm)
    result["conventions"] = {"dt_fs": dt_fs, "n": n, "tau0_power_fwhm_fs": tau_fs, "sigma_t_power_rms_fs": float(sigma_t), "sigma_omega_rad_per_fs": float(sigma_omega), "gdd_fs2": beta_fs2, "residual_gdd_fs2": residual_fs2, "residual_tod_fs3": cubic_fs3}
    return t, omega, fields, spectra, result


def main():
    t, omega, fields, spectra, result = calculate()
    sigma_omega = result["conventions"]["sigma_omega_rad_per_fs"]
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(2, 2, figsize=(11, 7), facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.19, top=0.86, wspace=0.26, hspace=0.54)
    fig.suptitle("Gaussian pulse compression: bandwidth and phase impose different limits", fontsize=14, y=0.97)
    fig.text(0.5, 0.91, "Chosen model: 30 fs power FWHM, 1 nJ seed; +3000 fs² stretcher, −3000 fs² compressor", ha="center", fontsize=10)
    x = omega / sigma_omega
    occupied = np.abs(x) <= 3
    ax = axes[0, 0]
    for name, label, color in [("seed", "Seed spectrum", "#334155"), ("narrowed", "After finite gain (÷G₀)", "#b45309")]:
        s = np.abs(spectra[name])**2
        ax.plot(x[occupied], s[occupied] / max(np.abs(spectra["seed"])**2), label=label, color=color, lw=2)
    ax.set(title="a  Gain can narrow the spectrum", xlabel="Angular frequency offset Ω / σΩ", ylabel="Spectral power / seed peak", xlim=(-3, 3), ylim=(0, 1.12))
    ax.legend(fontsize=9)
    ax = axes[0, 1]
    for phase, label, color in [(3000 * omega**2 / 2, "+3000 fs²", "#2171b5"),
                                (np.zeros_like(omega), "Exact cancellation", "#047857"),
                                (300 * omega**2 / 2, "Residual +300 fs²", "#c2410c"),
                                (20000 * omega**3 / 6, "Residual +20 000 fs³", "#7e22ce")]:
        ax.plot(x[occupied], phase[occupied], label=label, color=color, lw=1.6)
    ax.set(title="b  Unwrapped spectral phase", xlabel="Angular frequency offset Ω / σΩ", ylabel="Phase (rad)", xlim=(-3, 3))
    ax.legend(fontsize=8, loc="upper center")
    ax = axes[1, 0]
    ax.plot(t, np.abs(fields["stretched"])**2 * 1e3, lw=2, color="#2171b5")
    ax.set(title="c  Stretch at fixed energy", xlabel="Time (fs)", ylabel="Power (kW)", xlim=(-500, 500), ylim=(0, 4.6))
    ax.text(0.5, 0.93, f"FWHM {result['stretched']['fwhm_fs']:.2f} fs\nRMS {result['stretched']['rms_fs']:.2f} fs; energy 1 nJ", transform=ax.transAxes, ha="center", va="top", fontsize=9)
    ax = axes[1, 1]
    for name, label, color in [("recovered", "Recovered: FWHM 30 fs", "#047857"),
                                ("residual_gdd", f"Residual GDD: FWHM {result['residual_gdd']['fwhm_fs']:.2f} fs", "#c2410c"),
                                ("residual_tod", f"Residual TOD: RMS {result['residual_tod']['rms_fs']:.2f} fs", "#7e22ce"),
                                ("narrowed", "Narrowed (÷G₀): FWHM 42.43 fs", "#b45309")]:
        ax.plot(t, np.abs(fields[name])**2 * 1e3, label=label, color=color, lw=1.8)
    ax.set(title="d  Recovery and three limitations", xlabel="Time (fs)", ylabel="Power (kW)", xlim=(-90, 140), ylim=(0, 48))
    ax.legend(fontsize=7.7, loc="upper right")
    fig.text(0.5, 0.055, "FFT of the complex envelope; power = |A|². Phase-only operations conserve energy (Parseval).\nTOD gives an asymmetric pulse: its RMS width is stated without converting it to a Gaussian FWHM.\nFinite-gain curve divides out G₀, retaining the filter's energy loss; no measured pulse traces.", ha="center", va="center", fontsize=9)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white")
    plt.close(fig)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
