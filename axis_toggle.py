import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


fig = plt.figure(figsize=(5,3))
# fig.subplots_adjust(hspace=0.3)

# gs = GridSpec(2, 2, width_ratios=[1,0.1], height_ratios=[1,0.1])
# gs = GridSpec(1, 2, width_ratios=[1,0.1], height_ratios=[1,1])
gs = GridSpec(1, 2, width_ratios=[1,0.1])

        # ax.set_yticks([])
        # gs[1].set_xticks([])
        # gs[1].set_yticks([])
ax0 = fig.add_subplot(gs[0])
cax1 = fig.add_subplot(gs[1])

cax1.remove()

cax1 = fig.add_subplot(gs[1])
cax1.get_yaxis().set_visible(False)
cax1.get_xaxis().set_visible(False)

plt.show()