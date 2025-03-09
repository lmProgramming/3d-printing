from trimesh import Trimesh
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def set_axes_equal(ax: Axes3D) -> None:

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


def visualize_stl(stl: Trimesh) -> None:
    fig: plt.Figure = plt.figure()
    ax: Axes3D = fig.add_subplot(projection='3d')

    ax.plot_trisurf(stl.vertices[:, 0], stl.vertices[:, 1],
                    stl.vertices[:, 2], triangles=stl.faces)

    set_axes_equal(ax)
    plt.show()
