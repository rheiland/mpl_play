"""
"""

from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
import numpy as np

# from matplotlib.artist import Artist
# from matplotlib.lines import Line2D

class ColorBarInteractor:
    """
    Key-bindings
      'h' toggle horizontal colorbar
      'v' toggle vertical colorbar
    """
    def __init__(self, ax, myobj):

        # canvas = poly.figure.canvas
        # self.canvas = self.figure.canvas

        print("myobj= ",myobj)
        self.ax = ax
        canvas = myobj.figure.canvas
        print("canvas= ",canvas)

        self.ax_divider = make_axes_locatable(self.ax)
        # self.cax1 = self.ax_divider.append_axes("right", size="4%", pad="4%")
        self.cax2 = self.ax_divider.append_axes("bottom", size="4%", pad="7%")

        # sc = self.ax.scatter(xv, xv, c=z, vmin=yv.min(), vmax=yv.max(), s=35, cmap=cm)
        # sc = self.ax.scatter(xv, xv, c=z, vmin=yv.min(), vmax=yv.max(), s=35)

        # self.cbar2 = self.figure.colorbar(myobj, orientation='horizontal', cax=self.cax2)
        self.cbar2 = myobj.figure.colorbar(myobj, orientation='horizontal', cax=self.cax2)
        self.cbar2.ax.set_xlabel('cells colors')

        # canvas = sc.figure.canvas
        # canvas = self.figure.canvas
        # self.canvas.mpl_connect('key_press_event', self.on_key_press)
        # self.canvas.mpl_connect('draw_event', self.on_draw)
        canvas.mpl_connect('key_press_event', self.on_key_press)
        canvas.mpl_connect('draw_event', self.on_draw)
        # self.canvas = canvas

    def on_draw(self, event):
        print("on_draw()")
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        # self.ax.draw_artist(self.poly)
        # self.ax.draw_artist(self.line)
        # do not need to blit here, this will fire before the screen is
        # updated

    def on_key_press(self, event):
        """Callback for key presses."""
        print("got key= ",event.key)
        if not event.inaxes:
            return
        if event.key == 'h':
            self.horiz = not self.horiz
        elif event.key == 'v':
            self.vert = not self.vert
        if self.line.stale:
            self.canvas.draw_idle()

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    # ax.add_patch(poly)
    # p = PolygonInteractor(ax, poly)
    xv = range(8)
    yv = np.random.uniform(low=0.0, high=1.0, size=8)
    z = yv

    # fig, ax = plt.subplots()
    # ax.add_patch(poly)
    sc = ax.scatter(xv, xv, c=z, vmin=yv.min(), vmax=yv.max(), s=35)
    ColorBarInteractor(ax, sc)

    # ax.set_title('Click and drag a point to move it')
    # ax.set_xlim((-2, 2))
    # ax.set_ylim((-2, 2))
    plt.show()
