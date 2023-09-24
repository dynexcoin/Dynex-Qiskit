from dynexsdk.qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute

n = 4
a = QuantumRegister(n)
b = QuantumRegister(n)

C = QuantumRegister(n)
S = QuantumRegister(n)

ac = ClassicalRegister(n)
bc = ClassicalRegister(n)
Cc = ClassicalRegister(n)
Sc = ClassicalRegister(n)

circuit = QuantumCircuit(a, b, C, S, ac, bc, Cc, Sc)

circuit.ccx(a[n-1], b[n-1], C[n-1])
circuit.cx(a[n-1], S[n-1])
circuit.cx(b[n-1], S[n-1])

for i in range(1,n):
    circuit.ccx(a[n-1-i],b[n-1-i],C[n-1-i])
    circuit.ccx(b[n-1-i],C[n-1-(i-1)],C[n-1-i])
    circuit.ccx(a[n-1-i],C[n-1-(i-1)],C[n-1-i])
    circuit.cx(a[n-1-i], S[n-1-i])
    circuit.cx(b[n-1-i], S[n-1-i])
    circuit.cx(C[n-1-(i-1)], S[n-1-i])
    
circuit.measure(C, Cc)
circuit.measure(S, Sc)

execute(circuit)
