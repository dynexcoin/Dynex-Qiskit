# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""
Toffoli gate. Controlled-Controlled-X.
"""
from dynexsdk.qiskit import Gate
from dynexsdk.qiskit import QuantumCircuit
from dynexsdk.qiskit._instructionset import InstructionSet
from dynexsdk.qiskit._quantumregister import QuantumRegister
from dynexsdk.qiskit.extensions.standard import header  # pylint: disable=unused-import

class ToffoliGate(Gate):
    """Toffoli gate."""

    def __init__(self, ctl1, ctl2, tgt, circ=None):
        """Create new Toffoli gate."""
        super().__init__("ccx", [], [ctl1, ctl2, tgt], circ)

    def inverse(self):
        """Invert this gate."""
        return self  # self-inverse

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.ccx(self.qargs[0], self.qargs[1], self.qargs[2]))


def ccx(self, ctl1, ctl2, tgt):
    ################# Recursively Call across all bits #########################
    if isinstance(ctl1, QuantumRegister) and \
       isinstance(ctl2, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and \
       len(ctl1) == len(tgt) and len(ctl2) == len(tgt):
        for i in range(ctl1.size):
            self.ccx((ctl1, i), (ctl2, i), (tgt, i))
        return None

    ####################### Write Dwave CCNOT ##################################
    import os
    import sys
    import __main__ as main

    ctl1name = ctl1[0].name + '_' + str(ctl1[1])
    ctl2name = ctl2[0].name + '_' + str(ctl2[1])
    tgtname = tgt[0].name + '_' + str(tgt[1])
    
    self.annealergraph.add_Toffoli(ctl1name, ctl2name, tgtname)

    '''
    filename = main.__file__.split(".")[0] + "_dwave.py"
    with open(filename, "a") as f:
        f.write("#" * 80 + "\n")
        f.write("## CCNOT - control1: {0} control2: {1} target: {2} ##\n".format(ctl1name,ctl2name,tgtname))
        f.write("#" * 80 + "\n")
        f.write("if \'{0}\' not in globals():\n".format(ctl1name,ctl2name,tgtname))
        f.write("    {0}=0\n".format(ctl1name,ctl2name,tgtname))
        f.write("if \'{1}\' not in globals():\n".format(ctl1name,ctl2name,tgtname))
        f.write("    {1}=0\n".format(ctl1name,ctl2name,tgtname))
        f.write("if \'{2}\' not in globals():\n".format(ctl1name,ctl2name,tgtname))
        f.write("    {2}=0\n\n".format(ctl1name,ctl2name,tgtname))
        f.write("bqm = dimod.BinaryQuadraticModel({{\'anc1\' : 4, \'anc2\' : 4, \'out{2}\' : 1, \'{2}\' : 1}}, {{(\'anc1\', \'anc2\') : -4, (\'anc1\', \'out{2}\') : 4, ".format(ctl1name,ctl2name,tgtname))
        f.write("(\'anc1\',\'{2}\') : -4, (\'anc2\', \'{0}\') : -2, (\'anc2\', \'{1}\') : -2, (\'anc2\', \'out{2}\') : -2, (\'anc2\', \'{2}\') : 2, (\'{0}\', \'{1}\') : 1, ".format(ctl1name,ctl2name,tgtname))
        f.write("(\'out{2}\', \'{2}\') : -2}}, 0, dimod.BINARY)\n".format(ctl1name,ctl2name,tgtname))
        f.write("sampler = dimod.ExactSolver()\n")
        f.write("response = sampler.sample(bqm)\n\n")
        f.write("for sample, energy in response.data(['sample', 'energy']):\n")
        f.write("    if sample[\'{0}\']=={0} and sample[\'{1}\']=={1} and sample[\'{2}\']=={2} and int(energy)==0:\n".format(ctl1name,ctl2name,tgtname))
        f.write("        {0}=sample[\'{0}\']\n".format(ctl1name,ctl2name,tgtname))
        f.write("        {1}=sample[\'{1}\']\n".format(ctl1name,ctl2name,tgtname))
        f.write("        {2}=sample[\'out{2}\']\n".format(ctl1name,ctl2name,tgtname))
        f.write("        tgt_before = sample[\'{2}\']\n".format(ctl1name,ctl2name,tgtname))
        f.write("        break\n\n")
        f.write("print('#' * 80)\n")
        f.write("print(\"CCNOT operation on {0} (control1), {1} (control2) and {2} (target):\")\n".format(ctl1name,ctl2name,tgtname))
        f.write("print(\"    in:  {0}={{0}}, {1}={{1}}, {2}={{2}}\".format({0},{1},tgt_before))\n".format(ctl1name,ctl2name,tgtname))
        f.write("print(\"    out: {0}={{0}}, {1}={{1}}, {2}={{2}}\".format({0},{1},{2}))\n".format(ctl1name,ctl2name,tgtname))
        f.write("print('#' * 80)\n")
        f.write("print()\n")
    ############################################################################
    return None
    '''
QuantumCircuit.ccx = ccx
