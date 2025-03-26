
from numpy import pi
import pennylane as qml




def prep(freq, control_wire, wires):
    qml.PauliX(wires=control_wire)
    for wire in wires:
        qml.Hadamard(wires=wire)
    qml.ControlledSequence(qml.PhaseShift(-2 * pi * freq, wires=control_wire), control=wires)
    qml.PauliX(wires=control_wire)


def prep2(freq, freq2, control_wire, wires):
    qml.PauliX(wires=control_wire)
    for wire in wires:
        qml.Hadamard(wires=wire)
    qml.ControlledSequence(qml.PhaseShift(-2 * pi * freq * freq2, wires=control_wire), control=wires)
    qml.PauliX(wires=control_wire)


dev = qml.device("default.qubit")
@qml.qnode(dev)
def circuit_state(control_wire, wires):
    prep2(freq=1/7, freq2=-1/2, control_wire=control_wire, wires=wires)
    return qml.state()

@qml.qnode(dev)
def circuit_qft_probs(control_wire, wires):
    prep2(freq=1/7, freq2=-1/2, control_wire=control_wire, wires=wires)
    qml.QFT(wires=wires)
    return qml.probs(wires=wires)
