from qiskit_ibm_runtime import Session, Sampler

def run_sampler(backend_real, circuits):
    with Session(backend=backend_real) as session:
        sampler = Sampler(session=session)
        jobs = [sampler.run([qc]) for qc in circuits]
        results = [job.result() for job in jobs]
    return results

def extract_bitarray(result):
    data = result._pub_results[0].data
    for key in data.keys():
        if key.startswith('c'):
            return data[key]
    return None

def bitarray_to_counts(bitarray):
    return bitarray.get_counts()

def calculate_similarity_scores(counts_list):
    scores = {}
    organisms = ["YEAST", "PROTOZOAN", "BACTERIAL"]
    for counts, organism in zip(counts_list, organisms):
        scores[organism] = max(counts.values()) * 100
    return scores
