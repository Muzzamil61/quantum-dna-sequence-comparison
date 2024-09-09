def encode_dna_sequence(dna_sequence, max_qubits=127):
    mapping = {'A': '00', 'T': '01', 'C': '10', 'G': '11'}
    binary_sequence = ''.join([mapping[char] for char in dna_sequence])
    return binary_sequence[:max_qubits]  # Ensure the sequence is within the qubit limit
