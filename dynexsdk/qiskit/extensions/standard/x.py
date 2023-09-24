# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

# pylint: disable=invalid-name

"""
Pauli X (bit-flip) gate.
"""
from dynexsdk.qiskit import Gate
from dynexsdk.qiskit import InstructionSet
from dynexsdk.qiskit import QuantumCircuit
from dynexsdk.qiskit import QuantumRegister
from dynexsdk.qiskit.extensions.standard import header  # pylint: disable=unused-import


class XGate(Gate):
    """Pauli X (bit-flip) gate."""

    def __init__(self, qubit, circ=None):
        """Create new X gate."""
        super().__init__("x", [], [qubit], circ)

    def inverse(self):
        """Invert this gate."""
        return self  # self-inverse

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.x(self.qargs[0]))




def x(self, q):
    if isinstance(q, QuantumRegister):
        for j in range(q.size):
            self.x((q, j))
        return None

    tgtname = q[0].name + "_" + str(q[1])
    self.annealergraph.add_X(tgtname)
    '''
    ############################## Write Dwave NOT ##################################
    import os
    import sys
    import __main__ as main

    tgtname = q[0].name + "_" + str(q[1])

    filename = main.__file__.split(".")[0] + "_dwave.py"
    with open("./{}".format(filename), "a") as f:
        f.write("#" * 80 + "\n")
        f.write("## NOT - target: {0} ##\n".format(tgtname))
        f.write("#" * 80 + "\n")
        f.write("if \'{0}\' not in globals():\n".format(tgtname))
        f.write("    {0}=0\n\n".format(tgtname))
        f.write("bqm = dimod.BinaryQuadraticModel({{\'{0}\' : -4, \'out{0}\' : -4}}, {{(\'{0}\', \'out{0}\') : 8}}, 4, dimod.BINARY)\n".format(tgtname))
        f.write("sampler = dimod.ExactSolver()\n")
        f.write("response = sampler.sample(bqm)\n\n")
        f.write("for sample, energy in response.data(['sample', 'energy']):\n")
        f.write("    if sample[\'{0}\']=={0} and int(energy)==0:\n".format(tgtname))
        f.write("        {0}_before = sample[\'{0}\']\n".format(tgtname))
        f.write("        {0}=sample[\'out{0}\']\n".format(tgtname))
        f.write("        break\n\n")
        f.write("print('#' * 80)\n")
        f.write("print(\"NOT operation on {0}:\")\n".format(tgtname))
        f.write("print(\"    in:  {0}={{0}}\".format({0}_before))\n".format(tgtname))
        f.write("print(\"    out: {0}={{0}}\".format({0}))\n".format(tgtname))
        f.write("print('#' * 80)\n")
        f.write("print()\n")
    ##################################################################################
    return None
    '''
QuantumCircuit.x = x
