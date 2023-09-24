# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""
Quantum measurement in the computational basis.
"""
from ._instruction import Instruction
from ._instructionset import InstructionSet
from ._quantumcircuit import QuantumCircuit
from ._quantumregister import QuantumRegister
from ._classicalregister import ClassicalRegister


class Measure(Instruction):
    """Quantum measurement in the computational basis."""

    def __init__(self, qubit, bit, circuit=None):
        """Create new measurement instruction."""
        super().__init__("measure", [], [qubit], [bit], circuit)

    def qasm(self):
        """Return OPENQASM string."""
        qubit = self.qargs[0]
        bit = self.cargs[0]
        return self._qasmif("measure %s[%d] -> %s[%d];" % (qubit[0].name,
                                                           qubit[1],
                                                           bit[0].name,
                                                           bit[1]))

    def reapply(self, circuit):
        """Reapply this gate to corresponding qubits."""
        self._modifiers(circuit.measure(self.qargs[0], self.cargs[0]))


def measure(self, qubit, cbit):
    """Measure quantum bit into classical bit (tuples).

    Returns:
        qiskit.Instruction: the attached measure instruction.

    Raises:
        QISKitError: if qubit is not in this circuit or bad format;
            if cbit is not in this circuit or not creg.
    """
    if isinstance(qubit, QuantumRegister) and \
       isinstance(cbit, ClassicalRegister) and len(qubit) == len(cbit):
        for i in range(qubit.size):
            self.measure((qubit, i), (cbit, i))
        return None

    
    tgtname = qubit[0].name + '_' + str(qubit[1])
    self.annealergraph.qubits[tgtname]['measured'] = True
    
    '''
    ############################## Dwave 'Measure' ##################################
    import os
    import sys
    import __main__ as main

    tgtname = qubit[0].name + '_' + str(qubit[1])
    filename = main.__file__.split(".")[0] + "_dwave.py"

    with open(filename, "a") as f:
        f.write("print(\"Measurement of {0} => {{0}}\".format({0}))\n".format(tgtname))
    ###############################################################################

    return self._attach(Measure(qubit, cbit, self))
    '''

QuantumCircuit.measure = measure
