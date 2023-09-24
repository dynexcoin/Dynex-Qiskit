from dynexsdk.qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute
 
t1 = QuantumRegister(1)
t2 = QuantumRegister(1)
t1c = ClassicalRegister(1)
t2c = ClassicalRegister(1)

circuit = QuantumCircuit(t1,t2,t1c,t2c)

circuit.swap(t1[0],t2[0])
circuit.swap(t1[0],t2[0])

circuit.measure(t1, t1c)
circuit.measure(t2, t2c)

execute(circuit)
