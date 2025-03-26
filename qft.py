
"""
    QFT module

    author: William Morris [morriswa/williamatku]

    sources: https://pennylane.ai/qml/demos/tutorial_qft
"""


import matplotlib.pyplot as plt
import numpy as np

from circuits import circuit_state, circuit_qft_probs


QUBITS = 8
CONTROL_QUBIT = 0
ENC_QUBITS = range(1, QUBITS+1)
# only supports frequencies < 1
FREQUENCIES = [1/49, 1/25]
Q_STATES = 2**QUBITS


def show_amplitude_graph():
    """ adapted from https://pennylane.ai/qml/demos/tutorial_qft """
    state = circuit_state(FREQUENCIES, CONTROL_QUBIT, ENC_QUBITS)[:Q_STATES]

    plt.bar(range(len(state)), state)
    plt.xlabel("|x⟩")
    plt.ylabel("Amplitude (real part)")
    plt.show()


def show_probability_dist():
    """ adapted from https://pennylane.ai/qml/demos/tutorial_qft """

    state = circuit_qft_probs(FREQUENCIES, CONTROL_QUBIT, ENC_QUBITS)[:Q_STATES]

    top_indices = sorted(range(len(state)), key=lambda i: state[i], reverse=True)[:len(FREQUENCIES)]
    top_values = [(index, state[index]) for index in top_indices]

    for i, s in top_values:
        print(f'{int(s*100)}% certain freq {1 - i/(2**QUBITS)} is present...')

    plt.bar(range(len(state)), state)
    plt.xlabel("|x⟩")
    plt.ylabel("probs")
    plt.show()

