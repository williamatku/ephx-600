
"""
    PennyLane Circuits module

    author: William Morris [morriswa/williamatku]

    sources: https://pennylane.ai/qml/demos/tutorial_qft
"""

from numpy import pi
import pennylane as qml


def prepare_state_freq(freq, control_wire, wires):
    """ adapted from https://pennylane.ai/qml/demos/tutorial_qft """

    qml.PauliX(wires=control_wire)
    for wire in wires:
        qml.Hadamard(wires=wire)
    qml.ControlledSequence(qml.PhaseShift(2 * pi * freq, wires=control_wire), control=wires)
    qml.PauliX(wires=control_wire)


dev = qml.device("default.qubit")
@qml.qnode(dev)
def circuit_state(freq, control_wire, wires):
    """ adapted from https://pennylane.ai/qml/demos/tutorial_qft """

    for f in freq:
        prepare_state_freq(freq=f, control_wire=control_wire, wires=wires)

    return qml.state()

@qml.qnode(dev)
def circuit_qft_probs(freq, control_wire, wires):
    """ adapted from https://pennylane.ai/qml/demos/tutorial_qft """

    for f in freq:
        prepare_state_freq(freq=f, control_wire=control_wire, wires=wires)
    qml.QFT(wires=wires)
    return qml.probs(wires=wires)
