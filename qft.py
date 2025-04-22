
"""
    QFT module

    author: William Morris [morriswa/williamatku]

    sources: https://pennylane.ai/qml/demos/tutorial_qft
"""


import matplotlib.pyplot as plt

from circuits import circuit_state, circuit_qft_probs


QUBITS = 6
CONTROL_QUBIT = 0
ENC_QUBITS = range(1, QUBITS+1)
# only supports frequencies < 1
FREQUENCY_RES = 2
FREQUENCY_BINS = [s / 10 ** FREQUENCY_RES for s in range(1, 10 ** FREQUENCY_RES)]
print(len(FREQUENCY_BINS))
# must be in frequency bin...
FREQUENCIES = [31/100, 32/100, 71/100, 64/100]
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

    top_indices = sorted(range(len(state)), key=lambda i: state[i], reverse=True)
    top_values = [(index, state[index]) for index in top_indices]

    reported = []
    for i, s in top_values:
        freq = 1 - i/(2**QUBITS)
        for f in FREQUENCY_BINS:
            if round(freq, FREQUENCY_RES) == f:
                reported.append(f)
                break

    found = []
    others = []
    for reported_freq in reported:

        cat = False
        for desired_freq in FREQUENCIES:
            if reported_freq == desired_freq:
                found.append(reported_freq)
                cat = True

        if not cat:
            others.append(reported_freq)

    found = set(found)
    print(f"score: {len(found)/len(FREQUENCIES)}")
    print(f"identified {len(found)} of {len(FREQUENCIES)} frequencies")

    plt.bar(range(len(state)), state)
    plt.xlabel("|x⟩")
    plt.ylabel("probs")
    plt.show()
