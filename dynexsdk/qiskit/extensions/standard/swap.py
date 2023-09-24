# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""
swap gate.
"""
from dynexsdk.qiskit import Gate
from dynexsdk.qiskit import QuantumCircuit
from dynexsdk.qiskit._instructionset import InstructionSet
from dynexsdk.qiskit._quantumregister import QuantumRegister
from dynexsdk.qiskit.extensions.standard import header  # pylint: disable=unused-import


class SwapGate(Gate):
    """swap gate."""

    def __init__(self, ctl, tgt, circ=None):
        """Create new SWAP gate."""
        super().__init__("swap", [], [ctl, tgt], circ)

    def inverse(self):
        """Invert this gate."""
        return self  # self-inverse

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.swap(self.qargs[0], self.qargs[1]))



def swap(self, ctl, tgt):
    """Apply SWAP from ctl to tgt."""
    if isinstance(ctl, QuantumRegister) and \
            isinstance(tgt, QuantumRegister) and len(ctl) == len(tgt):
        for j in range(ctl.size):
            self.swap((ctl, j), (tgt, j))
        return None

    ctlname = ctl[0].name + "_" + str(ctl[1])
    tgtname = tgt[0].name + "_" + str(tgt[1])

    self.annealergraph.add_swap(ctlname,tgtname)

    '''
    ############################## Write Dwave SWAP ##################################
    elif isinstance(ctl, QuantumRegister) and \
       isinstance(tgt, QuantumRegister):
       raise("All registers must be of the same size")

    import os
    import sys
    import __main__ as main

    ctlname = ctl[0].name + "_" + str(ctl[1])
    tgtname = tgt[0].name + "_" + str(tgt[1])

    filename = main.__file__.split(".")[0] + "_dwave.py"
    with open(filename, "a") as f:
        f.write("#" * 80 + "\n")
        f.write("## SWAP - control: {0} target: {1} ##\n".format(ctlname, tgtname))
        f.write("#" * 80 + "\n")
        f.write("if \'{0}\' not in globals():\n".format(ctlname, tgtname))
        f.write("    {0}=0\n".format(ctlname, tgtname))
        f.write("if \'{1}\' not in globals():\n".format(ctlname, tgtname))
        f.write("    {1}=0\n\n".format(ctlname, tgtname))
        f.write("qubit_biases = {{\'{0}\' : 1, \'{1}\' : 1, \'out{0}\' : 1, \'out{1}\' : 1, \'a\' : 6, \'b\' : 6}}\n".format(ctlname, tgtname))
        f.write("binding_weights = {{(\'c\', \'out{0}\') : 2,(\'c\',\'out{1}\') : 2, (\'c\', \'a\') : -4, (\'c\', \'b\') : -4, (\'{0}\', \'out{0}\') : -2, (\'{0}\', \'a\') : 2, (\'{0}\', \'b\') : -2, (\'{1}\', \'out{1}\') : -2, (\'{1}\', \'a\') : -2, (\'{1}\', \'b\') : 2, (\'out{0}\', \'a\') : -4, (\'out{1}\', \'b\') : -4}}\n".format(ctlname, tgtname))
        f.write("bqm = dimod.BinaryQuadraticModel(qubit_biases, binding_weights, 0, dimod.BINARY)\n")
        f.write("sampler = dimod.ExactSolver()\n")
        f.write("response = sampler.sample(bqm)\n\n")
        f.write("for sample, energy in response.data(['sample', 'energy']):\n")
        f.write("    if sample[\'c\']==1 and sample[\'{0}\']=={0} and sample[\'{1}\']=={1} and int(energy)==0:\n".format(ctlname, tgtname))
        f.write("        {0}=sample[\'out{0}\']\n".format(ctlname, tgtname))
        f.write("        {1}=sample[\'out{1}\']\n".format(ctlname, tgtname))
        f.write("        tgt1_before = sample[\'{0}\']\n".format(ctlname, tgtname))
        f.write("        tgt2_before = sample[\'{1}\']\n".format(ctlname, tgtname))
        f.write("        break\n\n")
        f.write("print('#' * 80)\n")
        f.write("print(\"SWAP operation on {0} (control), {1} (target):\")\n".format(ctlname, tgtname))
        f.write("print(\"    in:  {0}={{0}}, {1}={{1}}\".format(tgt1_before, tgt2_before))\n".format(ctlname, tgtname))
        f.write("print(\"    out: {0}={{0}}, {1}={{1}}\".format({0}, {1}))\n".format(ctlname, tgtname))
        f.write("print('#' * 80)\n")
        f.write("print()\n")

    ##################################################################################
    return None
    '''
QuantumCircuit.swap = swap
