from scipy import optimize

from juno.juno_custom.elements.Herschel import equations as eq
from juno.juno_custom.elements.Herschel.structures import HerschelResults, HerschelSettings

import matplotlib.pyplot as plt
import numpy as np

def create_profiles(settings: HerschelSettings):
    a_list = []
    z_a_list = []
    r_b_list = []
    z_b_list = []

    for point in settings.radii:
        # print(f"Calculating for radius {point}...")
        settings.radius = point
        eq_19_ = eq.eq_19(settings)
        root = optimize.newton(
            eq_19_, 0, tol=settings.tolerance, maxiter=settings.max_iter
        )

        a_list.append(root)

        z_a_ = eq.z_a(settings)
        z_a_list.append(z_a_(root))

        r_b_ = eq.r_b(settings)
        r_b_list.append(r_b_(root))

        z_b_ = eq.z_b(settings)
        z_b_list.append(z_b_(root))

    results = HerschelResults(
        lens_roots=a_list,
        lens_x_first=settings.radii,
        lens_y_first=z_a_list,
        lens_x_second=r_b_list,
        lens_y_second=z_b_list,
    )

    return results


def display_ray_tracing(
    settings: HerschelSettings, results: HerschelResults, buffer: float = 1.1
):
    x_max = np.amax([results.lens_x_first[-1], results.lens_x_second[-1]]) * (
        buffer + 0.1
    )

    plt.figure()
    plt.xlim([-0.1 * x_max, x_max])
    plt.ylim(
        [
            settings.z_medium_o * buffer,
            (settings.z_medium_i + settings.thickness) * buffer,
        ]
    )
    skip = 5

    for i, point in enumerate(results.lens_y_first[::skip]):
        i = i * skip
        o_x = [0, results.lens_x_first[i]]
        o_y = [settings.z_medium_o, point]
        i_x = [0, results.lens_x_second[i]]
        i_y = [
            settings.z_medium_i + settings.thickness,
            results.lens_y_second[i],
        ]
        x = [results.lens_x_first[i], results.lens_x_second[i]]
        y = [point, results.lens_y_second[i]]
        plt.plot(x, y, linestyle="--")
        plt.plot(o_x, o_y, linestyle="dotted")
        plt.plot(i_x, i_y, linestyle="dotted")

    plt.plot(
        results.lens_x_first, results.lens_y_first, linewidth=2, color="red"
    )
    plt.plot(
        results.lens_x_second,
        results.lens_y_second,
        linewidth=2,
        color="red",
    )
    plt.show()