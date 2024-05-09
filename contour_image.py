"""
=============
Contour Image
=============

Test combinations of contouring, filled contouring, and image plotting.
For contour labelling, see also the :doc:`contour demo example
</gallery/images_contours_and_fields/contour_demo>`.

The emphasis in this demo is on showing how to make contours register
correctly on images, and on how to get both of them oriented as desired.
In particular, note the usage of the :ref:`"origin" and "extent"
<imshow_extent>` keyword arguments to imshow and
contour.
"""
import sys
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm

vert_cbar = None
horiz_cbar = None

def on_press(event):
    global vert_cbar, horiz_cbar
    # print('press', event.key)
    # sys.stdout.flush()
    # if event.key == 'x':
    #     visible = xl.get_visible()
    #     xl.set_visible(not visible)
    #     fig.canvas.draw()
    if event.key == 'v':
        if vert_cbar is not None:
            vert_cbar.remove()
            vert_cbar = None
        else:
            vert_cbar = fig.colorbar(cset1, ax=ax)
        fig.canvas.draw()
    elif event.key == 'h':
        if horiz_cbar is not None:
            horiz_cbar.remove()
            horiz_cbar = None
        else:
            horiz_cbar = fig.colorbar(cset1, ax=ax, orientation='horizontal')
        fig.canvas.draw()

delta = 0.5
extent = (-3, 4, -4, 3)
x = np.arange(-3.0, 4.001, delta)
y = np.arange(-4.0, 3.001, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

# Boost the upper limit to avoid truncation errors.
levels = np.arange(-2.0, 1.601, 0.4)

norm = cm.colors.Normalize(vmax=abs(Z).max(), vmin=-abs(Z).max())
cmap = cm.PRGn

fig, ax = plt.subplots(nrows=1, ncols=1)
fig.subplots_adjust(hspace=0.3)

cset1 = ax.contourf(X, Y, Z, levels, norm=norm,
                        cmap=cmap.resampled(len(levels) - 1))
ax.set_title('Filled contours')
vert_cbar = fig.colorbar(cset1, ax=ax)
horiz_cbar = fig.colorbar(cset1, ax=ax, orientation='horizontal')

fig.canvas.mpl_connect('key_press_event', on_press)

# xl = ax.set_xlabel('easy come, easy go')
ax.set_title('h to toggle horiz cbar; v to toggle vertical cbar')

# fig.tight_layout()
plt.show()


# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`
#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`
#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`
#    - `matplotlib.colors.Normalize`
