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

    def get_ray(self, tau, f0, solz, senz, phi, type="I"):
        pts = (tau, solz, senz)

        if type == "I":

            ray_i = 0
            for i in range(3):
                interp_I = RegularGridInterpolator(
                    self.points,
                    self.tab_coef[:, 0, :, :, i],
                )
                ray_coef_I = interp_I(pts)
                ray_i = ray_i + ray_coef_I * np.cos(np.deg2rad(i * phi))
            return f0 * ray_i
        else:

            ray = np.zeros(3)

            for i in range(3):
                for j in range(3):
                    interp = RegularGridInterpolator(
                        self.points, self.tab_coef[:, i, :, :, j]
                    )
                    ray_coef = interp(pts)
                    ray[i] = ray[i] + ray_coef * np.cos(np.deg2rad(j * phi))
            return f0 * ray
