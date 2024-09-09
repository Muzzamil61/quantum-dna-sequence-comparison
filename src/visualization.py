import matplotlib.pyplot as plt
from qiskit.visualization import circuit_drawer

def plot_similarity_scores(similarity_scores):
    organisms = list(similarity_scores.keys())
    scores = list(similarity_scores.values())
    plt.bar(organisms, scores, color='lightblue')
    plt.xlabel('Organisms')
    plt.ylabel('Similarity Scores (%)')
    plt.title('Similarity Scores between Organisms and Reference DNA')

def draw_circuit(circuit, title):
    print(f"{title} Quantum Circuit:")
    display(circuit_drawer(circuit, output='mpl', fold=-1))
