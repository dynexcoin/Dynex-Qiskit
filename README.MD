# Dynex Qiskit (alpha) Package

Recent advances in quantum hardware have resulted in the first systems becoming publicly available. On one hand, gate-based quantum computers have been designed, such as the IBM Q, Rigetti’s Aspen, or IonQ’s systems using using superconducting transmons or ion tubes. On the other hand, adibiatic quantum computing and neuromorphic computing has emerged as another possibility to leverage physics inspired computations. It was shown that adiabatic quantum computing can solve the same problems as gate-based (universal) quantum computing given at least two degrees
of freedom for 2-local Hamiltonian [3,4,5]. The Dynex Neuromorphic platform supports a 2-local Ising
Hamiltonian with a single degree of freedom, which is why it is believed to only solve a subset of the problems that can be expressed by gate-based (universal) quantum machines. In 2014, Warren outlined how a set of universal quantum gates could be realized in adiabatic form using D-Wave’s annealing abstraction [1]. This is demonstrated, among others, for C-NOT, Toffoli (CC-NOT), Swap and C-Swap (Fredkin) gates in a {0, 1} base of qubit states, and for the Hadamard gate in a two-vector {|0i, |1i} base. 

The Dynex Qiskit Package allows to execute IBM Qiskit programs and circuits on the Dynex Neuromorphic platform. Thanks to groundbreaking research from [Richard H. Warren](https://arxiv.org/pdf/1405.2354.pdf), it is possible to directly translate Qiskit quantum circuits into Dynex Neuromorphic chips. The concept behind is a direct translation of Qiskit objects, but instead of running on IBM Q, the circuits are executed on the Dynex platform.

# Guides

- [Medium: Computing on the Dynex Neuromorphic Platform: IBM Qiskit 4-Qubit Full Adder Circuit](https://github.com/dynexcoin/Dynex-Qiskit/blob/main/Medium_IBM_Qiskit.ipynb)

# Requirements

The following packages are requried to use the Dynex Qiskit Package:

```
pip install dynex   # Dynex SDK
pip install qiskit  # Qiskit
```

Please make sure your configure your Dynex SDK accordingly before.

# Example

The only change required to Qiskit code are the imports (replacing 'qiskit' with 'dynexsdk.qiskit'. Here is an example of a 1 qubit adder:

```
from dynexsdk.qiskit import QuantumRegister, ClassicalRegister
from dynexsdk.qiskit import QuantumCircuit, execute

# Input Registers: a = qi[0]; b = qi[1]; ci = qi[2]
qi = QuantumRegister(3)
ci = ClassicalRegister(3)

# Output Registers: s = qo[0]; co = qo[1]
qo = QuantumRegister(2)
co = ClassicalRegister(2)
circuit = QuantumCircuit(qi,qo,ci,co)

# Define adder circuit
for idx in range(3):
    circuit.ccx(qi[idx], qi[(idx+1)%3], qo[1])
for idx in range(3):
    circuit.cx(qi[idx], qo[0])

circuit.measure(qo, co)

# Run
execute(circuit)
```

Which outputs:

```
=====================================
Qiskit on Dynex Neuromorphic Platform
=====================================


[DYNEX] Embedding has been built:
	number of qubits:  79
	number of couplers:  110
	number of non-gate couplers: 47

Constrain input of measured qubit q1_0 to be 0 (y/n)? y
Constrain input of measured qubit q1_1 to be 0 (y/n)? y
Constrain input of unmeasured qubit q0_0 to be 0 (y/n)? n
Constrain input of unmeasured qubit q0_1 to be 0 (y/n)? n
Constrain input of unmeasured qubit q0_2 to be 0 (y/n)? n

How many samples (=num_reads)? 10000

How many ODE integration steps (=annealing_time)? 300

Qubit biases:
 {397: 5, 393: 10, 398: 5, 394: 10, 396: 9, 399: 8, 392: 13, 395: 9, 264: 10, 136: 9, 266: 10, 138: 10, 142: 10, 137: 5, 141: 10, 139: 8, 140: 13, 143: 9, 148: 10, 156: 9, 149: 10, 157: 10, 521: 10, 525: 10, 533: 10, 529: 10, 401: 10, 273: 10, 145: 10, 151: 10, 159: 10, 153: 10, 155: 10, 158: 8, 152: 8, 154: 9, 283: 10, 411: 11, 415: 6, 409: 6, 413: 6, 408: 9, 412: 9, 421: 10, 429: 6, 134: 10, 130: 10, 2: 10, 6: 10, 14: 10, 22: 10, 30: 10, 38: 10, 34: 10, 162: 10, 290: 10, 418: 10, 422: 10, 430: 11, 426: 6, 425: 6, 428: 9, 424: 9, 297: 10, 169: 6, 25: 10, 29: 10, 37: 10, 33: 10, 161: 10, 289: 10, 293: 10, 301: 10, 299: 10, 171: 11, 175: 6, 173: 1, 168: 9, 172: 9}

Coupler strength:
 {(393, 397): -10, (394, 398): -10, (392, 399): -13, (395, 396): -9, (395, 397): -4, (395, 398): -5, (395, 399): 9, (392, 396): -7, (393, 399): -2, (394, 399): -2, (393, 396): 2, (394, 396): 2, (394, 397): 1, (264, 392): -10, (136, 264): -10, (266, 394): -10, (138, 266): -10, (138, 142): -10, (137, 141): -10, (139, 140): -13, (136, 143): -9, (138, 143): -4, (137, 143): -5, (139, 143): 9, (136, 140): -7, (139, 142): -2, (139, 141): -2, (136, 142): 2, (136, 141): 2, (138, 141): 1, (140, 148): -10, (148, 156): -10, (141, 149): -10, (149, 157): -10, (393, 521): -10, (521, 525): -10, (525, 533): -10, (529, 533): -10, (401, 529): -10, (273, 401): -10, (145, 273): -10, (145, 151): -10, (151, 159): -10, (153, 157): -10, (155, 159): -10, (152, 158): -13, (154, 156): -9, (154, 157): -4, (154, 159): -5, (154, 158): 9, (152, 156): -7, (153, 158): -2, (155, 158): -2, (153, 156): 2, (155, 156): 2, (155, 157): 1, (155, 283): -10, (283, 411): -10, (408, 412): -14, (408, 415): -4, (409, 412): -4, (408, 413): 4, (411, 415): -11, (411, 413): -2, (409, 415): 2, (409, 413): -2, (413, 421): -10, (421, 429): -10, (134, 142): -10, (130, 134): -10, (2, 130): -10, (2, 6): -10, (6, 14): -10, (14, 22): -10, (22, 30): -10, (30, 38): -10, (34, 38): -10, (34, 162): -10, (162, 290): -10, (290, 418): -10, (418, 422): -10, (422, 430): -10, (424, 428): -14, (426, 428): -4, (424, 429): -4, (425, 428): 4, (426, 430): -11, (425, 430): -2, (426, 429): 2, (425, 429): -2, (297, 425): -10, (169, 297): -10, (25, 153): -10, (25, 29): -10, (29, 37): -10, (33, 37): -10, (33, 161): -10, (161, 289): -10, (289, 293): -10, (293, 301): -10, (299, 301): -10, (171, 299): -10, (168, 172): -14, (168, 175): -4, (169, 172): -4, (168, 173): 4, (171, 175): -11, (171, 173): -2, (169, 175): 2, (169, 173): -2}

#bqm variables:
 79

Running Qiskit Circuit on the Dynex Neuromorphic Platform...
[DYNEX] MODEL CONVERTED TO QUBO
[DYNEX] PRECISION SET TO 0.001
[DYNEX] QUBO: Constant offset of the binary quadratic model: 0.0
[DYNEX] SAMPLER INITIALISED
[DYNEX] MALLOB: JOB CREATED:  5118
[ÐYNEX] SUBMITTING JOB - UPLOADING JOB FILE...
file upload progress:   0%|          | 0.00/9.09k [00:00<?, ?B/s]
[DYNEX] File 'tmp/c7e431f347ea4ccb3e139ad74c575e6c.bin' sent successfully to 'ftp.dynexcoin.org/'
[ÐYNEX] SUBMITTING START COMMAND...
[DYNEX] MALLOB: JOB UPDATED: 5118 STATUS: 0
[ÐYNEX] STARTING JOB...
╭────────────┬───────────┬───────────┬─────────┬──────┬─────────┬───────┬─────┬──────────┬───────────╮
│   DYNEXJOB │   ELAPSED │   WORKERS │   CHIPS │    ✔ │   STEPS │   LOC │   ✔ │   ENERGY │         ✔ │
├────────────┼───────────┼───────────┼─────────┼──────┼─────────┼───────┼─────┼──────────┼───────────┤
│       5118 │      0.21 │         1 │  139776 │ 9984 │   10000 │    11 │  11 │   767000 │ 767000.00 │
╰────────────┴───────────┴───────────┴─────────┴──────┴─────────┴───────┴─────┴──────────┴───────────╯
╭───────────┬───────────────┬─────────┬───────┬───────────┬───────────┬───────────────┬──────────╮
│    WORKER │       VERSION │   CHIPS │   LOC │    ENERGY │   RUNTIME │   LAST UPDATE │   STATUS │
├───────────┼───────────────┼─────────┼───────┼───────────┼───────────┼───────────────┼──────────┤
│ 134767307 │ 2.3.0.OZM.124 │    9984 │    12 │ 767000.00 │  0.05 min │    10.00s ago │  STOPPED │
├───────────┼───────────────┼─────────┼───────┼───────────┼───────────┼───────────────┼──────────┤
│ 134767310 │ 2.3.0.OZM.124 │    9984 │    11 │ 767000.00 │  0.07 min │     9.00s ago │  STOPPED │
├───────────┼───────────────┼─────────┼───────┼───────────┼───────────┼───────────────┼──────────┤
│ 134767315 │ 2.3.0.OZM.124 │    9984 │    11 │ 767000.00 │  0.05 min │     9.00s ago │  STOPPED │
├───────────┼───────────────┼─────────┼───────┼───────────┼───────────┼───────────────┼──────────┤
│ 134767325 │ 2.3.0.OZM.124 │    9984 │    11 │ 767000.00 │  0.07 min │     7.00s ago │  STOPPED │
├───────────┼───────────────┼─────────┼───────┼───────────┼───────────┼───────────────┼──────────┤
│ 134767335 │ 2.3.0.OZM.124 │    9984 │    12 │ 767000.00 │  0.07 min │     6.00s ago │  STOPPED │
├───────────┼───────────────┼─────────┼───────┼───────────┼───────────┼───────────────┼──────────┤
│ 134767337 │ 2.3.0.OZM.124 │    9984 │    12 │ 767000.00 │  0.08 min │     4.00s ago │  STOPPED │
├───────────┼───────────────┼─────────┼───────┼───────────┼───────────┼───────────────┼──────────┤
│ 134767339 │ 2.3.0.OZM.124 │    9984 │    13 │ 767000.00 │  0.05 min │     6.00s ago │  STOPPED │
├───────────┼───────────────┼─────────┼───────┼───────────┼───────────┼───────────────┼──────────┤
│ 134767341 │ 2.3.0.OZM.124 │    9984 │    12 │ 767000.00 │  0.07 min │     5.00s ago │  STOPPED │
├───────────┼───────────────┼─────────┼───────┼───────────┼───────────┼───────────────┼──────────┤
│ 134767344 │ 2.3.0.OZM.124 │    9984 │    12 │ 767000.00 │  0.10 min │     2.00s ago │  STOPPED │
├───────────┼───────────────┼─────────┼───────┼───────────┼───────────┼───────────────┼──────────┤
│ 134767352 │ 2.3.0.OZM.124 │    9984 │    14 │ 767000.00 │  0.07 min │     4.00s ago │  STOPPED │
├───────────┼───────────────┼─────────┼───────┼───────────┼───────────┼───────────────┼──────────┤
│ 134767366 │ 2.3.0.OZM.124 │    9984 │    12 │ 767000.00 │  0.05 min │     3.00s ago │  STOPPED │
├───────────┼───────────────┼─────────┼───────┼───────────┼───────────┼───────────────┼──────────┤
│ 134767364 │ 2.3.0.OZM.121 │    9984 │    92 │ 767000.00 │  0.05 min │     3.00s ago │  STOPPED │
├───────────┼───────────────┼─────────┼───────┼───────────┼───────────┼───────────────┼──────────┤
│ 134767374 │ 2.3.0.OZM.124 │    9984 │    13 │ 767000.00 │  0.08 min │     0.00s ago │  STOPPED │
├───────────┼───────────────┼─────────┼───────┼───────────┼───────────┼───────────────┼──────────┤
│ 134767376 │ 2.3.0.OZM.121 │    9984 │    92 │ 767000.00 │  0.05 min │     2.00s ago │  STOPPED │
╰───────────┴───────────────┴─────────┴───────┴───────────┴───────────┴───────────────┴──────────╯
[DYNEX] FINISHED READ AFTER 0.21 SECONDS
[DYNEX] COMPUTING FILE c7e431f347ea4ccb3e139ad74c575e6c.bin REMOVED
[DYNEX] SAMPLESET LOADED
Done.
   2  6 14 22 25 29 30 33 34 37 38 130 134 136 137 138 ... 533 energy num_oc.
0  0  0  0  0  0  0  0  0  0  0  0   0   0   0   0   0 ...   0    0.0       1
['BINARY', 1 rows, 1 samples, 79 variables]
Ground State:  0.0


qubits:
['q1_0', 'q1_1', 'q0_0', 'q0_1', 'q0_2']
reads:
[0, 0, 0, 0, 0]

```

# Technical Background

The Dynex Qiskit Package automatically translates quantum programs (Qiskit based) from a subset of common gates to an adibiatic representation, which is used by adibiatic quantum computers and by the Dynex Neuromorphic platform. Adiabatic computing with two degrees of freedom of 2-local Hamiltonians has been theoretically shown to be equivalent to the gate model of universal quantum computing. The Dynex Qiskit Package translates quantum gate circuits comprised of a subset of common gates expressed as an IBM Qiskit program to single-degree 2-local Ising Hamiltonians, which are subsequently embedded on the Dynex Neuromomorphic platform. These gate elements are placed in the chimera graph and augmented by constraints that enforce inter-gate logical relationships, resulting in an annealer embedding that completely characterizes the overall gate circuit.

Given a circuits (in Qiskit format):

1. Construct equivalent QUBO (quadratic unconstrained binary opt.)
	- Each gate -> QUBO
	- Compose QUBOs into single Hamiltonian
2. Find embedding
	- In 16x16 bi-partite graphs (K4,4) sparsely connected as Chimera
	- Project per-gate QUBO -> bi-partite unit graph K4,4
	- Connect constraints b/w QUBOs of units graphs -> “wires”
3. In Python: Transform IBM Qiskit program
	- Replace gates
	- Run, but instead of IBM Q exec., sample on the Dynex Neuromorphic sampler

Given 'n' gates and 'q' qubits (IBM), the resulting QUBO/Ising problem translates to ~ 23n qubits (Dynex), but often just to 5-6n due to complex (Toffoli) gates. 

An upper bound on the resource requirements on both ends can be given as follows: Given an n-gate quantum circuit (in our case specified as a Qiskit program), a translation to an adiabatic form is provided in no more than 32n adiabatic qubits on its QUBO/Ising representation. The factor is comprised of 8 qubits for the K4,4 representation of a gate, the remaining 24 qubits are used as wiring to the left and below that gate-equivalent K4,4 graph. Notice that an increase by 32X still increases the capabilities by
mapping to the Dynex platform dramatically, and problems can often be mapped more efficiently.

Notice that currently we do not provide a translation for the Hadamard gate, H, as it requires a different base of qubit states than the others.

# References and Scientific Background

[1] Warren, Richard. (2014). [Gates for Adiabatic Quantum Computing](https://www.researchgate.net/publication/262264335_Gates_for_Adiabatic_Quantum_Computing). 

[2] Regan, Malcolm & Eastwood, Brody & Nagabhiru, Mahita & Mueller, Frank. (2019). [Automatically Translating Quantum Programs from a Subset of Common Gates to an Adiabatic Representation](https://www.researchgate.net/publication/333814539_Automatically_Translating_Quantum_Programs_from_a_Subset_of_Common_Gates_to_an_Adiabatic_Representation). 10.1007/978-3-030-21500-2_9. 

[3] Aharonov, D., van Dam, W., Kempe, J., Landau, Z., Lloyd, S.,
Regev, O.: Adiabatic quantum computation is equivalent to standard quantum computation. SIAM J. Comput. 37(1), 166–194 (Apr 2007). https://doi.org/10.1137/S0097539705447323, http://dx.doi.org/10.1137/S0097539705447323

[4] Bacon, D., Flammia, S.T., Crosswhite, G.M.: Adiabatic quantum transistors (2012). https://doi.org/10.1103/PhysRevX.3.021015

[5] Dorit Aharonov, Wim van Dam, J.K.Z.L.S.L.O.R.: Adiabatic quantum computation is equivalent to standard quantum computation. ArXiv e-prints (May 2004), https://arxiv.org/abs/quant-ph/0405098
