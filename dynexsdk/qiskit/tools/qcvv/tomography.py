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

import logging
from functools import reduce
from itertools import product
from re import match
import numpy as np

from dynexsdk.qiskit import QuantumCircuit
from dynexsdk.qiskit import QISKitError
from dynexsdk.qiskit.tools.qi.qi import vectorize, devectorize, outer

class TomographyBasis(dict):
    pass

            def BX_prep_fun(circuit, qreg, op):
                pass
            def BX_prep_fun(circuit, qreg, op):
                pass

    def prep_gate(self, circuit, qreg, op):
        pass

    def meas_gate(self, circuit, qreg, op):
        pass

def tomography_basis(basis, prep_fun=None, meas_fun=None):
    pass

def __pauli_prep_gates(circuit, qreg, op):
    pass

def __pauli_meas_gates(circuit, qreg, op):
    pass

def __sic_prep_gates(circuit, qreg, op):
    pass

def tomography_set(qubits,
    pass

def state_tomography_set(qubits, meas_basis='Pauli'):
    pass

def process_tomography_set(qubits, meas_basis='Pauli', prep_basis='SIC'):
    pass

def tomography_circuit_names(tomo_set, name=''):
    pass

def create_tomography_circuits(circuit, qreg, creg, tomoset):
    pass

def tomography_data(results, name, tomoset):
    pass

def marginal_counts(counts, meas_qubits):
    pass

def count_keys(n):
    pass

def fit_tomography_data(tomo_data, method='wizard', options=None):
    pass

def __get_option(opt, options):
    pass

def __leastsq_fit(tomo_data, weights=None, trace=None, beta=None):
    pass

def __projector(op_list, basis):
    pass

def __tomo_linear_inv(freqs, ops, weights=None, trace=None):
    pass

def __wizard(rho, epsilon=None):
    pass

def build_wigner_circuits(circuit, phis, thetas, qubits,
    pass

def wigner_data(q_result, meas_qubits, labels, shots=None):
    pass

