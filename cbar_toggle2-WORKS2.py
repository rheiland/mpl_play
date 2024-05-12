import sys
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

cbar_flag = True

def on_key_press(event):
    print("key= ",event.key)
    global cbar_flag, cax1, fig
    sys.stdout.flush()
    if event.key == 'h':
        cbar_flag = not cbar_flag
        if cbar_flag:
            print('create cax1')
            cax1 = fig.add_subplot(gs[1])
            xv = range(8)
            yv = np.random.uniform(low=0.0, high=1.0, size=8)
            z = yv
            sc = ax0.scatter(xv, xv, c=z, vmin=yv.min(), vmax=yv.max(), s=35)
            cbar1 = fig.colorbar(sc, cax=cax1)
        else:
            print('remove cax1')
            # cax1.get_xaxis().set_visible(False)
            # cax1.get_yaxis().set_visible(False)
            # cax1.set_xticks([])
            # cax1.set_yticks([])
            cax1.remove()   # same as "clear"?

        fig.canvas.draw()


fig = plt.figure(figsize=(5,3))

gs = GridSpec(1, 2, width_ratios=[1,0.1])
ax0 = fig.add_subplot(gs[0])
cax1 = fig.add_subplot(gs[1])

xv = range(8)
yv = np.random.uniform(low=0.0, high=1.0, size=8)
z = yv
sc = ax0.scatter(xv, xv, c=z, vmin=yv.min(), vmax=yv.max(), s=35)
cbar1 = fig.colorbar(sc, cax=cax1)

fig.canvas.mpl_connect('key_press_event', on_key_press)

plt.show()