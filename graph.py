# graph.py
# This module takes data and outputs it to a graph


import matplotlib.pyplot as plt
import numpy as np


def dict_to_graph(d: dict, data_type: str, name: str) -> None:
    """ Takes a dictionary and graphs the contents """
    sorted_d = sorted(d.items(), key=lambda x: x[0])

    left = np.arange(len(sorted_d))
    tick_label = [k for k,v in sorted_d]
    height = [v for k,v in sorted_d]

    plt.bar(left, height, tick_label=tick_label, width=.1)

    plt.xlabel(f'{data_type}')
    plt.ylabel("Amount")
    plt.title(f'{data_type} Data Graph')

    plt.show()
    plt.savefig(f"C:\\message_data\\{name}\\{name}_{data_type}_graph.png")
