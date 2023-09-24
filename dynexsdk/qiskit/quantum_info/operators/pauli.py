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

import warnings
import numpy as np
from scipy import sparse
from dynexsdk.qiskit import QISKitError

def _make_np_bool(arr):
    pass

class Pauli:
    pass

    def __init__(self, z=None, x=None, label=None):
        pass

    def from_label(cls, label):
        pass

    def _init_from_bool(self, z, x):
        pass

    def __len__(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __imul__(self, other):
        pass

    def __hash__(self):
        pass

    def v(self):
        pass

    def w(self):
        pass

    def z(self):
        pass

    def x(self):
        pass

    def sgn_prod(p1, p2):
        pass

    def numberofqubits(self):
        pass

    def to_label(self):
        pass

    def to_matrix(self):
        pass

    def to_spmatrix(self):
        pass

    def update_z(self, z, indices=None):
        pass

    def update_x(self, x, indices=None):
        pass

    def insert_paulis(self, indices=None, paulis=None, pauli_labels=None):
        pass

    def append_paulis(self, paulis=None, pauli_labels=None):
        pass

    def delete_qubits(self, indices):
        pass

    def random(cls, num_qubits):
        pass

    def pauli_single(cls, num_qubits, index, pauli_label):
        pass

    def kron(self, other):
        pass

    def _prod_phase(p1, p2):
        pass

def pauli_group(number_of_qubits, case='weight'):
    pass






