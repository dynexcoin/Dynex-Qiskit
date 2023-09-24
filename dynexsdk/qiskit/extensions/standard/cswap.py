# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""
Cswap gate. Fredkin gate - Controlled Swap.
"""
from dynexsdk.qiskit import Gate
from dynexsdk.qiskit import QuantumCircuit
from dynexsdk.qiskit._instructionset import InstructionSet
from dynexsdk.qiskit._quantumregister import QuantumRegister
from dynexsdk.qiskit.extensions.standard import header  # pylint: disable=unused-import


class FredkinGate(Gate):
    """Cswap gate."""

    def __init__(self, ctl1, tgt1, tgt2, circ=None):
        """Create new Cswap gate."""
        super().__init__("cswap", [], [ctl1, tgt1, tgt2], circ)

    def inverse(self):
        """Invert this gate."""
        return self  # self-inverse

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.cswap(self.qargs[0], self.qargs[1], self.qargs[2]))


def cswap(self, ctl1, tgt1, tgt2):
    
    ################# Recursively Call across all bits #########################
    if isinstance(ctl1, QuantumRegister) and \
       isinstance(tgt1, QuantumRegister) and \
       isinstance(tgt2, QuantumRegister) and \
       len(ctl1) == len(tgt2) and len(tgt1) == len(tgt2):
        for i in range(ctl1.size):
            self.cswap((ctl1, i), (tgt1, i), (tgt2, i))
        return None
    elif isinstance(ctl1, QuantumRegister) and \
       isinstance(tgt1, QuantumRegister) and \
       isinstance(tgt2, QuantumRegister):
       raise("All registers must be of the same size")
    ######################### Write Dwave CSWAP ################################
   
    ctl1name = ctl1[0].name + '_' + str(ctl1[1])
    tgt1name = tgt1[0].name + '_' + str(tgt1[1])
    tgt2name = tgt2[0].name + '_' + str(tgt2[1])
    self.annealergraph.add_Fredkin(ctl1name, tgt1name, tgt2name)

    
    '''
    import os
    import sys
    import __main__ as main

    ctl1name = ctl1[0].name + '_' + str(ctl1[1])
    tgt1name = tgt1[0].name + '_' + str(tgt1[1])
    tgt2name = tgt2[0].name + '_' + str(tgt2[1])

    filename = main.__file__.split(".")[0] + "_dwave.py"
    with open(filename, "a") as f:
        f.write("#" * 80 + "\n")
        f.write("## CCNOT - control1: {0} target1: {1} target2: {2} ##\n".format(ctl1name, tgt1name, tgt2name))
        f.write("#" * 80 + "\n")
        f.write("if \'{0}\' not in globals():\n".format(ctl1name, tgt1name, tgt2name))
        f.write("    {0}=0\n".format(ctl1name, tgt1name, tgt2name))
        f.write("if \'{1}\' not in globals():\n".format(ctl1name, tgt1name, tgt2name))
        f.write("    {1}=0\n".format(ctl1name, tgt1name, tgt2name))
        f.write("if \'{2}\' not in globals():\n".format(ctl1name, tgt1name, tgt2name))
        f.write("    {2}=0\n\n".format(ctl1name, tgt1name, tgt2name))
        f.write("qubit_biases = {{\'{1}\' : 1, \'{2}\' : 1, \'out{1}\' : 1, \'out{2}\' : 1, \'a\' : 6, \'b\' : 6}}\n".format(ctl1name, tgt1name, tgt2name))
        f.write("binding_weights = {{(\'{0}\', \'out{1}\') : 2, (\'{0}\', \'out{2}\') : 2, (\'{0}\', \'a\') : -4, (\'{0}\', \'b\') : -4, (\'{1}\', \'out{1}\') : -2, (\'{1}\', \'a\') : 2, (\'{1}\', \'b\') : -2, (\'{2}\', \'out{2}\') : -2, (\'{2}\', \'a\') : -2, (\'{2}\', \'b\') : 2, (\'out{1}\', \'a\') : -4, (\'out{2}\', \'b\') : -4}}\n".format(ctl1name, tgt1name, tgt2name))
        f.write("bqm = dimod.BinaryQuadraticModel(qubit_biases, binding_weights, 0, dimod.BINARY)\n")
        f.write("sampler = dimod.ExactSolver()\n")
        f.write("response = sampler.sample(bqm)\n\n")
        f.write("for sample, energy in response.data(['sample', 'energy']):\n")
        f.write("    if sample[\'{0}\']=={0} and sample[\'{1}\']=={1} and sample[\'{2}\']=={2} and int(energy)==0:\n".format(ctl1name, tgt1name, tgt2name))
        f.write("        {0}=sample[\'{0}\']\n".format(ctl1name, tgt1name, tgt2name))
        f.write("        {1}=sample[\'out{1}\']\n".format(ctl1name, tgt1name, tgt2name))
        f.write("        {2}=sample[\'out{2}\']\n".format(ctl1name, tgt1name, tgt2name))
        f.write("        tgt1_before = sample[\'{1}\']\n".format(ctl1name, tgt1name, tgt2name))
        f.write("        tgt2_before = sample[\'{2}\']\n".format(ctl1name, tgt1name, tgt2name))
        f.write("        break\n\n")
        f.write("print('#' * 80)\n")
        f.write("print(\"CSWAP operation on {0} (control), {1} (target1) and {2} (target2):\")\n".format(ctl1name, tgt1name, tgt2name))
        f.write("print(\"    in:  {0}={{0}}, {1}={{1}}, {2}={{2}}\".format({0}, tgt1_before, tgt2_before))\n".format(ctl1name, tgt1name, tgt2name))
        f.write("print(\"    out: {0}={{0}}, {1}={{1}}, {2}={{2}}\".format({0}, {1}, {2}))\n".format(ctl1name, tgt1name, tgt2name))
        f.write("print('#' * 80)\n")
        f.write("print()\n")

    ##################################################################################
    return None
    '''

QuantumCircuit.cswap = cswap
