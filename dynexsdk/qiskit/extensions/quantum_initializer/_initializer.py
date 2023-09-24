"""
Qiskit Dynex SDK (beta) Neuromorphic Computing Library
Copyright (c) 2021-2023, Dynex Developers

All rights reserved.

1. Redistributions of source code must retain the above copyright notice, this list of
    conditions and the following disclaimer.
 
2. Redistributions in binary form must reproduce the above copyright notice, this list
   of conditions and the following disclaimer in the documentation and/or other
   materials provided with the distribution.
 
3. Neither the name of the copyright holder nor the names of its contributors may be
   used to endorse or promote products derived from this software without specific
   prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

__version__ = "0.0.1"
__author__ = 'Dynex Developers'
__credits__ = 'Dynex Developers, Contributors, Supporters and the Dynex Community'

import math
import numpy as np
import scipy

from dynexsdk.qiskit import CompositeGate
from dynexsdk.qiskit import Gate
from dynexsdk.qiskit import QISKitError
from dynexsdk.qiskit import QuantumCircuit
from dynexsdk.qiskit.extensions.standard.cx import CnotGate
from dynexsdk.qiskit.extensions.standard.ry import RYGate
from dynexsdk.qiskit.extensions.standard.rz import RZGate

class InitializeGate(CompositeGate):
    pass

    def __init__(self, param, qargs, circ=None):
        pass

    def nth_qubit_from_least_sig_qubit(self, nth):
        pass

    def reapply(self, circ):
        pass

    def gates_to_uncompute(self):
        pass

    def _rotations_to_disentangle(local_param):
        pass

    def _bloch_angles(pair_of_complex):
        pass

    def _multiplex(self, bottom_gate, bottom_qubit_index, list_of_angles):
        pass

    def chop_num(numb):
        pass

def reverse(self):
    pass

def optimize_gates(self):
    pass

def remove_zero_rotations(self):
    pass

def number_atomic_gates(self):
    pass

def remove_double_cnots_once(self):
    pass

def first_atomic_gate_host(self):
    pass

def last_atomic_gate_host(self):
    pass

def initialize(self, params, qubits):
    pass

