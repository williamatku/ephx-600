#!/usr/bin/env python
import random
import warnings
import csv

from numpy.exceptions import ComplexWarning

from qft import QFT

TRIALS = 20
FREQUENCY_RESOLUTION = 2
MIN_QUBITS = 2
MAX_QUBITS = 16
TEST_FREQS = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

def main():
    warnings.simplefilter("ignore", category=ComplexWarning)

    scoresheet = []
    for trial_no in range(TRIALS):
        for n_qubits in range(2, MAX_QUBITS+1):
            for enc_freqs in TEST_FREQS:
                qft = QFT(n_qubits, FREQUENCY_RESOLUTION)
                freqs = []
                for i in range(enc_freqs):
                    freqs.append(random.randint(1, 10**FREQUENCY_RESOLUTION)/(10**FREQUENCY_RESOLUTION))
                qft.set_encoded_frequencies(freqs)
                score, conf = qft.prep_state_apply_qft()
                print(f"trial no: {trial_no+1}, n_qubits: {n_qubits}, enc_freqs: {enc_freqs}, score: {score}, average confidence: {conf}")
                scoresheet.append([trial_no+1, n_qubits, enc_freqs, score, conf])

    with open('out.csv', 'w', newline='') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(["trial no", "n_qubits", "enc_freqs", "score", "avg confidence"])
        for row in scoresheet:
            w.writerow(row)



if __name__ == "__main__":
    main()
