from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler
from dna_encoding import encode_dna_sequence
from dna_circuits import create_dna_circuit, calculate_similarity
from similarity_comparison import run_sampler, extract_bitarray, bitarray_to_counts, calculate_similarity_scores
from visualization import plot_similarity_scores, draw_circuit
import matplotlib.pyplot as plt

# Connect to IBM Quantum
QiskitRuntimeService.save_account(channel="ibm_quantum", token="token_here", overwrite=True)
service = QiskitRuntimeService()
backend_name = 'ibm_sherbrooke'
backend_real = service.get_backend(backend_name)

print(f"Selected backend: {backend_real.name}")

# DNA sequences
YEAST = "ATCG" * 32
PROTOZOAN = "ATGC" * 32
BACTERIAL = "TGCA" * 32
REFERENCE = "GCTA" * 32

# Encode the sequences
encoded_yeast = encode_dna_sequence(YEAST)
encoded_protozoan = encode_dna_sequence(PROTOZOAN)
encoded_bacterial = encode_dna_sequence(BACTERIAL)
encoded_reference = encode_dna_sequence(REFERENCE)

# Determine the number of qubits
num_qubits = len(encoded_yeast)

# Create the DNA quantum circuits
qc_yeast, qr_yeast, cr_yeast = create_dna_circuit(encoded_yeast, num_qubits)
qc_protozoan, qr_protozoan, cr_protozoan = create_dna_circuit(encoded_protozoan, num_qubits)
qc_bacterial, qr_bacterial, cr_bacterial = create_dna_circuit(encoded_bacterial, num_qubits)
qc_reference, qr_reference, cr_reference = create_dna_circuit(encoded_reference, num_qubits)

# Compare sequences with the reference
qc_similarity_yeast = calculate_similarity(qc_yeast, qc_reference, qr_yeast, cr_yeast)
qc_similarity_protozoan = calculate_similarity(qc_protozoan, qc_reference, qr_protozoan, cr_protozoan)
qc_similarity_bacterial = calculate_similarity(qc_bacterial, qc_reference, qr_bacterial, cr_bacterial)

# Execute the quantum circuits
result_yeast, result_protozoan, result_bacterial = run_sampler(backend_real, [qc_similarity_yeast, qc_similarity_protozoan, qc_similarity_bacterial])

# Extract results and calculate similarity scores
bitarray_yeast = extract_bitarray(result_yeast)
bitarray_protozoan = extract_bitarray(result_protozoan)
bitarray_bacterial = extract_bitarray(result_bacterial)
counts_yeast = bitarray_to_counts(bitarray_yeast)
counts_protozoan = bitarray_to_counts(bitarray_protozoan)
counts_bacterial = bitarray_to_counts(bitarray_bacterial)
similarity_scores = calculate_similarity_scores([counts_yeast, counts_protozoan, counts_bacterial])

# Display the results
for organism, score in similarity_scores.items():
    print(f"Similarity score between {organism} and REFERENCE: {score:.2f}%")

most_similar = max(similarity_scores, key=similarity_scores.get)
print(f"[ANSWER] The sequence most similar to the REFERENCE is {most_similar}")

# Plot the results
plot_similarity_scores(similarity_scores)
plt.show()

# Visualize the circuits
draw_circuit(qc_yeast, "YEAST DNA Sequence")
draw_circuit(qc_protozoan, "PROTOZOAN DNA Sequence")
draw_circuit(qc_bacterial, "BACTERIAL DNA Sequence")
draw_circuit(qc_reference, "REFERENCE DNA Sequence")
draw_circuit(qc_similarity_yeast, "YEAST vs REFERENCE Comparison")
draw_circuit(qc_similarity_protozoan, "PROTOZOAN vs REFERENCE Comparison")
draw_circuit(qc_similarity_bacterial, "BACTERIAL vs REFERENCE Comparison")
