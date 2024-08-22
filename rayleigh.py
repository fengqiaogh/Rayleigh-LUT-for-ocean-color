import h5py
import numpy as np
from scipy.interpolate import RegularGridInterpolator


class Rayleigh:
    def __init__(self) -> None:
        with h5py.File("Rayleigh.h5") as f:
            self.tab_solz = f["Solar zenith angle"][()]
            self.tab_senz = f["Sensor zenith angle"][()]
            self.tab_coef = f["Radiance coef"][()]

        self.tab_tau = np.arange(0.002, 0.4 + 0.002, 0.002)
        self.points = (self.tab_tau, self.tab_solz, self.tab_senz)

        self.interp_I = [
            RegularGridInterpolator(
                self.points,
                self.tab_coef[:, 0, :, :, 0],
            ),
            RegularGridInterpolator(
                self.points,
                self.tab_coef[:, 0, :, :, 1],
            ),
            RegularGridInterpolator(
                self.points,
                self.tab_coef[:, 0, :, :, 2],
            ),
        ]
        self.interp_Q = [
            RegularGridInterpolator(
                self.points,
                self.tab_coef[:, 1, :, :, 0],
            ),
            RegularGridInterpolator(
                self.points,
                self.tab_coef[:, 1, :, :, 1],
            ),
            RegularGridInterpolator(
                self.points,
                self.tab_coef[:, 1, :, :, 2],
            ),
        ]
        self.interp_U = [
            RegularGridInterpolator(
                self.points,
                self.tab_coef[:, 2, :, :, 0],
            ),
            RegularGridInterpolator(
                self.points,
                self.tab_coef[:, 2, :, :, 1],
            ),
            RegularGridInterpolator(
                self.points,
                self.tab_coef[:, 2, :, :, 2],
            ),
        ]

    def get_ray(self, tau, f0, solz, senz, phi, type="I"):
        pts = (tau, solz, senz)

        if type == "I":
            ray_i = (
                self.interp_I[0](pts)
                + self.interp_I[1](pts) * np.cos(np.deg2rad(1 * phi))
                + self.interp_I[2](pts) * np.cos(np.deg2rad(2 * phi))
            )
            return f0 * ray_i

        elif type == "Q":
            ray_q = (
                self.interp_Q[0](pts)
                + self.interp_Q[1](pts) * np.cos(np.deg2rad(1 * phi))
                + self.interp_Q[2](pts) * np.cos(np.deg2rad(2 * phi))
            )
            return f0 * ray_q

        elif type == "U":
            ray_u = (
                self.interp_U[0](pts)
                + self.interp_U[1](pts) * np.cos(np.deg2rad(1 * phi))
                + self.interp_U[2](pts) * np.cos(np.deg2rad(2 * phi))
            )

            return f0 * ray_u
