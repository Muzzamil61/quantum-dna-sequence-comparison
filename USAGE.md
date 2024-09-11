# Usage Guide for Quantum DNA Sequence Comparison

This guide provides instructions on how to run the quantum DNA sequence comparison project using Qiskit and IBM Quantum hardware.

## Prerequisites

1. **Python**: Ensure you have Python 3.7+ installed.
2. **Qiskit**: Install the Qiskit library and other required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. **IBM Quantum Account**: You must have an IBM Quantum Experience account to run the code on IBM Quantum hardware. Save your API token using the following command:
    ```python
    from qiskit_ibm_runtime import QiskitRuntimeService
    QiskitRuntimeService.save_account(channel="ibm_quantum", token="your_token_here", overwrite=True)
    ```

## Running the Quantum DNA Sequence Comparison Scripts

Navigate to the `src/` directory and run the specific DNA sequence comparison scripts:

### Yeast vs Reference Comparison

To compare the YEAST DNA sequence with the REFERENCE DNA sequence, run:

```bash
python src/yeast_vs_reference_circuit.py
