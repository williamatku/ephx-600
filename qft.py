
"""
    QFT module

    author: William Morris [morriswa/williamatku]

    sources: https://pennylane.ai/qml/demos/tutorial_qft
"""


import matplotlib.pyplot as plt

import circuits




class QFT:
    def __init__(self, n_qubits, freq_res):
        self.n_qubits = n_qubits
        self.control_q = 0
        self.enc_q = range(1, self.n_qubits + 1)
        self.freq_res = freq_res
        self.freq_bins = [s / 10 ** self.freq_res for s in range(1, 10 ** self.freq_res)]
        self.q_states = 2**self.n_qubits
        self.enc_freq = None

    def set_encoded_frequencies(self, freq):
        self.enc_freq = freq


    @staticmethod
    def show_amplitude_graph(state):
        plt.bar(range(len(state)), state)
        plt.xlabel("|x⟩")
        plt.ylabel("Amplitude (real part)")
        plt.show()

    @staticmethod
    def show_probability_dist(state):
        plt.bar(range(len(state)), state)
        plt.xlabel("|x⟩")
        plt.ylabel("probs")
        plt.show()


    def prep_state(self, show_amplitude_graph=False):
        """
            currently set up to display visualization of quantum state use amplitudes
            adapted from https://pennylane.ai/qml/demos/tutorial_qft """
        if self.enc_freq is None:
            raise Exception('please call set_encoded_frequencies first')

        state = circuits.encode_frequencies(self.enc_freq, self.control_q, self.enc_q)[:self.q_states]
        if show_amplitude_graph:
            self.show_amplitude_graph(state)


    def prep_state_apply_qft(self, show_probability_dist=False):
        """
        then output probability distribution of all quantum states after applying qft
        adapted from https://pennylane.ai/qml/demos/tutorial_qft """

        state = circuits.encode_frequencies_apply_qft(self.enc_freq, self.control_q, self.enc_q)[:self.q_states]

        top_indices = sorted(range(len(state)), key=lambda i: state[i], reverse=True)[:len(self.enc_freq)]
        top_values = [(index, state[index]) for index in top_indices]

        reported = []
        for i, s in top_values:
            freq = 1 - i / (2 ** self.n_qubits)
            for f in self.freq_bins:
                if round(freq, self.freq_res) == f:
                    reported.append((f, s))
                    break

        found = []
        confs = []
        others = []
        for reported_freq, confidence_score in reported:

            cat = False
            for desired_freq in self.enc_freq:
                if reported_freq == desired_freq:
                    found.append(reported_freq)
                    confs.append(confidence_score)
                    cat = True

            if not cat:
                others.append(reported_freq)

        found = set(found)
        score = len(found) / len(self.enc_freq)
        if len(confs) == 0:
            confidence_score = 0
        else:
            confidence_score = sum(confs) / len(confs)

        if show_probability_dist:
            self.show_probability_dist(state)

        return score, confidence_score
