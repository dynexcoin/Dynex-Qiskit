from dynexsdk.qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from sys import argv

qin1 = QuantumRegister(1)
cin1 = ClassicalRegister(1)
qin2 = QuantumRegister(1)
cin2 = ClassicalRegister(1)

#output bit: function XORed onto this
qz = QuantumRegister(1)
cz = ClassicalRegister(1)

#output bit: function XORed onto this
tmp = QuantumRegister(1)

#beginning of the circuit
circuit = QuantumCircuit(qin1,qin2,qz,tmp,cin1,cin2,cz)

#initialize temp
circuit.x(tmp)

circuit.cx(tmp, qz)
circuit.ccx(qin1, tmp, qz)
circuit.ccx(qin2, tmp, qz)

#reversing tmp
circuit.x(tmp)

#circuit.measure(qin1, cin1)
#circuit.measure(qin2, cin2)
circuit.measure(qz, cz)

execute(circuit)
