
"""
    PennyLane Circuits module

    author: William Morris [morriswa/williamatku]

    sources: https://pennylane.ai/qml/demos/tutorial_qft
"""

from numpy import pi
import pennylane as qml


dev = qml.device("default.qubit")



def pstate(freqs, control_wire, wires):
    """ adapted from https://pennylane.ai/qml/demos/tutorial_qft """

    qml.PauliX(wires=control_wire)

    embed = None
    for freq in freqs:
        embed = qml.PhaseShift(2 * pi * freq, wires=control_wire)

    for wire in wires:
        qml.Hadamard(wires=wire)
    qml.ControlledSequence(embed, control=wires)

    qml.PauliX(wires=control_wire)


@qml.qnode(dev)
def circuit_state(freqs, control_wire, wires):
    """ adapted from https://pennylane.ai/qml/demos/tutorial_qft """
    pstate(freqs, control_wire, wires)
    return qml.state()


@qml.qnode(dev)
def circuit_qft_probs(freqs, control_wire, wires):
    """ adapted from https://pennylane.ai/qml/demos/tutorial_qft """
    pstate(freqs, control_wire, wires)
    qml.QFT(wires=wires)
    return qml.probs(wires=wires)
