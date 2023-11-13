import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap, ListedColormap


class ncolors:
    reds   = ['#DFCFE6', '#D2B3D7', '#D776B8', '#E24FA2', '#E52786', '#D21861', '#B0084B', '#8A0039', '#7F0040']
    greens = ['#F9FDC5', '#F9FDC5', '#D2EDA0', '#B1DF90', '#8BCE81', '#64BC6F', '#3FA85B', '#288A47', '#10743C']
    purples= [f'#{40:02x}{27:02x}{53:02x}', f'#{68:02x}{39:02x}{78:02x}', f'#{131:02x}{71:02x}{117:02x}', f'#{161:02x}{90:02x}{130:02x}', f'#{189:02x}{114:02x}{142:02x}', f'#{207:02x}{141:02x}{157:02x}', f'#{224:02x}{171:02x}{175:02x}', f'#{235:02x}{202:02x}{197:02x}']
    creamy = [f'#{255:02x}{247:02x}{243:02x}', f'#{254:02x}{230:02x}{227:02x}', f'#{253:02x}{211:02x}{208:02x}', f'#{252:02x}{189:02x}{192:02x}', f'#{250:02x}{160:02x}{181:02x}', f'{247:02x}{124:02x}{169:02x}', f'{236:02x}{85:02x}{158:02x}', f'#{214:02x}{47:02x}{147:02x}', f'#{182:02x}{15:02x}{132:02x}', f'#{146:02x}{2:02x}{122:02x}', f'#{109:02x}{1:02x}{115:02x}', f'#{73:02x}{0:02x}{106:02x}']
    creamy_values = np.linspace(0, 1.0, 12)
    # #16825d


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def hex_to_rgb(hx):
    hx = hx.lstrip('#')
    return tuple(int(hx[i:i + 2], 16) for i in (0, 2, 4))


def plot_examples(cms):
    """
    helper function to plot two colormaps
    """
    np.random.seed(19680801)
    data = np.random.randn(30, 30)

    fig, axs = plt.subplots(1, 2, figsize=(6, 3), constrained_layout=True)
    for [ax, cmap] in zip(axs, cms):
        psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
        fig.colorbar(psm, ax=ax)
    plt.show()


def get_cmap(colors):
    cs = np.array([hex_to_rgb(g) for g in colors])
    return LinearSegmentedColormap.from_list("mycmap", cs / 255.)


if __name__ == "__main__":
    rs = np.array([hex_to_rgb(r) for r in ncolors.reds])

    # cmap2 = LinearSegmentedColormap.from_list("mycmap", list(zip(ncolors.creamy_values, cs/255.)))
    cmap1 = get_cmap(ncolors.creamy)
    cmap2 = get_cmap(ncolors.greens)
    
    plot_examples([cmap1, cmap2])

    # channel_colors = 'rgb'
    # for i, c in enumerate(cs.T):
    #     plt.plot(c, c=channel_colors[i], marker='o')
    # plt.show()
    pass
