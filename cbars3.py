"""
===========
Poly Editor
===========

This is an example to show how to build cross-GUI applications using
Matplotlib event handling to interact with objects on the canvas.

.. note::
    This example exercises the interactive capabilities of Matplotlib, and this
    will not appear in the static documentation. Please run this code on your
    machine to see the interactivity.

    You can copy and paste individual parts, or download the entire example
    using the link at the bottom of the page.
"""

import numpy as np

from matplotlib.artist import Artist
from matplotlib.lines import Line2D


def dist_point_to_segment(p, s0, s1):
    """
    Get the distance from the point *p* to the segment (*s0*, *s1*), where
    *p*, *s0*, *s1* are ``[x, y]`` arrays.
    """
    s01 = s1 - s0
    s0p = p - s0
    if (s01 == 0).all():
        return np.hypot(*s0p)
    # Project onto segment, without going past segment ends.
    p1 = s0 + np.clip((s0p @ s01) / (s01 @ s01), 0, 1) * s01
    return np.hypot(*(p - p1))


class PolygonInteractor:
    """
    A polygon editor.

    Key-bindings

      't' toggle vertex markers on and off.  When vertex markers are on,
          you can move them, delete them

      'd' delete the vertex under point

      'i' insert a vertex at point.  You must be within epsilon of the
          line connecting two existing vertices

    """

    showverts = True
    epsilon = 5  # max pixel distance to count as a vertex hit

    def __init__(self, ax, poly):
        if poly.figure is None:
            raise RuntimeError('You must first add the polygon to a figure '
                               'or canvas before defining the interactor')
        self.ax = ax
        print("poly= ",poly)
        canvas = poly.figure.canvas
        print("canvas= ",canvas)
        self.poly = poly

        x, y = zip(*self.poly.xy)
        self.line = Line2D(x, y,
                           marker='o', markerfacecolor='r',
                           animated=True)
        self.ax.add_line(self.line)

        # cb = poly.figure.colorbar(self.line)

        # self.cid = self.poly.add_callback(self.poly_changed)
        # self._ind = None  # the active vert

        canvas.mpl_connect('draw_event', self.on_draw)
        # canvas.mpl_connect('button_press_event', self.on_button_press)
        canvas.mpl_connect('key_press_event', self.on_key_press)
        # canvas.mpl_connect('button_release_event', self.on_button_release)
        # canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.canvas = canvas

    def on_draw(self, event):
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        # self.ax.draw_artist(self.poly)
        self.ax.draw_artist(self.line)
        # do not need to blit here, this will fire before the screen is
        # updated

    def on_key_press(self, event):
        """Callback for key presses."""
        print("got key= ",event.key)
        if not event.inaxes:
            return
        if event.key == 'h':
            pass
        elif event.key == 'v':
            pass

        if self.line.stale:
            self.canvas.draw_idle()

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    from matplotlib.patches import Polygon
    # from matplotlib.patches import Circle

    # theta = np.arange(0, 2*np.pi, 0.1)
    tdel = 2*np.pi / 10
    theta = np.arange(0, 2*np.pi + 0.1, tdel)
    print("theta=",theta)
    r = 4.0
    r = 1.5
    r = 1.0

    # xs = r * np.cos(theta)
    # ys = r * np.sin(theta)
    xs = theta
    ys = np.sin(theta)

    poly = Polygon(np.column_stack([xs, ys]), animated=True)
    # circles = Circle(np.column_stack([xs, ys]), animated=True)
    # circles = Circle(np.column_stack([xs, ys]), animated=True)

    fig, ax = plt.subplots()
    ax.add_patch(poly)
    p = PolygonInteractor(ax, poly)

    ax.set_title('Press h to toggle horiz colorbar')
    ax.set_xlim((-0.5, 6.5))
    ax.set_ylim((-2, 2))
    plt.show()
