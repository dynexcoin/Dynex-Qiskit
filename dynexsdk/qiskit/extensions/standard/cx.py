# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

# pylint: disable=invalid-name

"""
controlled-NOT gate.
"""
from dynexsdk.qiskit import Gate
from dynexsdk.qiskit import QuantumCircuit
from dynexsdk.qiskit._instructionset import InstructionSet
from dynexsdk.qiskit._quantumregister import QuantumRegister
from dynexsdk.qiskit.extensions.standard import header  # pylint: disable=unused-import


class CnotGate(Gate):
    """controlled-NOT gate."""

    def __init__(self, ctl, tgt, circ=None):
        """Create new CNOT gate."""
        super().__init__("cx", [], [ctl, tgt], circ)

    def inverse(self):
        """Invert this gate."""
        return self  # self-inverse

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.cx(self.qargs[0], self.qargs[1]))


def cx(self, ctl, tgt):
    if isinstance(ctl, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and len(ctl) == len(tgt):
        for i in range(ctl.size):
            self.cx((ctl, i), (tgt, i))
        return None

    if isinstance(ctl, QuantumRegister):
        for j in range(ctl.size):
            self.cx((ctl, j), tgt)
        return None

    if isinstance(tgt, QuantumRegister):
        for j in range(tgt.size):
            self.cx(ctl, (tgt, j))
        return None

    ctlname = ctl[0].name + '_' + str(ctl[1])
    tgtname = tgt[0].name + '_' + str(tgt[1])
    self.annealergraph.add_CNOT(ctlname,tgtname)

    '''
    ############################## Write Dwave CNOT ##################################

    import os
    import sys
    import __main__ as main

    ctlname = ctl[0].name + '_' + str(ctl[1])
    tgtname = tgt[0].name + '_' + str(tgt[1])

    filename = main.__file__.split(".")[0] + "_dwave.py"
    with open(filename, "a") as f:
        f.write("#" * 80 + "\n")
        f.write("## CNOT - control: {0} target: {1} ##\n".format(ctlname,tgtname))
        f.write("#" * 80 + "\n")
        f.write("if \'{0}\' not in globals():\n".format(ctlname,tgtname))
        f.write("    {0}=0\n".format(ctlname,tgtname))
        f.write("if \'{1}\' not in globals():\n".format(ctlname,tgtname))
        f.write("    {1}=0\n\n".format(ctlname,tgtname))
        f.write("bqm = dimod.BinaryQuadraticModel({{'{0}\' : 1, \'{1}\' : 1, \'out{1}\' : 1, \'anc\' : 4}}, {{(\'{0}\', \'{1}\') : 2, (\'{0}\', \'out{1}\') : -2, (\'{1}\', \'out{1}\') : ".format(ctlname,tgtname))
        f.write("-2, (\'{0}\', \'anc\') : -4, (\'{1}\', \'anc\') : -4, (\'out{1}\', \'anc\') : 4}}, 0, dimod.BINARY)\n".format(ctlname,tgtname))
        f.write("sampler = dimod.ExactSolver()\n")
        f.write("response = sampler.sample(bqm)\n\n")
        f.write("for sample, energy in response.data(['sample', 'energy']):\n")
        f.write("    if sample[\'{0}\']=={0} and sample[\'{1}\']=={1} and int(energy)==0:\n".format(ctlname,tgtname))
        f.write("        {0}=sample[\'{0}\']\n".format(ctlname,tgtname))
        f.write("        {1}=sample[\'out{1}\']\n".format(ctlname,tgtname))
        f.write("        tgt_before = sample[\'{1}\']\n".format(ctlname,tgtname))
        f.write("        break\n\n")
        f.write("print('#' * 80)\n")
        f.write("print(\"CNOT operation on {0} (control) and {1} (target):\")\n".format(ctlname,tgtname))
        f.write("print(\"    in:  {0}={{0}}, {1}={{1}}\".format({0},tgt_before))\n".format(ctlname,tgtname))
        f.write("print(\"    out: {0}={{0}}, {1}={{1}}\".format({0},{1}))\n".format(ctlname,tgtname))
        f.write("print('#' * 80)\n")
        f.write("print()\n")

    ##################################################################################

    return None
    '''

QuantumCircuit.cx = cx
