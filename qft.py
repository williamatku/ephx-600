#!/usr/bin/env python

"""
    QFT module

    author: William Morris [morriswa/williamatku]
"""


import matplotlib.pyplot as plt

from circuits import circuit_state, circuit_qft_probs


QUBITS = 5
CONTROL_QUBIT = 0
ENC_QUBITS = range(1, QUBITS+1)


def show_amplitude_graph():
    state = circuit_state(
                          control_wire=CONTROL_QUBIT,
                          wires=ENC_QUBITS
            )[:2**QUBITS]

    plt.bar(range(len(state)), state)
    plt.xlabel("|x⟩")
    plt.ylabel("Amplitude (real part)")
    plt.show()


def show_probability_dist():
    state = circuit_qft_probs(
                              control_wire=CONTROL_QUBIT,
                              wires=ENC_QUBITS
            )[:2**QUBITS]



    plt.bar(range(len(state)), state)
    plt.xlabel("|x⟩")
    plt.ylabel("probs")
    plt.show()


def main():
    show_amplitude_graph()
    show_probability_dist()


if __name__ == "__main__":
    main()
