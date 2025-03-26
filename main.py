#!/usr/bin/env python
from qft import show_amplitude_graph, show_probability_dist


def main():
    # currently set up to display visualization of quantum state use amplitudes
    show_amplitude_graph()
    # then output probability distribution of all quantum states after applying qft
    show_probability_dist()


if __name__ == "__main__":
    main()
