# Demo to create 2 colorbars (one vertical, one horizontal) and on mouse-click, alternate
# between deleting and recreating the horiz one.

import sys
from PyQt5 import QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg 
from matplotlib.figure import Figure
from matplotlib import colormaps
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
import matplotlib.pyplot as plt
import numpy as np


class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MplWidget, self).__init__(parent)

        self.figure = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.figure)

        vertical_layout = QtWidgets.QVBoxLayout(self)
        vertical_layout.addWidget(self.canvas)

        self.ax0 = self.figure.add_subplot(111, adjustable='box')   # in vis_tab.py
        self.ax0_divider = make_axes_locatable(self.ax0)

        # self.cax1 = None
        # self.cax2 = None
        self.cax1 = self.ax0_divider.append_axes("right", size="4%", pad="4%")
        self.cax2 = self.ax0_divider.append_axes("bottom", size="4%", pad="7%")

        self.flag = False

        self.plot_contours()
        self.plot_cells()

        self.canvas.mpl_connect("button_press_event", self.redraw)

    def plot_contours(self):
        x = np.arange(1, 10)
        y = x.reshape(-1, 1)
        h = x * y
        cplot = self.ax0.contourf(h)
        if self.cax1 is None:
            self.ax0_divider = make_axes_locatable(self.ax0)
            self.cax1 = self.ax0_divider.append_axes("right", size="4%", pad="4%")
        self.cbar1 = self.figure.colorbar(cplot, cax=self.cax1)
        self.cbar1.ax.set_ylabel('contour label')

    def plot_cells(self):
        cm = colormaps.get_cmap('RdYlBu')
        xv = range(8)
        # print("xv=",xv)
        yv = np.random.uniform(low=0.0, high=1.0, size=8)
        # print("yv.min(), max()= ",yv.min(),yv.max())
        z = yv
        self.flag = not self.flag
        if self.flag:   # show colorbar
            if self.cax2 is None:
            # if self.ax0_divider is None:
                # self.ax0_divider = make_axes_locatable(self.ax0)
                self.cax2 = self.ax0_divider.append_axes("bottom", size="4%", pad="7%")
                print("type(self.cax2)= ",type(self.cax2))
                # print("len(self.cax2)= ",len(self.cax2))
                print("type(self.ax0_divider)= ",type(self.ax0_divider))
                print("self.ax0_divider= ",self.ax0_divider)
                # self.cax2 = self.cax_horiz

            sc = self.ax0.scatter(xv, xv, c=z, vmin=yv.min(), vmax=yv.max(), s=35, cmap=cm)
            self.cbar2 = self.figure.colorbar(sc, orientation='horizontal', cax=self.cax2)
            self.cbar2.ax.set_xlabel('cells colors')
            print("self.cbar2.ax=",self.cbar2.ax)

        else:  # don't show colorbar
            if self.cax2 is not None:
                self.cax2.remove()
                self.cax2 = None
            sc = self.ax0.scatter(xv, xv, c=z, vmin=yv.min(), vmax=yv.max(), s=35)

    def redraw(self, event):
        # print("redraw()")
        self.ax0.cla()
        self.plot_contours()
        self.plot_cells()
        self.canvas.update()
        self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MplWidget()
    w.show()
    sys.exit(app.exec_())
